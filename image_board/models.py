from django.db import models


class Image(models.Model):
    image = models.URLField()
    title = models.CharField(max_length=200)
    caption = models.TextField()
