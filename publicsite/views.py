from django.shortcuts import render


def view_event(request, event_name=None):
    return render(request, 'view_event.html', None)
