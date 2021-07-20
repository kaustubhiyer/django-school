from django.urls import path
from . import views

urlpatterns = [
    path("student/", views.ListStudentAPIView.as_view(), name="student_list"),
    path("student/create/", views.CreateStudentAPIView.as_view(), name="student_create"),
    path("student/update/<int:pk>/", views.UpdateStudentAPIView.as_view(), name="student_update"),
    path("student/delete/<int:pk>/", views.DeleteStudentAPIView.as_view(), name="student_delete"),
    path("teacher/", views.ListTeacherAPIView.as_view(), name="teacher_list"),
    path("teacher/create/", views.CreateTeacherAPIView.as_view(), name="teacher_create"),
    path("teacher/update/<int:pk>/", views.UpdateTeacherAPIView.as_view(), name="teacher_update"),
    path("teacher/delete/<int:pk>/", views.DeleteTeacherAPIView.as_view(), name="teacher_delete"),
]
