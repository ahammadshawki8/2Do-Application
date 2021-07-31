from django import forms
from django.core import validators
from user.models import *


# def check_for_z(value):
#     if value[0].lower() != "z":
#         raise forms.ValidationError("needs to start with z")


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email Address ") # , validators=[check_for_z])
    password = forms.CharField(label="Password ", widget=forms.PasswordInput)
    # botcatcher = forms.Charfield(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcatcher_text = self.cleaned_data["botcatcher"]
    #     if len(botcatcher_text) > 0:
    #         raise forms.ValidationError("Only humans are allowed!")
    #     return botcatcher_text

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data["email"]
        if len(email) > 32:
            raise forms.ValidationError("Invalid Email")



class SignUpForm(forms.ModelForm):
    password = forms.CharField(label="Password ", widget=forms.PasswordInput)
    
    class Meta:
        model = Person
        fields = ("name", "email", "password")



class AddTaskForm(forms.Form):
    task = forms.CharField(label="Task Name ")
    priority = forms.IntegerField(label="Priority ", min_value=0, max_value=10)



class DeleteTaskForm(forms.Form):
    task = forms.CharField(label="Task Name ")



class UpdateTaskForm(forms.Form):
    old_task = forms.CharField(label="Old Task Name ")
    new_task = forms.CharField(label="New Task Name ")
    new_priority = forms.IntegerField(label="Priority ", min_value=0, max_value=10)
