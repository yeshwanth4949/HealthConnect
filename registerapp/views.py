from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import UsersRegistration
from django.db.models import Q

from django.core.mail import EmailMessage
from django.conf import settings

def indexfunction(request):
	return HttpResponse("Demo Project")

def pagefunction(request):
	return HttpResponse("Register app")

def registeruserfunction(request):
	return render(request,"register.html")

def loginfunction(request):
	return render(request,'login.html')

def adduser(request):
	if request.method=='POST':
		FirstName=request.POST["FirstName"]
		LastName=request.POST["LastName"]
		Birthday=request.POST["Birthday"]
		gender=request.POST["gender"]
		email=request.POST["email"]
		gender=request.POST["gender"]
		password=request.POST["password"]
		mobileno=request.POST["mobileno"]
		username=request.POST["username"]
		state=request.POST["state"]
		print(FirstName,LastName,Birthday)
		flag=UsersRegistration.objects.create(FirstName=FirstName,LastName=LastName,Birthday=Birthday,gender=gender,email=email,password=password,mobileno=mobileno,username=username,state=state)
		if flag:
			subject="Successful Registration"
			emails=email
			emails=EmailMessage(subject,"Welcome to Health Connect, otp = 2455",to=[emails])
			emails.send()
			return render(request,"login.html")
	else:
		return HttpResponse("Student Not Added !")
	return render(request,'adduser.html',{'form':form})

def viewusers(request):
	UsersRegistrations=UsersRegistration.objects.all() # select * from student_table;
	count=UsersRegistration.objects.all().count() # select count(*) from student_table;
	return render(request,'viewusers.html',{'UsersRegistrations':UsersRegistrations,'count':count})


def checkloginfunction(request):
	if request.method=="POST":
		username=request.POST["username"]
		password=request.POST["password"]
		flag=UsersRegistration.objects.filter( Q(username__iexact=username) & Q(password__iexact=password) )
		if flag:
			request.session['username'] = username
			return redirect("/homeuser")
		else:
			return HttpResponse("Invalid Login")
	else:
		return render(request,"pages")


