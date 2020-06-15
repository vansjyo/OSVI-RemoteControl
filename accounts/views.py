# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from django.shortcuts import render

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def single_user(request):
    logout(request)
    return render(request, 'single_user.html')


def time_up(request):
    logout(request)
    return render(request, 'time_up.html')

def team(request):
    return render(request, 'team.html')
