from django.db import models

# Create your models here.
class Student(models.Model):
    # Basic Information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    # Contact Information
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    # Academic Information
    student_id = models.CharField(max_length=10, unique=True)
    major = models.CharField(max_length=50)
    enrollment_date = models.DateField()

    # Exam Scores
    math_score = models.DecimalField(max_digits=5, decimal_places=2)
    science_score = models.DecimalField(max_digits=5, decimal_places=2)
    english_score = models.DecimalField(max_digits=5, decimal_places=2)

    # Boolean Field
    is_active = models.BooleanField(default=True)

    # Date and Time Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.student_id}"


class Car(models.Model):
    car_name = models.CharField(max_length=500, default="GMC")
    speed = models.IntegerField(default=50)

    def __str__(self):
        return self.car_name
