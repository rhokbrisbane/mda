from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Goal

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'goals/index.html'
    context_object_name = 'goal_list'

    def get_queryset(self):
        return Goal.objects.order_by('name')

class DetailView(generic.DetailView):
    model = Goal
    template_name = 'goals/detail.html'
