from django.db import models

class Event(models.Model):

    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20, default='')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    longitude = models.DecimalField(max_digits=9, decimal_places=3)
    latitude = models.DecimalField(max_digits=9, decimal_places=3)
    total_attendees = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
