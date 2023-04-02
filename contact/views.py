from django.shortcuts import render
from django.views import generic, View
from django.conf import settings
from .forms import ContactForm
from .models import Contact


class ContactUs(View):
    """
    This view is used to display the contact form and
    handle GET and POST requests
    """

    def get(self, request):
        """
        Renders the contact form
        """
        if request.user.is_authenticated:
            form = ContactForm(initial={'email': request.user.email})
        else:
            form = ContactForm()

        return render(
            request,
            "contact/contact.html",
            {
                "contact_form": form,
            },
        )
