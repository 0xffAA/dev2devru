import json

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse, HttpResponseForbidden, HttpResponseNotFound
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST, require_GET

from .models import Event, Visitor
from .forms import NewVisitorForm


@require_GET
def current_event(request):
    event = Event.objects.get_current()
    if event:
        return render(
            request,
            'view_event.html',
            {
                'event': event,
                'form': NewVisitorForm(initial={'event': event})
            }
        )
    else:
        return render(
            request,
            'empty_event.html'
        )


@require_POST
@csrf_protect
def query_visitor_information(request):
    if not request.is_ajax():
        return HttpResponseForbidden()

    email = json.loads(request.body.decode(encoding='UTF-8'))['email']
    result = Visitor.objects.get_latest_registration(email)

    if result:
        return JsonResponse({
            'name': result.name,
            'position': result.position,
            'company': result.company
        })
    else:
        return HttpResponseNotFound()


@csrf_protect
def register_new_visitor(request):
    if request.method == 'POST':
        form = NewVisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                'thanks_for_registration.html'
            )
        else:
            return render(
                request,
                'register_new_visitor.html',
                {'form': form}
            )
    else:
        return redirect(reverse('main'))


@require_GET
def view_event(request, event_name=None):
    event = Event.objects.get_by_name(event_name)
    if not event:
        raise Http404("Event doesn't exist...")
    return render(
        request,
        'view_event.html',
        {'event': event}
    )


@require_GET
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