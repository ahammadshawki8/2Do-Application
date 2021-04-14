# Imports
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from . import database




# Prerequisites
class LoginForm(forms.Form):
    email = forms.EmailField(label="Email Address ")
    password = forms.CharField(label="Password ", widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    name = forms.CharField(label="Fullname ")
    email = forms.EmailField(label="Email Address ")
    password = forms.CharField(label="Password ", widget=forms.PasswordInput)


class AddTaskForm(forms.Form):
    task = forms.CharField(label="Task Name ")
    priority = forms.IntegerField(label="Priority ", min_value=0, max_value=10)


class DeleteTaskForm(forms.Form):
    task = forms.CharField(label="Task Name ")


class UpdateTaskForm(forms.Form):
    old_task = forms.CharField(label="Old Task Name ")
    new_task = forms.CharField(label="New Task Name ")
    new_priority = forms.IntegerField(label="Priority ", min_value=0, max_value=10)




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
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            database.signed_up(name, email, password)
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
