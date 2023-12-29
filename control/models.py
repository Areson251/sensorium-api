from django.contrib.auth.models import User
from django.db import models


class Devices(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, default="NoName")
    add_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "devices"


class Equipment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, default="NoName")
    description = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "equipment"


class Indicators(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True)
    indicator_type = models.CharField(max_length=100, default="Gague")
    min_value = models.CharField(max_length=100)
    max_value = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "indicators"


class IndicatorValues(models.Model):
    indicator = models.ForeignKey(Indicators, on_delete=models.SET_NULL, null=True)
    value = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now_add=True)
    image_path = models.CharField(max_length=100, default="NoPath")

    class Meta:
        db_table = "indicator_values"
