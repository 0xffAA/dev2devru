from django.shortcuts import render
from .models import Event


def current_event(request):
    event = Event.objects.get_current()
    return render(request, 'view_event.html' if event else 'empty_event.html', event)


def view_event(request, event_name=None):
    event = Event.objects.get_by_name(event_name)
    return render(request, 'view_event.html', event)


def events_history(request):
    pass


def about(request):
    pass


def contribute(request):
    pass