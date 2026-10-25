from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_fake, name="login"),
    path("logout/", views.logout_fake, name="logout"),
    path("panel/", views.panel_general, name="panel"),
]