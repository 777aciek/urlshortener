from django.urls import path
from . import views

urlpatterns = [
    path("", views.add_url, name="add_url"),
    path("<str:path>/", views.r_redirect, name="r_redirect"),
]
