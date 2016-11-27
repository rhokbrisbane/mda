from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'mentee', views.mentee_profile),
]
