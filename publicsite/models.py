from django.db import models
from .managers import *


class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    place_latitude = models.FloatField()
    place_longitude = models.FloatField()
    center_latitude = models.FloatField(null=True)
    center_longitude = models.FloatField(null=True)
    zoom = models.IntegerField(null=True)

    def __str__(self):
        return "{0} [{1}]".format(self.name, self.address)


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date = models.DateField()
    public_name = models.SlugField(max_length=20, null=False)
    place = models.ForeignKey(
        Place,
        related_name='events',
        on_delete=models.CASCADE,
    )

    objects = EventManager()

    def __str__(self):
        return "{0} [{1}]".format(self.name, self.date)


class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='sections'
    )

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='speakers', null=True)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return "{0} [{1}~{2}]".format(self.title, self.start, self.duration)

    class Meta:
        ordering = ['start']


class Partner(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    logo = models.ImageField(upload_to='partners')
    events = models.ManyToManyField(
        Event,
        related_name='partners'
    )

    def __str__(self):
        return self.name


class Materials(models.Model):
    slides = models.URLField()
    video = models.URLField()
    sources = models.URLField()
    point = models.ForeignKey(
        Point,
        on_delete=models.CASCADE,
        related_name='materials'
    )

    def __str__(self):
        return "{0} {1} {2}".format(self.slides, self.video, self.sources)


class Visitor(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100, null=True)
    email = models.EmailField(db_index=True)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='visitors'
    )

    def __str__(self):
        return "{0} [{1}]".format(self.name, self.email)
