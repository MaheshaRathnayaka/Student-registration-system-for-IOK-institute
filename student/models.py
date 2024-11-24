from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Class(models.Model):
    class_name = models.CharField(max_length=100)
    class_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.class_name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='class_id')
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.student} enrolled in {self.enrolled_class}"

class AcademicRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='class_id')
    grade = models.CharField(max_length=2)
    remarks = models.TextField()
    attendance_percentage = models.FloatField(default=0.0)
    participation_score = models.IntegerField(default=0)
    assignment_score = models.IntegerField(default=0)
    exam_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.student}'s record for {self.enrolled_class}"
class ClassSession(models.Model):
    enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    session_date = models.DateField()
    topic = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.enrolled_class.class_name} - {self.session_date}"
