
from django.shortcuts import render,get_object_or_404
from .models import Student
from django.views.generic import ListView,DetailView
from .models import Teacher

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher_list.html'
    context_object_name = 'teachers'

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_detail.html', {'student': student})

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher_detail.html'
    context_object_name = 'teacher'

