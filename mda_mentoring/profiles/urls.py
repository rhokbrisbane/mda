from django.conf.urls import url

from .views import LoginView, LogoutView, CreateProfileView, ProfileView

urlpatterns = [
    url(r'login/', LoginView.as_view()),
    url(r'logout/', LogoutView.as_view()),
    url(r'create/', CreateProfileView.as_view()),
    url(r'view/', ProfileView.as_view())
]
