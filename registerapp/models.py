from django.db import models

# Create your models here.
#this can be used for both table and form
class UserLogin(models.Model):
	username=models.CharField(max_length=100,blank=False)
	password=models.CharField(max_length=100,blank=False)
	class Meta:
		db_table = "userlogin_table"

class UsersRegistration(models.Model):
	FirstName=models.CharField(max_length=100,blank=False)
	LastName=models.CharField(max_length=100,blank=False)
	Birthday=models.CharField(max_length=100,blank=False)
	gender_choices=(('Male','Male'),('Female','Female'))
	gender=models.CharField(max_length=100,blank=False,choices=gender_choices)
	email=models.EmailField(max_length=100,blank=False)
	password=models.CharField(max_length=100,blank=False,default='KLU123')
	mobileno=models.CharField(max_length=100,blank=False)
	username=models.CharField(max_length=100,blank=False,unique=True)
	state_choices=(('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),('Arunachal Pradesh','Arunachal Pradesh'),('Assam','Assam'),('Bihar','Bihar'),('Delhi','Delhi'),('Telangana','Telangana'),('Tamil Nadu','Tamil Nadu'),('Uttar Pradesh','Uttar Pradesh'),('Uttarakhand','Uttarakhand'))
	state=models.CharField(max_length=100,blank=False,choices=state_choices)
	class Meta:
		db_table = "usersregistrations_table"