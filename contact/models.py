""" Contact Models """

from django.db import models
from django.urls import reverse


class Contact(models.Model):
    """ Model for Contact """

    name = models.CharField(max_length=122, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=200, null=False, blank=False)
    message = models.TextField(max_length=500, default='')
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """Get url after user submits message """
        return reverse('home')

    def __str__(self):
        return f"Enquiry: {self.subject} from {self.name}"
