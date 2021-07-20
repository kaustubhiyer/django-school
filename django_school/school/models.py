from django.db import models

# Create your models here.

class Teacher(models.Model):
  name = models.CharField(max_length=50)
  gender = models.CharField(max_length=1)
  email = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Student(models.Model):
  name = models.CharField(max_length=50)
  gender = models.CharField(max_length=1)
  grade = models.CharField(max_length=2)

  def __str__(self):
    return self.name