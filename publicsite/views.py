from django.shortcuts import render
from django.http import Http404

from .models import Event, Visitor
from .forms import NewVisitorForm
from .view_models import EventVM


def current_event(request):
    event = Event.objects.get_current()
    if event:
        return render(
            request,
            'view_event.html',
            {'event': EventVM(event), 'form': NewVisitorForm(initial={'event': event})}
        )
    else:
        return render(
            request,
            'empty_event.html'
        )


def view_event(request, event_name=None):
    event = Event.objects.get_by_name(event_name)
    if not event:
        raise Http404("Event doesn't exist...")
    return render(
        request,
        'view_event.html',
        {'event': EventVM(event)}
    )


def events_history(request):
    events = Event.objects.get_history()
    return render(
        request,
        'events_list.html',
        {'events': events}
    )


def about(request):
    pass


def contribute(request):
    pass