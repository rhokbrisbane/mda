from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
from datetime import datetime

# Create your models here.
class Goal(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='A Goal')
    eval_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

class Milestone(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    name = models.CharField(max_length=200, default='Give me a name')
    low_evaluation = models.CharField(max_length=200, default='A low evaluation')
    high_evaluation = models.CharField(max_length=200, default='A high evaluation')

    def __str__(self):
        return self.name

class Action(models.Model):
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="Here's an action to complete my milestone")

    def __str__(self):
        return self.name
