from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)
from .serializers import StudentSerializer, TeacherSerializer, CourseSerializer
from .models import Teacher, Student, Course

# Create your views here.

#######################################################################
### Student Views
#######################################################################
class CreateCourseAPIView(CreateAPIView):
    """
    This endpoint can be accessed to create a new course in the DB
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ListActiveCoursesAPIView(ListAPIView):
    """
    This endpoint returns a list of active courses
    """

    serializer_class = CourseSerializer

    def get_queryset(self):
        """
        The queryset is only active courses
        """
        return Course.objects.filter(is_active=True)


class DeleteCourseAPIView(DestroyAPIView):
    """
    To delete a course (deactivate it)
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class GetActiveStudentCourses(ListAPIView):
    """
    Retrieves all active courses of a student
    """

    serializer_class = CourseSerializer

    def get_queryset(self):
        student_id = self.kwargs["pk"]
        return Course.objects.filter(students__id=student_id)


class GetTeacherAPIView(RetrieveAPIView):
    """
    Retreives a single teacher's information
    """

    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
