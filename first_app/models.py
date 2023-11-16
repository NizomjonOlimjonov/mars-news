from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=500)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title
class User(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=300)
    Phone_number = models.CharField(max_length=16)
    email = models.CharField(max_length=30)
    RegTime = models.DateTimeField(auto_created=True)
    def __str__(self) -> str:
        return self.First_name