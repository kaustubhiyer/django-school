from django.urls import path
from . import views

urlpatterns = [
    path("course/", views.ListCreateCourseAPIView.as_view(), name="create_list_course"),
    path(
        "course/<int:pk>/",
        views.DeleteCourseAPIView.as_view(),
        name="delete_course",
    ),
    path(
        "student/<int:pk>/course/",
        views.GetActiveStudentCourses.as_view(),
        name="get_student_courses",
    ),
    path("teacher/<int:pk>/", views.GetTeacherAPIView.as_view(), name="get_teacher"),
    path(
        "teacher/create/", views.CreateTeacherAPIView.as_view(), name="create_teacher"
    ),
    path(
        "student/create/", views.CreateStudentAPIView.as_view(), name="create_student"
    ),
]
