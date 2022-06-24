from django.db import models

# Create your models here.

class Vacation(models.Model):
    vac_request = models.CharField(max_length=50)

    def __str__(self):
        return self.vac_request

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile= models.CharField(max_length=15)
    vac_request= models.ForeignKey(Vacation,on_delete=models.CASCADE)