from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *
urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('contact/', feedback_form, name='contact'),

    path('', HomeNews.as_view(), name='home'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),

]
