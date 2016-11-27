from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

from .models import Profile
from mda_mentoring.settings import LOGIN_URL


class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/goals/')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(LOGIN_URL)

        return render(request, "index.html")

    def get(self, request):
        return render(request, "login.html")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(LOGIN_URL)

class CreateProfileView(CreateView):
    # TODO : creating profiles work incorrect now
    model = Profile
    fields = ['username', 'email', 'password', 'phone_number', 'experience']
    template_name = "create_profile.html"
    success_url = '/goals/'
