from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("alumnae/", views.alumnae, name="alumnae"),
    path("summer/", views.summer, name="summer"),
    path("rush/", views.rush, name="rush"),
    path("login/", views.login, name="login"),
    path("house/", views.house, name="house"),
]
