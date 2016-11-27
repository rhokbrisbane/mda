from django.conf.urls import url

from .views import LoginView, LogoutView, CreateProfileView, MenteeProfileView

urlpatterns = [
    url(r'login/', LoginView.as_view()),
    url(r'logout/', LogoutView.as_view()),
    url(r'create/', CreateProfileView.as_view()),
    url(r'view/', MenteeProfileView.as_view())
]
