# Imports
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse


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

def save_data(name, email, password):
    with open("db_csv.csv", "a") as database:
        database.write(f"{name}, {email}, {password}\n")

def auth_db(email, password):
    with open("db_csv.csv", "r") as database:
        info = database.read()
        info_list = info.split("\n")[:-1]
        for record in info_list:
            db_name, db_email, db_password = record.split(", ")
            if email == db_email and password == db_password:
                return True
        return False


# All Views
def index(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            if auth_db(email, password):
                return HttpResponseRedirect(reverse("user:tasks"))
        else:
             return render(request, "login/index.html", {
                "form": form
            })

    return render(request, "login/index.html", {
        "form": LoginForm()
    })

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            save_data(name, email, password)
            return HttpResponseRedirect(reverse("user:index"))
        else:
            return render(request, "signup/index.html", {
                "form": form
            })

    return render(request, "signup/index.html", {
        "form": SignUpForm()
    })

def tasks(request):
    if not ("tasks" in request.session):
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": [value for key,value in sorted(request.session["tasks"], reverse=True)]
    })

def add(request):
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            priority = form.cleaned_data["priority"]
            request.session["tasks"] += [(priority, task)]
            return HttpResponseRedirect(reverse("user:tasks"))
        else:
            return render(request, "add/index.html", {
                "form": form
            })

    return render(request, "add/index.html", {
        "form": AddTaskForm()
    })

def delete(request):
    if request.method == "POST":
        form = DeleteTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            for db_task in request.session["tasks"]:
                key,value = db_task
                if value == task:
                    request.session["tasks"].remove(db_task)
                    request.session.modified = True
            return HttpResponseRedirect(reverse("user:tasks"))
        else:
            return render(request, "delete/index.html", {
                "form": form
            })

    return render(request, "delete/index.html", {
        "form": DeleteTaskForm()
    })
