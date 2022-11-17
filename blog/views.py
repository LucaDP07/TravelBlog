from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render (
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked, 
                "comment_form": CommentForm()

            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

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


        return render (
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked, 
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.info(
                request, 'You took the favourite star away from this post!')
        else:
            post.likes.add(request.user)
            messages.success(request, 'You gave this post a favourite star!')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class MyTripList(LoginRequiredMixin, generic.ListView):
    """
    Displays logged in user's own recipes
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'mytrips.html'
    context_object_name = 'blog'


class TripCreate(
                  SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    """
    Logged in user can create a recipe and add to my recipes list
    """
    model = Post
    fields = ['trip_image', 'title', 'text', ]
    template_name = 'mytrips.html'
    success_url = reverse_lazy('mytrips')
    success_message = "You have successfully created a post!"

    def form_valid(self, form):
        """
        Sets logged in user as author field in form
        Sets form default status to published
        """
        form.instance.author = self.request.user
        form.instance.status = 1
        return super(TripCreate, self).form_valid(form)