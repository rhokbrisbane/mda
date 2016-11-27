from django.shortcuts import render

from django.views.generic import View, ListView
from django.views.generic.detail import DetailView

from events.models import Event

class EventListView(ListView):
    template_name = 'event_list.html'

    def get_queryset(self):
        return Event.objects.all()

class EventDetailsView(DetailView):
    model = Event
    template_name = 'event.html'
