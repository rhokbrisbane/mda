from django.shortcuts import render

# Create your views here.
# Create your views here.
def mentee_profile(request):
    return render(request, 'mentee/profile.html')
