from django.db import models
from .managers import *


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date = models.DateField()
    public_name = models.SlugField(max_length=20, null=False)

    objects = EventManager()


class Section(models.Model):
    name = models.CharField(max_length=100)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='sections'
    )


class Author(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)


class Point(models.Model):
    section = models.ForeignKey(
        Section,
        null=True,
        on_delete=models.SET_NULL,
        related_name='points'
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    start = models.TimeField()
    duration = models.DurationField()
    authors = models.ManyToManyField(Author)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='points'
    )

    class Meta:
        ordering = ['start']


class Materials(models.Model):
    slides = models.URLField()
    video = models.URLField()
    sources = models.URLField()
    point = models.ForeignKey(
        Point,
        on_delete=models.CASCADE,
        related_name='materials'
    )