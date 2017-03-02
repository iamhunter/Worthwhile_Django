from django.shortcuts import render, HttpResponse, render_to_response, redirect, get_object_or_404

from django.apps import apps

from .models import Course
from .models import Course_index

# Create your views here.

def index(request):
    latest_course_list = Course.objects.all()
    context = {'latest_course_list': latest_course_list}
    return render(request, 'index.html', context)

def add(request):
    if request.method == 'POST':
        form = Course_index(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    else:
        form = Course_index()
        return render(request, 'add.html', {'form': form})
    
def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'detail.html', {'course': course})

def change(request, course_id):
    my_record = Course.objects.get(id=course_id)

    if request.method =='POST':
        form = Course_index(request.POST, request.FILES, instance=my_record)
        if form.is_valid():
            form.save()
            return redirect('index')
            
    else:
        form = Course_index(instance=my_record)
        return render(request, 'add.html', {'form': form})
