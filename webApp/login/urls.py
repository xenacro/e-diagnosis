from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('', views.indexView, name="home"),
    path('dashboard/', include('dashboard.urls')),
    path('login/', LoginView.as_view(), name="login_url"),
    path('register/', views.registerView, name="register_url"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
