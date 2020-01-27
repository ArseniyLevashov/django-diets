from django.db import models


class Diet(models.Model):
    """"""

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    start_date = models.DateField()
    start_weight = models.FloatField()


class Result(models.Model):
    """"""

    diet_id = models.IntegerField()
    current_date = models.DateField()
    current_weight = models.FloatField()
