from django.db import models
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Receipt(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    receipt_number = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.receipt_number = timezone.now().strftime('%Y-%m-%d-%H%M%S')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.receipt_number