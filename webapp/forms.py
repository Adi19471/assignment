from django import forms
from django.contrib.admin.helpers import checkbox
from django.db.models import fields

from django.forms.widgets import DateInput, SelectMultiple, TextInput

from .models import Assignments, Employe 

from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm




class AssignmentsForm(forms.ModelForm):
    

    class Meta:
        # call_to_people: forms.RadioSelect(attrs={"class": "form-control",})
        model = Assignments
        fields = "__all__"
        
        

        exclude = {'skill_required'}

      
        labels = {
            "assign_id": "AssignID:",
            "name_of_title": "Name Title of the Assignment:",
            "Date_of_call_mode": "Date of Call to people:",
            
            "date_of_assigning_task":"Date of Assigning Task:",
            "date_of_submistion": "Date of Submission:",
            "skill_required": "Skill required:",
            "call_to_people": "Call to people:",
            "assigned_to": "Assigned to:",

            
            "downlode_attachement": "Download attachment:",
            "status":"Status:",
            "detail":"Detail:",
            
        }


        widgets = {
            "assign_id": forms.TextInput(attrs={"class": "form-control","readonly":"readonly"}),
            
            "name_of_title": forms.TextInput(attrs={"class": "form-control",'rows':1, 'cols': '90','id':'selected-area',}),

            "date_of_call_to_people":forms.DateInput(attrs={"class": "form-control","readonly":"readonly"}),

          

            "date_of_assigning_task":forms.DateInput(attrs={"class": "form-control",'id':'datepickers',"readonly":"readonly"}),


            "date_of_submistion": forms.DateInput(attrs={"class": "form-control",'id':'datepickerss'}),
            
            "call_to_people": forms.CheckboxSelectMultiple(attrs={"class": "form-control",'id':'id_call_to_people'}),

            "assigned_to": forms.TextInput(attrs={"class": "form-control"}),

            "downlode_attachement": forms.FileInput(attrs={"class": "form-control"}),

            
           

            "status": forms.Select(attrs={"class": "form-control"}),

            "detail": forms.Textarea(attrs={"class": "form-control",'rows': '4',
                'cols': '90',}),

             # "skill_required": forms.TextInput(attrs={"class": "form-control"}),
        }

   

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = "__all__"

        labels = {
            "empid":"EMPLOYE ID",
            "empname":"EMPLOYE NAME",
            "empskills":"EMPLOYE SKILLS",


        }

        

        widgets = {
            "empid": forms.TextInput(attrs={"class": "form-control"}),
            
            "empname": forms.TextInput(attrs={"class": "form-control"}),

            "empskills": forms.TextInput(attrs={"class": "form-control"}),

        }


# registration form 

class SignupForm(UserCreationForm):
    password2 = forms.CharField(label='Confoirm Password (again)',widget=forms.PasswordInput)
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email']
        label = {'email':'Email'}