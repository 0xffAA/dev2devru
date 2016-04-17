from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.current_event, name='main'),
    url(r'^event/(?P<event_name>[\w\-_]*)$', views.view_event, name='event_name'),
    url(r'^history$', views.events_history, name='history'),
    url(r'^about$', views.about, name='about'),
    url(r'^contribute$', views.contribute, name='contribute')
]