from .models import *
import datetime


def _get_first_or_none(qs):
    query_result = list(qs[:1])
    if query_result:
        return query_result[0]
    else:
        return None


def query_current_event():
    current_date = datetime.datetime.utcnow().date()

    event = _get_first_or_none(Event.objects.order_by('date').filter(date__date__qt=current_date))
    if not event:
        event = _get_first_or_none(Event.objects.order_by('-date').filter(date__date__lt=current_date))

    return event
