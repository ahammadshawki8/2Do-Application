from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path("", views.index , name="index"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("tasks", views.tasks, name="tasks"),
    path("add", views.add, name="add"),
    path("delete", views.delete, name="delete"),
    path("update", views.update, name="update")
]