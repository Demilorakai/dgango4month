from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .forms import RegistrationForm, LoginForm, MyPasswordChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.urls import reverse_lazy


class RegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = "register.html"
    success_url = "/login/"


def profile(request):
    return render(request, 'profile.html')

class MyPasswordChangeView(PasswordChangeView):
    template_name = "registration/account.html"
    success_url = reverse_lazy("users:change")


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = "registration/account_change.html"

