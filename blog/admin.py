from django.contrib import admin
from .models import Post, Comment, Profile, GalleryBlog
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Add fields which will use summernote editor in admin panel
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Add fields for additional display in admin panel
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'about_me', 'featured_image',
                    'favourite_country')


@admin.register(GalleryBlog)
class GalleryBlog(admin.ModelAdmin):

    list_display = ('name', 'active', 'image')
