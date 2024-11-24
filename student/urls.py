# urls.py
from django.urls import path
from .views import search_student

urlpatterns = [
    # Your other URL patterns
    path('search/', search_student, name='student_search'),
]
