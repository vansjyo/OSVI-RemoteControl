# accounts/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('single_user', views.single_user, name='single_user'),
    path('time_up', views.time_up, name='time_up'),
    path('team', views.team, name='team'),
]
