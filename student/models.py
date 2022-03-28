from re import M
from statistics import mode
from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(default='abc@gmail.com')
    address = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    email = models.EmailField()
    school = models.ForeignKey(School, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return "{} -> {}".format(self.name, self.address)


