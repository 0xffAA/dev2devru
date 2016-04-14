from django.shortcuts import render
from .models import Event
from .view_models import EventVM


def current_event(request):
    event = EventVM(
        Event.objects.get_current()
    )
    return render(
        request,
        'view_event.html' if event else 'empty_event.html',
        {'event': event}
    )


def view_event(request, event_name=None):
    event = EventVM(
        Event.objects.get_by_name(event_name)
    )
    return render(
        request,
        'view_event.html',
        {'event': event}
    )


def events_history(request):
    pass


def about(request):
    pass


def contribute(request):
    pass