from django.shortcuts import render, HttpResponse, render_to_response, redirect

from django.apps import apps

from .models import Course
from .models import Course_index

# Create your views here.

def index(request):
    latest_course_list = Course.objects.all()
    context = {'latest_course_list': latest_course_list}
    return render(request, 'index.html', context)

def add(request):
    if request.method == "POST":
        form = Course_index(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    
    else:
        form = Course_index()
    return render(request, 'add.html', {'form': form})

def change(request, question_id):
    return HttpResponse("You're changing question %s." % question_id)
