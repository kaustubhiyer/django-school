from django.db import models

# Create your models here.




class Course(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    course_id = models.OneToOneField(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    courses = models.ManyToManyField(to=Course, related_name="students")

    def __str__(self):
        return self.name



