from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.current_event, name='main'),
    url(r'^(?P<event_name>[\w\-_]*)$', views.view_event, name='event_name')
]