from django.db import models
import datetime


def _get_first_or_none(qs):
    query_result = list(qs[:1])
    if query_result:
        return query_result[0]
    else:
        return None


class EventManager(models.Manager):
    def get_current(self):
        current_date = datetime.datetime.utcnow().date()

        event = _get_first_or_none(self.get_query_set().order_by('date').filter(date__date__qt=current_date))
        if not event:
            event = _get_first_or_none(self.get_query_set().order_by('-date').filter(date__date__lt=current_date))

        return event

    def by_name(self, name):
        _get_first_or_none(self.get_query_set().filter(public_name=name))
