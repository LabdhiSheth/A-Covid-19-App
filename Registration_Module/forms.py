from django import forms
from django.db.models import fields
from .models import *
from django.forms import ModelForm
from django.utils.safestring import mark_safe

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser



class NewUserForm(UserCreationForm):

	class Meta:
		model = CustomUser
		fields = ("email", "first_name","last_name","password1", "password2")
    

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user


class HospitalUserForm(UserCreationForm):
    
    class Meta:
	    model = CustomUser
	    fields = ("email", "first_name","last_name","password1", "password2","is_hospital_staff", 'hospital')

    # def save(self, commit=True):
	#     user = super(NewUserForm, self).save(commit=False)
	#     if commit:
	# 	    user.save()
	#     return user