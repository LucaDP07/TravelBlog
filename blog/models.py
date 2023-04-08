"""
Imports
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Model for post
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', blank=False)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blogpost_like', blank=True)
    content = models.TextField(blank=False,)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)

    class Meta:
        """
        Posts ordered to show newest first to show regular updates
        """
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        """
        Returns total number of times users have liked a post
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Model for comment. Logged in user can leave a comment for a post
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)


class Meta:
    """
    Comments ordered from the oldest to the newest
    """
    ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', default='placeholder')
    about_me = models.TextField(max_length=300, blank=True)
    favourite_country = models.TextField(max_length=100, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class GalleryBlog(models.Model):
    """
    Model for galleryimages.
    """
    name = models.CharField(max_length=150, unique=False, default="image")
    image = CloudinaryField('image', default='placeholder')
    active = models.BooleanField(default=False)
