import sys
import os
sys.path.append(os.getcwd())
os.environ["DJANGO_SETTINGS_MODULE"] = "todo_app.settings"

import django
django.setup()

from user.models import Person, Task



class Constant:
    EMAIL = None


def logged_in(email, password):
    query_set = Person.objects.all()
    for person in query_set:
        if person.email == email and person.password == password:
            Constant.EMAIL = email
            return True
    return False


def signed_up(name, email, password):
    new_user = Person(name=name, email=email, password=password)
    new_user.save()
    return new_user


def add_new_task(priority, task_name):
    new_task = Task(name=task_name, priority=priority)
    new_task.save()
    person = Person.objects.get(email=Constant.EMAIL)
    person.tasks.add(new_task)
    return new_task


def delete_task(task_name):
    task_list = Task.objects.filter(name=task_name)
    person = Person.objects.get(email=Constant.EMAIL)
    for task in task_list:
        if person in task.tasks.all():
            person.tasks.get(pk = task.id).delete()
            if len(task.tasks.all()) == 0:
                task.delete()
                return task


def advanced_task_list():
    result = []
    person = Person.objects.get(email=Constant.EMAIL)
    task_list = person.tasks.all()
    temp = []   
    for task in task_list:
        temp.append((task.priority, task.name)) 
    for task in sorted(temp, reverse=True):
        result.append(task[1])    
    return result


def update_task(old_task_name, new_task_name, new_task_priority):
    deleted = delete_task(old_task_name)
    added = add_new_task(new_task_priority,new_task_name)
    return [deleted, added]

