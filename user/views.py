# Imports
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from user import database
from user.forms import *



# All Views
def index(request):
    return render(request, "user/index.html")


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            if database.logged_in(email,password):
                return HttpResponseRedirect(reverse("user:tasks"))
        else:
             return render(request, "user/login.html", {
                "form": form
            })

    return render(request, "user/login.html", {
        "form": LoginForm()
    })


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse("user:login"))
        else:
            return render(request, "user/signup.html", {
                "form": form
            })

    return render(request, "user/signup.html", {
        "form": SignUpForm()
    })


def tasks(request):
    return render(request, "user/tasks.html", {
        "tasks": database.advanced_task_list()
    })


def add(request):
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task_name = form.cleaned_data["task"]
            priority = form.cleaned_data["priority"]  
            database.add_new_task(priority, task_name)          
            return HttpResponseRedirect(reverse("user:tasks"))
        else:
            return render(request, "user/add.html", {
                "form": form
            })

    return render(request, "user/add.html", {
        "form": AddTaskForm()
    })


def delete(request):
    if request.method == "POST":
        form = DeleteTaskForm(request.POST)
        if form.is_valid():
            task_name = form.cleaned_data["task"]
            database.delete_task(task_name)
            return HttpResponseRedirect(reverse("user:tasks"))
        else:
            return render(request, "user/delete.html", {
                "form": form
            })

    return render(request, "user/delete.html", {
        "form": DeleteTaskForm()
    })


def update(request):
    if request.method == "POST":
        form = UpdateTaskForm(request.POST)
        if form.is_valid():
            old_task_name = form.cleaned_data["old_task"]
            new_task_name = form.cleaned_data["new_task"]
            new_priority = form.cleaned_data["new_priority"]
            database.update_task(old_task_name, new_task_name, new_priority)
            return HttpResponseRedirect(reverse("user:tasks"))
        else:
            return render(request, "user/update.html", {
                "form": form
            })

    return render(request, "user/update.html", {
        "form": UpdateTaskForm()
    })
