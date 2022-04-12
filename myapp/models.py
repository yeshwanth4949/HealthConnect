from django.db import models

class LifeBank(models.Model):
	hospitalname=models.CharField(max_length=100,blank=False)
	patientnname=models.CharField(max_length=100,blank=False)
	assistname=models.CharField(max_length=100,blank=False)
	requiremets=models.CharField(max_length=100,blank=False)
	username=models.CharField(max_length=100,blank=False)
	mobileno=models.CharField(max_length=100,blank=False)
	address=models.TextField(max_length=255,blank=False)
	status=models.CharField(max_length=100,blank=False,default='Pending')
	fileuploadtime = models.DateTimeField(auto_now_add=True)
	class Meta:
		db_table ="lifebank_table"

class Medication(models.Model):
	hospitalname=models.CharField(max_length=100,blank=False)
	patientname=models.CharField(max_length=100,blank=False,default='Sai')
	medicationname=models.CharField(max_length=100,blank=False)
	startdate=models.CharField(max_length=100,blank=False)
	enddate=models.CharField(max_length=100,blank=False)
	attachment=models.FileField()
	description=models.TextField(max_length=255,blank=False)
	disease=models.TextField(max_length=255,blank=False,default='Fever')
	username=models.CharField(max_length=100,blank=False)
	category_choices = (('Prescription','Prescription'),('Diagonisis Reports','Diagonisis Reports'),('Others','Others'))
	file_category=models.CharField(max_length=50,choices=category_choices,blank=False)
	type_choices = (('Major','Major'),('Minor','Minor'))
	type_category=models.CharField(max_length=50,choices=type_choices,blank=False,default='Minor')
	fileuploadtime = models.DateTimeField(auto_now_add=True)
	class Meta:
		db_table ="medication_table"


class User(models.Model):
	fullname=models.CharField(max_length=100,blank=False)
	email=models.EmailField(max_length=100,blank=False)
	username=models.CharField(max_length=100,blank=False)
	password=models.CharField(max_length=100,blank=False)
	mobileno=models.CharField(max_length=100,blank=False)
	location=models.CharField(max_length=100,blank=False)
	class Meta:
		db_table = "user_table"

class Doctor(models.Model):
	firstname=models.CharField(max_length=100,blank=False)
	lastname=models.CharField(max_length=100,blank=False)
	password=models.CharField(max_length=100,blank=False)
	cpassword=models.CharField(max_length=100,blank=False)
	gender_choices=(('Male','Male'),('Female','Female'))
	gender=models.CharField(max_length=100,blank=False,choices=gender_choices)
	email=models.EmailField(max_length=100,blank=False)
	mobileno=models.CharField(max_length=100,blank=False)
	specialization_choices=(('General Surgeon','General Surgeon'),('Orthopedics','Orthopedics'),('Neurology','Neurology'))
	specialization=models.CharField(max_length=100,blank=False,choices=specialization_choices)
	username=models.CharField(max_length=100,blank=False,unique=True)
	status=models.CharField(max_length=100,blank=False,default='NotAccepted')
	class Meta:
		db_table = "doctor_table"

class Appointment(models.Model):
	username = models.CharField(max_length=100,blank=False,default='chandu2811')
	name=models.CharField(max_length=100,blank=False)
	email=models.EmailField(max_length=100,blank=False)
	pdate=models.CharField(max_length=100,blank=False)
	ptime_choices=(('8:00 to 9:00','8:00 to 9:00'),('9:00 to 10:00','9:00 to 10:00'),('10:00 to 1:00','10:00 to 1:00'))
	ptime=models.CharField(max_length=100,blank=False,choices=ptime_choices)
	specialization_choices=(('General Surgeon','General Surgeon'),('Orthopedics','Orthopedics'),('Neurology','Neurology'))
	specialization=models.CharField(max_length=100,blank=False,choices=specialization_choices)
	status=models.CharField(max_length=100,blank=False,default='NotAccepted')
	docuname=models.CharField(max_length=100,blank=False,default=' ')
	class Meta:
		db_table = "appointment_table"