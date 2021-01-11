from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Answer(models.Model):
    title = models.CharField(max_length=255)
    #create_by = models.CharField(max_length=255)
    schoolans = models.CharField(max_length=255)
    foodans = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Correct(models.Model):
    title = models.OneToOneField(Answer, on_delete=models.CASCADE)
    #create_by = models.OneToOneField(Answer, on_delete=models.CASCADE)
    schoolans = models.CharField(max_length=255)
    foodans = models.CharField(max_length=255)

class User(models.Model):
    name = models.CharField(max_length=20)
    answer = models.CharField(default="", max_length=10, null=True, blank=True)

class Challenger(models.Model):
    user_obj = models.ForeignKey("User", on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    result = models.CharField(default="", max_length=10, null=True, blank=True)








