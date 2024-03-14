from django.urls import path
from . import views
from .views import TeacherListView,TeacherDetailView

urlpatterns = [
path('student-list/', views.student_list, name='student_list'),
path('teacher-list/', TeacherListView.as_view(), name='teacher_list'),
path('student/<int:pk>/', views.student_detail, name='student_detail'),
path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
]