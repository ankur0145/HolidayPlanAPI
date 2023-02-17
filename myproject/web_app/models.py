from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    emp_holiday=models.IntegerField(max_length=30)
    emp_holiday_approved=models.IntegerField(max_length=15)
    emp_holiday_pending=models.IntegerField(max_length=10)
    emp_holiday_reject=models.IntegerField(max_length=5)

    def __str__(self):
       return self.first_name