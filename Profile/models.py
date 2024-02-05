from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Emp(models.Model):
    eid = models.DecimalField(max_digits=10, decimal_places=2)
    ename = models.CharField(max_length=255)
    sal = models.DecimalField(max_digits=10, decimal_places=2)


