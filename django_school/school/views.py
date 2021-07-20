from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import StudentSerializer, TeacherSerializer
from .models import Teacher, Student

# Create your views here.

#######################################################################
### Student Views
#######################################################################
class CreateStudentAPIView(CreateAPIView):
  """ This endpoint can be accessed to create a new student in the DB """
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class ListStudentAPIView(ListAPIView):
  """ This endpoint can be accessed to list the students in the DB """
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class UpdateStudentAPIView(UpdateAPIView):
  """ This endpoint can be accessed to update a student's information in the DB """
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class DeleteStudentAPIView(DestroyAPIView):
  """ This endpoint can be accessed to delete a student from the DB """
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

#######################################################################
### Teacher Views
#######################################################################
class CreateTeacherAPIView(CreateAPIView):
  """ This endpoint can be accessed to create a new teacher in the DB """
  queryset = Teacher.objects.all()
  serializer_class = TeacherSerializer

class ListTeacherAPIView(ListAPIView):
  """ This endpoint can be accessed to list the teachers in the DB """
  queryset = Teacher.objects.all()
  serializer_class = TeacherSerializer

class UpdateTeacherAPIView(UpdateAPIView):
  """ This endpoint can be accessed to update a teacher's information in the DB """
  queryset = Student.objects.all()
  serializer_class = TeacherSerializer

class DeleteTeacherAPIView(DestroyAPIView):
  """ This endpoint can be accessed to delete a teacher from the DB """
  queryset = Teacher.objects.all()
  serializer_class = TeacherSerializer