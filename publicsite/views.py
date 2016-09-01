import json

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST

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


@require_POST
@csrf_protect
def query_visitor(request):
    if request.is_ajax():
        try:
            email = json.loads(request.body.decode(encoding='UTF-8'))['email']
            result = Visitor.objects.filter(email=email).order_by('-registered_at')[0]
            return JsonResponse({
                'name': result.name,
                'position': result.position,
                'company': result.company
            })
        except:
            pass
    return JsonResponse({})


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