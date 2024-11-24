from django.shortcuts import render
from django.db.models import Q  # Import the Q object here
from .models import Student

def search_student(request):
    query = request.GET.get('q', '')
    students = Student.objects.none()  # Empty QuerySet by default
    if query:
        students = Student.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) | 
            Q(email__icontains=query)
        )
    return render(request, 'students/search.html', {'students': students})
