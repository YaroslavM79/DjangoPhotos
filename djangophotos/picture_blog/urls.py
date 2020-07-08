from django.urls import path
from django.conf.urls import url
from django.views.decorators.cache import cache_page

from .views import *
urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    # path('contact/', feedback_form, name='contact'),
    #
    path('', HomePicturesView.as_view(), name='home'),
    # path('picture/<int:pk>/', ViewPicture.as_view(), name='view_picture'),
    path('picture/add-picture/', CreatePicture.as_view(), name='add_picture'),

]
