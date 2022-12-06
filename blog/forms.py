from .models import Comment
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):

    """
    Form for post comment
    """

    class Meta:
        """
        Form has field of body from Comment model
        """
        model = Comment
        fields = ('body',)