from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django import forms
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

from .models import Profile
from mda_mentoring.settings import LOGIN_URL

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/profiles/view/')
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
    model = Profile
    fields = ['username', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'experience', 'field', 'qualification', 'language', 'is_mentor']
    template_name = "create_profile.html"
    success_url = '/goals/'

    def get_form(self, form_class):
        form = super(CreateProfileView, self).get_form(form_class)
        form.fields['password'].widget = forms.PasswordInput()
        return form

    def form_valid(self, form):
        self.object = form.save()
        self.object.set_password(self.object.password)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Create your views here.

class ProfileView(View):
    @method_decorator(login_required)
    def get(self, request):
        current_user = request.user
        if current_user.is_mentor:
            profile = current_user.mentee or current_user
        else:
            profile = Profile.objects.filter(mentee_id=current_user.id).first() or current_user

        return render(request, 'view_profile.html', {'profile': profile })
