from django.db import models


class Continent(models.Model):
    """
    Model class for the continents app
    """
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='continents')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.name
