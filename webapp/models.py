from typing import Optional
from django.db import models
from django.contrib.auth.models import User


class Employe(models.Model):
    empid = models.CharField(max_length=6)
    empname = models.CharField(max_length=200)
    empskills = models.CharField(max_length=120,)

    def __str__(self):
        return self.empname


class Assignments(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Assigned', 'Assigned'),
        ('Issuess', 'Issuess'),
        ('raised', 'raised'),
        ('submitted', 'submitted'),
    )
    
    assign_id = models.CharField(max_length=100)
    name_of_title = models.CharField(max_length=50)
    date_of_call_to_people      = models.DateField(auto_now_add=False,null=True)
    date_of_assigning_task = models.DateField(auto_now_add=False)
    date_of_submistion = models.DateField(auto_now_add=False)  
    call_to_people = models.ManyToManyField(Employe)
    assigned_to = models.CharField(max_length=120, default=None)
    downlode_attachement = models.FileField(upload_to="doc/")
    status = models.CharField(max_length=200,choices=STATUS)
    detail = models.TextField(max_length=120, default=None)

    def __str__(self):
        return self.name_of_title
