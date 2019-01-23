from django.db import models

from django.conf import settings
from django.db import models
from django.utils import timezone


class Image(models.Model):
    image = models.URLField()
    title = models.CharField(max_length=200)
    caption = models.TextField(null=True)
