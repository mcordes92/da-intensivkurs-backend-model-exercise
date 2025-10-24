from django.db import models

class Semester(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Professor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class StudentCard(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="card")
    card_number = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return f"Card {self.card_number} for {self.student}"
    
class CourseDescription(models.Model):
    text = models.TextField()

    def __str__(self):
        return f"Course Description {self.text}"
    
class Course(models.Model):
    title = models.CharField(max_length=200)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT, related_name="courses")
    students = models.ManyToManyField(Student, related_name="courses", blank=True)
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT, related_name="courses")
    description = models.OneToOneField(CourseDescription, on_delete=models.CASCADE, related_name="course")

    def __str__(self):
        return f"{self.title} – {self.description.text}"