
from pdb import post_mortem
from django.shortcuts import redirect, render
from .models import Student
from .forms import StudentForm

def index(request):
    return render(request, 'fscohort/index.html')


def student_list(request):
    students = Student.objects.all()
    
    context = {
        "students" : students
    }
    
    return render(request, "fscohort/student_list.html", context)

def student_add(request):
    form = StudentForm()
    print(request.POST)
    if  request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("list")
        pass
    
    context = {
        "form" : form
    }
    return render(request, "fscohort/student_add.html", context)