from .models import Comment, Profile
from django import forms
from django.forms import ModelForm
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


class ProfileEditForm(forms.ModelForm):

    """
    Form to edit profile
    """

    featured_image = forms.FileField(label='Image')
    about_me = forms.CharField(
                            label='About Me:',
                            required=False,
                            max_length=300,
                            widget=forms.Textarea)
    favourite_country = forms.CharField(
                                    label='My Favourite Countries:',
                                    required=False,
                                    max_length=100,
                                    widget=forms.Textarea, )

    class Meta:
        model = Profile
        fields = (
                'featured_image', 'about_me',
                'favourite_country')
