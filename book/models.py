from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Notification(models.Model):
    message = models.TextField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)




