from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    priority = models.IntegerField()

    def __str__(self):
        return f"{self.id}. {self.name} ({self.priority})"



class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    tasks = models.ManyToManyField(Task, blank=True, related_name="tasks")

    def __str__(self):
        return self.name
    
