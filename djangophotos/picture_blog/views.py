from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserLoginForm, UserRegisterForm

from .models import PictureBlog

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'registration successful')
            return redirect('home')
        else:
            messages.error(request, 'Error in registration')
    else:
        form = UserRegisterForm()
    return render(request, 'picture_blog/register.html', {"form": form})

