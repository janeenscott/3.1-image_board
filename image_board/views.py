from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Image

class Board(TemplateView):         # Has to be called Board because this is what we're importing in URLs.py
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        images = Image.objects.all()
        # images is a list

        context = {
            'images': images
        }

        return context
