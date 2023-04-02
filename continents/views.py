from django.shortcuts import render, get_list_or_404
from .models import Continent


def continents_all(request):
    """
    Get all continents and return template.
    """
    continents = get_list_or_404(Continent)

    context = {
        'continents': continents,
    }

    return render(request, 'continents/continents.html', context)