from django.db import models

class Deposit(models.Model):
    job = models.CharField(max_length=50)
    marital = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    default = models.CharField(max_length=50)
    housing = models.CharField(max_length=50)
    loan = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    month = models.CharField(max_length=50)
    day_of_week = models.CharField(max_length=50)
    duration = models.IntegerField()
    campaign = models.IntegerField()
    pdays = models.IntegerField()
    previous = models.IntegerField()
    poutcome = models.CharField(max_length=50)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
