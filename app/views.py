from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import LoginView

class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')

class UserList(ListView):
    model = User
    template_name = 'home.html'
    context_object_name = 'users'

class FavoritesList(ListView):
    model = Favorites
    template_name = 'home.html'
    context_object_name = 'favorites'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all()
        return context
    
class UpdateUser(UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'update.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

class DeleteUser(DeleteView):
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'