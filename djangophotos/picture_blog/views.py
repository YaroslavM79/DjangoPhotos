from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth import login, logout
from django.contrib import messages

from .models import picture_blog

# Create your views here.
