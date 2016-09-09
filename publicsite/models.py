import datetime

import pytz
from django.db import models
from .managers import EventManager, VisitorManger


class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return "{0} [{1}]".format(self.name, self.address)


class MapSetting(models.Model):
    name = models.CharField(max_length=100)
    map_center_latitude = models.FloatField(null=True)
    map_center_longitude = models.FloatField(null=True)
    map_zoom = models.IntegerField(null=True)

    def __str__(self):
        return self.name


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
    map_settings = models.ForeignKey(
        MapSetting,
        on_delete=models.SET_NULL,
        null=True
    )

    objects = EventManager()

    @property
    def registration_enabled(self):
        now = datetime.datetime.now(tz=pytz.UTC)
        return self.publication.stop_registration_date > now

    def __str__(self):
        return "{0} [{1}]".format(self.name, self.date)

    class Meta:
        ordering = ['date']


class EventPublication(models.Model):
    start_publication_date = models.DateTimeField(null=True)
    stop_publication_date = models.DateTimeField(null=True)
    stop_registration_date = models.DateTimeField(null=True)
    event = models.OneToOneField(
        Event,
        related_name='publication',
        on_delete=models.CASCADE,
        primary_key=True,
    )


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
        null=False,
        on_delete=models.CASCADE,
        related_name='points'
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    start = models.TimeField()
    duration = models.DurationField()
    authors = models.ManyToManyField(Author)

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
    registered_at = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='visitors'
    )

    objects = VisitorManger()

    def __str__(self):
        return "{0} [{1}]".format(self.name, self.email)
