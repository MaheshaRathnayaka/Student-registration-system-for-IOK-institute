from django.contrib import admin
from .models import Student, Class, Enrollment, AcademicRecord, ClassSession

class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1 

class AcademicRecordInline(admin.TabularInline):
    model = AcademicRecord
    extra = 1  

class ClassSessionInline(admin.TabularInline):
    model = ClassSession
    extra = 1  

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'gender', 'email', 'phone_number', 'registration_date')
    search_fields = ('first_name', 'last_name', 'email')
    inlines = [EnrollmentInline, AcademicRecordInline] 

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'class_description', 'start_date', 'end_date', 'capacity')
    search_fields = ('class_name',)
    inlines = [ClassSessionInline]  

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'enrolled_class', 'enrollment_date')
    search_fields = ('student__first_name', 'student__last_name', 'enrolled_class__class_name')
    list_filter = ('enrolled_class', 'enrollment_date')  

@admin.register(AcademicRecord)
class AcademicRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'enrolled_class', 'grade', 'remarks')
    search_fields = ('student__first_name', 'student__last_name', 'enrolled_class__class_name', 'grade')
    list_filter = ('grade', 'enrolled_class')  


@admin.register(ClassSession)
class ClassSessionAdmin(admin.ModelAdmin):
    list_display = ('enrolled_class', 'session_date', 'topic')
    list_filter = ('enrolled_class', 'session_date')
    search_fields = ('enrolled_class__class_name', 'topic')
