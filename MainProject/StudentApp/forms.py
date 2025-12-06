from .models import Student
from django import forms

class StdntForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ["fname","lname","email","mobile","pfimg"]
		widgets = {
			"fname":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Firstname"}),
			"lname":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Lastname"}),
			"email":forms.EmailInput(attrs={"class":"form-control my-2","placeholder":"Enter Emailid"}),
			"mobile":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Mobile Number","max":10,"min":10}),
		}
