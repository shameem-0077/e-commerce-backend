from django.db import models


class Customer(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
