# from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.core.paginator import Paginator
from django.contrib.auth import login, logout
from django.contrib import messages

from .forms import UserLoginForm, UserRegisterForm, AddPictureForm
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

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'picture_blog/login.html', {"form": form})

def user_logout(request):
    logout(request)
    return redirect('login')



class HomePicturesView(ListView):
    model = PictureBlog  # по сути сделали news = News.objects.all()
    template_name = 'picture_blog/home_pictures_list.html'
    context_object_name = 'pictures'
    queryset = PictureBlog.objects.all()
    paginate_by = 10
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main Page'
        return context

    def get_queryset(self):
        return PictureBlog.objects.filter(is_published=True)


class AddPicture(CreateView):
    model = PictureBlog
    form_class = AddPictureForm
    template_name = 'picture_blog/add_picture.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.user = self.request.user
        return super().form_valid(form)


class ViewPicture(DetailView):
    model = PictureBlog
    template_name = 'picture_blog/view_user_pictures.html'


class MyPicturesView(ListView):
    model = PictureBlog
    template_name = 'picture_blog/my_pictures_list.html'
    context_object_name = 'pictures'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main Page'
        return context

    def get_queryset(self):
        return PictureBlog.objects.filter(author=self.request.user)
