from django.shortcuts import render

def index(request):
    return render(request, 'mda_mentoring/index.html')
