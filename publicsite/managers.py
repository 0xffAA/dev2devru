from django.db.models import Count
from django.db.models.query import QuerySet
from django.db import models
import datetime


def _get_current_date():
    return datetime.datetime.utcnow()


def _get_first_or_none(qs):
    query_result = list(qs[:1])
    if query_result:
        return query_result[0]
    else:
        return None


class EventQuerySet(QuerySet):
    def published(self):
        return self.exclude(publication__isnull=True)

    def active_now(self):
        now = _get_current_date()
        return self.filter(
            publication__start_publication_date__lt=now,
            publication__stop_publication_date__gt=now,
        )

    def history(self):
        return self.filter(
            publication__stop_publication_date__gt=_get_current_date(),
        )

    def load_all(self):
        return self.select_related(
            'place',
            'map_settings',
        ).prefetch_related(
            'publication',
            'sections',
            'sections__points',
            'sections__points__authors',
            'sections__points__materials',
            'partners'
        )

    def with_visitors_count(self):
        return self.annotate(visitors_count=Count('visitors'))


class EventManager(models.Manager):
    @property
    def _qs(self):
        return EventQuerySet(self.model)

    def get_current(self):
        return _get_first_or_none(
            self._qs.active_now().order_by('-date').load_all().with_visitors_count()
        )

    def get_by_name(self, name):
        return _get_first_or_none(
            self._qs.filter(public_name=name).load_all()
        )

    def get_history(self):
        return self._qs.history().with_visitors_count()


class VisitorManger(models.Manager):
    def get_latest_registration(self, email):
        return _get_first_or_none(self.filter(email=email).order_by('-registered_at'))
