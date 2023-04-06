from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import CommentForm
from .forms import ProfileEditForm
from django.views import generic, View
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Post, Profile


class PostList(generic.ListView):
    """
    Adjusts site’s pagination to max six posts
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        """
        Displays full published posts with approved comments
        Checks if post has been liked by current user
        Logged In User can like or unlike a post
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        is_favourite = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        if post.favourite.filter(id=self.request.user.id).exists():
            is_favourite = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "is_favourite": is_favourite,
                "comment_form": CommentForm()

            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Displays full published posts with approved comments
        Checks if post has been liked by current user
        User can submit a comment form for approval by admin
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        is_favourite = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        if post.favourite.filter(id=self.request.user.id).exists():
            is_favourite = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Thanks for leaving a comment!')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "is_favourite": is_favourite,
                "comment_form": CommentForm()
            },
        )


class FavouritePost(LoginRequiredMixin, View):
    """
    This view allows a logged in user to add a post to favourites.
    """
    def post(self, request, slug):
        """
        Checks if user id already exists in the favourites
        field in the Post database.
        If they exist then remove them from the database.
        If they don't exist then add them to the database.
        """
        post = get_object_or_404(Post, slug=slug)
        if post.favourite.filter(id=request.user.id).exists():
            post.favourite.remove(request.user)
            messages.success(self.request, 'Post removed from favourites')
        else:
            post.favourite.add(request.user)
            messages.success(self.request, 'Post added to favourites')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class MyFavourites(LoginRequiredMixin, generic.ListView):
    """
    This view allows a logged in user to view their favourite posts.
    """
    model = Post
    template_name = 'my_favourites.html'
    paginate_by = 8

    def get_queryset(self):
        """Override get_queryset to filter by user favourites"""
        return Post.objects.filter(favourite=self.request.user.id)


class PostLike(View):
    """
    Logged in user can like or unlike a post
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.info(
                request, 'You unliked this post!')
        else:
            post.likes.add(request.user)
            messages.success(request, 'You liked this post!')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class CreateTrip(
                  SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    """
    Logged in user can create a post
    """
    model = Post
    fields = ['title', 'excerpt', 'content', 'featured_image', 'slug']
    template_name = 'trip_form.html'
    success_url = reverse_lazy('home')
    success_message = "You have successfully created a post!"

    def form_valid(self, form):
        """
        Sets logged in user as author field in form
        Sets form default status to published
        """
        form.instance.author = self.request.user
        form.instance.status = 1
        return super(CreateTrip, self).form_valid(form)


class EditTrip(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    """
    Logged in user can edit a post
    """
    model = Post
    fields = ['title', 'excerpt', 'content', 'featured_image', 'slug']
    template_name = 'update_post.html'
    success_url = reverse_lazy('home')
    success_message = "Trip successfully updated!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = 1
        return super(EditTrip, self).form_valid(form)


class DeleteTrip(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView):
    """
    Logged in user can delete a post they created
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    success_message = "Trip deleted!"

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeleteTrip, self).delete(request, *args, **kwargs)


@login_required
def edit_profile(request):
    """ Display the user's profile to edit """
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileEditForm(
                            request.POST or None,
                            request.FILES,
                            instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile is successfully updated')
            return redirect('home')
        else:
            messages.error(request,
                           ('Update failed. Please ensure'
                            'the form is valid.'))
    else:
        form = ProfileEditForm(instance=profile)
    template = 'profile_edit.html'
    context = {'form': form, }

    return render(request, template, context)


class ProfileList(LoginRequiredMixin, generic.ListView):
    """Displays the member list page"""
    model = Profile
    queryset = Profile.objects.all()
    template_name = "profile.html"
    paginate_by = 8


class ProfileDetail(LoginRequiredMixin, generic.DetailView):
    """Displays profile detail page"""
    model = Profile
    queryset = Profile.objects.all()
    template_name = 'profile_detail.html'

    def get_object(self):
        return get_object_or_404(
                                Profile,
                                user__username=self.kwargs['username'])
