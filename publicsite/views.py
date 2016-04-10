from django.shortcuts import render
from .models import Event

def view_event(request, event_name=None):
    event = None
    if event_name:
        event = Event.objects.get_by_name(event_name)
    if not event:
        event = Event.objects.get_current()
    return render(request, 'view_event.html' if event else 'empty_event.html', event)
