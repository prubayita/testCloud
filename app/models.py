from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  receiptNumber = models.DateTimeField(auto_now_add=True)
  paymentDate = models.DateTimeField(null=True, blank=True)
  totalAmount = models.CharField(max_length=255)
  
  def __str__(self):
    return f"{self.firstname} {self.lastname}"