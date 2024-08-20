from django.db import models
from django.conf import settings

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email




class DonarInfo(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    address = models.CharField(max_length=255)
    date = models.DateField()
    mobileno = models.CharField(max_length=15)
    email = models.EmailField()
    pincode = models.CharField(max_length=10)
    expiry = models.DateField()

    def __str__(self):
        return self.name

# class Donation(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=100)
#     quantity = models.IntegerField()
#     address = models.CharField(max_length=200)
#     date = models.DateField()
#     mobileno = models.CharField(max_length=10, null=True, blank=True)
#     email = models.EmailField()
#     pincode = models.CharField(max_length=6, null=True, blank=True)
#     expiry = models.DateField()

#     def __str__(self):
#         return f"Donation by {self.name} on {self.date}"