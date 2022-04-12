from django import forms
from .models import User,Doctor,Appointment,Medication,LifeBank


class RegistrationForm(forms.ModelForm):
	class Meta:
		model = User
		fields= "__all__"

class DoctorForm(forms.ModelForm):
	class Meta:
		model = Doctor
		fields= "__all__"

class AppointmentForm(forms.ModelForm):
	class Meta:
		model = Appointment
		fields= "__all__"

class MedicationForm(forms.ModelForm):
	class Meta:
		model = Medication
		fields= "__all__"

class LifeBankForm(forms.ModelForm):
	class Meta:
		model = LifeBank
		fields= "__all__"