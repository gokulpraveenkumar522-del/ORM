from django.db import models
from django.contrib import admin
class Student(models.Model):
    Ref_No=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=10)
    DoJ=models.DateField()
    Email=models.EmailField()
    Address=models.TextField()
    Percentage=models.FloatField()
class StudentAdmin(admin.ModelAdmin):
    list_display=["Ref_No","Name","DoJ","Email","Address","Percentage"]
