from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Asset(models.Model):
    code = models.CharField(max_length=10)

    description = models.CharField(max_length=120)

    def __str__(self):
        return self.code


class Cotation(models.Model):
    assetid = models.ForeignKey("Asset", on_delete=models.CASCADE)

    date = models.DateTimeField()

    price = models.FloatField()

    currency = models.CharField(max_length=5)

    change_percent = models.FloatField()

    updated_at = models.DateTimeField()


class Tunnel(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)

    assetid = models.ForeignKey("Asset", on_delete=models.CASCADE)

    cotationid = models.ForeignKey("Cotation", on_delete=models.CASCADE, null=True)

    period = models.TimeField()

    date_updated = models.DateTimeField()

    max_price = models.FloatField()

    min_price = models.FloatField()
