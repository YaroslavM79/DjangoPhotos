from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
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
    path('picture/<int:pk>/', ViewPicture.as_view(), name='view_picture'),
    path('picture/add-picture/', AddPicture.as_view(), name='add_picture'),


]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)