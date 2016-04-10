from django.db import models
import datetime


def _get_current_date():
    return datetime.datetime.utcnow().date()


def _get_first_or_none(qs):
    query_result = list(qs[:1])
    if query_result:
        return query_result[0]
    else:
        return None


class EventManager(models.Manager):
    def _get_timeline(self, reverse=False):
        return self.order_by('-date' if reverse else 'date')

    def get_current(self):
        return _get_first_or_none(self._get_timeline().filter(date__gte=_get_current_date()))

    def get_by_name(self, name):
        _get_first_or_none(self.filter(public_name=name))

    def get_history(self):
        return self._get_timeline().filter(date__lt=_get_current_date())