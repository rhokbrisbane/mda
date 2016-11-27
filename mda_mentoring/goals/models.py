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
        return "{} ({})".format(self.name, self.user)

class Milestone(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    name = models.CharField(max_length=200, default='Give me a name')
    low_evaluation = models.CharField(max_length=200, default='A low evaluation')
    high_evaluation = models.CharField(max_length=200, default='A high evaluation')

    def user(self):
        return self.goal.user

    def __str__(self):
        return "{} (goal: {})".format(self.name, self.goal)

class Action(models.Model):
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="Here's an action to complete my milestone")

    def goal(self):
        return self.milestone.goal

    def user(self):
        return self.milestone.user

    def __str__(self):
        return "{} (milestone: {})".format(self.name, self.milestone)
