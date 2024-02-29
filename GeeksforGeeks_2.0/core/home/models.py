from django.db import models
from django.contrib.auth.models import User

#Create mode for receipt
class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True),
 

# ============== CGPA Calcualtor Model ===================
class Subject(models.Model):
    name = models.CharField(max_length=255)
    grade = models.CharField(max_length=2, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')])
    credit = models.PositiveIntegerField()
 
    def __str__(self):
        return f"{self.name} - Grade: {self.grade}, Credit: {self.credit}"