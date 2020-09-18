from django.shortcuts import render
from .models import StudentProfile
from .forms import StudentForm

def image_view(request):
    if request.method == "POST":
        sform = StudentForm(request.POST,request.FILES)
        if sform.is_valid():
            sform.save()
            return images(request)

    sform = StudentForm()
    return render(request,'image_form.html',{'sform':sform})

def images(request):
    imgs = StudentProfile.objects.all()
    return render(request,'image_display.html',{'imgs':imgs})

def update(request,pk):
    students = StudentProfile.objects.get(id=pk)
    uform = StudentForm(request.POST or None,request.FILES or None,instance=students)
    if uform.is_valid():
        uform.save()
        return images(request)

    return render(request,'image_form.html',{'sform':uform})

def delete(request,pk):
    student = StudentProfile.objects.get(id=pk)
    student.delete()
    return images(request)
