from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test
from . forms import LoginUserForm, RegisterUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}
    def get_success_url(self):
        user = self.request.user
        if user.groups.filter(name='Creator').exists():
            return reverse_lazy("creator:anketa-list")
        elif user.groups.filter(name='Manager').exists():
            return reverse_lazy("manager:survey-list")
        elif user.groups.filter(name='Student').exists():
            return reverse_lazy("student:tests-list")
        else:
            return super().get_success_url()
    
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация"} 
    def get_success_url(self):
        return reverse_lazy('users:login')