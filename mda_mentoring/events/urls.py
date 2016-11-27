from django.conf.urls import url

from .views import EventListView, EventDetailsView

urlpatterns = [
    url(r'eventList/', EventListView.as_view()),
    url(r'event/(?P<pk>\d+)/$', EventDetailsView.as_view()),
]
