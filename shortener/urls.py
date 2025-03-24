from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.add_url, name="add_url"),
    path("<str:path>/", views.r_redirect, name="r_redirect"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", LogoutView.as_view(next_page="/"), name="logout"),
]
