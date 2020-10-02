from django.shortcuts import render
from .models import User
from . forms import SignUpForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages



class UserCreateView(CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = "account/user.html"

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

class Login(LoginView):
    form_class = SignUpForm
    template_name = 'account/login.html'

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)


class Logout(LogoutView):
    template_name = 'account/login.html'





