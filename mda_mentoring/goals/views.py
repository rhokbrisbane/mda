from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Goal

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class IndexView(generic.ListView):
    template_name = 'goals/index.html'
    context_object_name = 'goal_list'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Goal.objects.order_by('name')

class DetailView(generic.DetailView):
    model = Goal
    template_name = 'goals/detail.html'
