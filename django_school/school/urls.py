from django.urls import path
from . import views

urlpatterns = [
    path("course/", views.CreateCourseAPIView.as_view(), name="create_course"),
    path(
        "course/", views.ListActiveCoursesAPIView.as_view(), name="list_active_courses"
    ),
    path(
        "course/<int:pk>/",
        views.DeleteCourseAPIView.as_view(),
        name="delete_course",
    ),
    path(
        "student/<int:pk>/course",
        views.GetActiveStudentCourses.as_view(),
        name="get_student_courses",
    ),
    path("teacher/<int:pk>", views.GetTeacherAPIView.as_view(), name="get_teacher"),
]
