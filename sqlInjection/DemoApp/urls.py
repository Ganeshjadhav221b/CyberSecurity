"""
BackgateStore URL Configuration
"""
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from . import views

urlpatterns = [
   path('', views.index, name = "index"),
   path(r'signup', views.signup, name = "signup"),
   path(r'login',views.login, name= 'login'),
   path(r'profile', views.profile, name = "profile"),
   path(r'accounts/profile/', views.profile, name = "profilet"),
   path('logout/', auth_views.LogoutView.as_view(template_name='DemoApp/logout.html'), name='logout'),

  ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)