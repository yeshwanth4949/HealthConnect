from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .forms import RegistrationForm,DoctorForm,AppointmentForm,MedicationForm,LifeBankForm
from .models import User,Doctor,Appointment,Medication,LifeBank
from django.db.models import Q
from django.core.mail import EmailMessage
from django.conf import settings

def indexfunction(request):
	return render(request,"main.html")

def adminh(request):
	return render(request,"Adminhome/index.html")

def doctorhome(request):
	specialization = request.session['specialization']
	return render(request,"Doctorhome/index.html",{'specialization':specialization})

def userfunction(request):
	return HttpResponse("<h1 align=center>Welcome User, you are in myapp folder</h1>")

def guestfunction(request):
	return HttpResponse("Guest Page")

#app functions

def logindoc(request):
	return render(request,"login/login.html")

def coverpage(request):
	return render(request,"cover.html")

def loginadmin(request):
	return render(request,"login1/login.html")

def registeruser(request):
	return render(request,"register/index.html")

def homeuser(request):
	username = request.session['username'] 
	return render(request,"home/index.html",{'username':username})

def adminhome(request):
	return render(request,"Adminhome/index.html")

def doc(request):
	return render(request,"add_doctor/index.html")

def uploadfile(request):
	if (request.method=="POST" and request.FILES['attachment']):
		hname=request.POST["hname"]
		pname=request.POST["pname"]
		mname=request.POST["mname"]
		startdate=request.POST["startdate"]
		enddate=request.POST["enddate"]
		username=request.POST["username"]
		attachment=request.FILES["attachment"]
		desc=request.POST["desc"]
		disease=request.POST["disease"]
		filecat=request.POST["filecat"]
		type_category=request.POST["type_category"]
		flag=Medication.objects.create(hospitalname=hname,patientname=pname,medicationname=mname,startdate=startdate,enddate=enddate,username=username,attachment=attachment,description=desc,disease=disease,file_category=filecat,type_category=type_category)
		if flag:
			return redirect("/homeuser")
		else:
			return HttpResponse("Not Inserted")
	else:
		return HttpResponse("error")

def addlifebank(request):
	if (request.method=="POST"):
		hname=request.POST["hname"]
		pname=request.POST["pname"]
		aname=request.POST["aname"]
		req=request.POST["req"]
		username=request.POST["username"]
		mobileno=request.POST["mobileno"]
		address=request.POST["address"]
		flag=LifeBank.objects.create(hospitalname=hname,patientnname=pname,assistname=aname,requiremets=req,username=username,mobileno=mobileno,address=address)
		if flag:
			return redirect("/homeuser")
		else:
			return HttpResponse("Not Inserted")
	else:
		return HttpResponse("error")


def adddoc(request):
	if request.method=='POST':
		firstname=request.POST["firstname"]
		lastname=request.POST["lastname"]
		password=request.POST["password"]
		cpassword=request.POST["cpassword"]
		gender=request.POST["gender"]
		email=request.POST["email"]
		mobileno=request.POST["mobileno"]
		specialization=request.POST["specialization"]
		username=request.POST["username"]
		print(firstname,lastname,email)
		flag=Doctor.objects.create(firstname=firstname,lastname=lastname,password=password,cpassword=cpassword,gender=gender,email=email,mobileno=mobileno,specialization=specialization,username=username)
		if flag:
			subject="Thank You for your interest towards Health-Connect"
			emails=email
			emails=EmailMessage(subject,"You will shortly receive a response from Health-Connect Team",to=[emails])
			emails.send()
			return render(request,'login/login.html')
	else:
		return HttpResponse("Doctor Not Added !")
	return HttpResponse("Invalid Details!")

def addrequest(request):
	if request.method=='POST':
		username = request.session['username'] 
		name=request.POST["name"]
		email=request.POST["email"]
		pdate=request.POST["pdate"]
		ptime=request.POST["ptime"]
		specialization=request.POST["specialization"]
		print(name,email,pdate,ptime)
		flag=Appointment.objects.create(name=name,email=email,pdate=pdate,ptime=ptime,specialization=specialization,username=username)
		if flag:
			return redirect('/homeuser')
	else:
		return HttpResponse("Request is not Sent !")
	return HttpResponse("Request Failed!")



def checkdocfunction(request):
	if request.method=="POST":
		username=request.POST["username"]
		password=request.POST["password"]
		flag=Doctor.objects.filter( Q(username__iexact=username) & Q(password__iexact=password) & Q(status="Accepted"))
		if flag:
			Doctors = Doctor.objects.filter(Q(username__iexact=username))
			for e in Doctors:
				request.session['specialization']=e.specialization
				request.session['docuname']=e.username
			return redirect("/doctorhome")
		else:
			return HttpResponse("Invalid Doctor Login")
	else:
		return HttpResponse("Failed Login")

def viewsearch(request):
	if request.method=="POST":
		search=request.POST["search"]
		specialization = request.session['specialization'] 
		docuname = request.session['docuname']
		if search!='':
			Appointments=Appointment.objects.filter(Q(status='NotAccepted') & Q(specialization=specialization) & (Q(email=search) | Q(name=search) | Q(pdate=search) | Q(ptime=search))) 
		else:
			Appointments=Appointment.objects.filter(Q(status='NotAccepted') & Q(specialization=specialization))
		return render(request,'viewrequests.html',{'Appointments':Appointments,'search':search})

def viewrequests(request):
	specialization = request.session['specialization'] 
	docuname = request.session['docuname']
	Appointments=Appointment.objects.filter(Q(status='NotAccepted') & Q(specialization=specialization)) 
	return render(request,'viewrequests.html',{'Appointments':Appointments})

def viewsearchappoit(request):
	if request.method=="POST":
		search=request.POST["search"]
		specialization = request.session['specialization'] 
		docuname = request.session['docuname']
		if search!='':
			Appointments=Appointment.objects.filter(Q(status='Accepted') & Q(specialization=specialization) & (Q(email=search) | Q(name=search) | Q(pdate=search) | Q(ptime=search))) 
		else:
			Appointments=Appointment.objects.filter(Q(status='Accepted') & Q(specialization=specialization))
		return render(request,'viewappoit.html',{'Appointments':Appointments,'search':search})

def viewappoit(request):
	specialization = request.session['specialization'] 
	docuname = request.session['docuname']
	Appointments=Appointment.objects.filter(Q(status='Accepted') & Q(specialization=specialization) & Q(docuname=docuname)) 
	return render(request,'viewappoit.html',{'Appointments':Appointments})

def myneeds(request):
	username = request.session['username']
	LifeBanks=LifeBank.objects.filter(Q(username=username))
	return render(request,'home/myneeds.html',{'LifeBanks':LifeBanks})

def allneeds(request):
	LifeBanks=LifeBank.objects.filter(Q(status='Pending'))
	return render(request,'home/viewallneeds.html',{'LifeBanks':LifeBanks})

def removemyneeds(request,id):
	LifeBank.objects.filter(id=id).delete()
	LifeBanks=LifeBank.objects.all()
	return render(request,'home/myneeds.html',{'LifeBanks':LifeBanks})

def viewmedication(request):
	username = request.session['username']
	Medications=Medication.objects.filter(Q(username=username))
	return render(request,'home/viewmedication.html',{'Medications':Medications})

def patientrecords(request,username,name,email):
	request.session['name'] = name
	request.session['email'] = email
	request.session['username'] = username
	Medications=Medication.objects.filter(Q(username=username) & Q(patientname=name))
	return render(request,'Doctorhome/patientrecords.html',{'Medications':Medications,'name':name,'email':email})

def viewsearchpatientrecords(request):
	if request.method=="POST":
		search=request.POST["search"]
		name = request.session['name']
		email = request.session['email']
		username = request.session['username']
		if search=='':
			Medications=Medication.objects.filter(Q(username=username) & Q(patientname=name)) 
		else:
			Medications=Medication.objects.filter(Q(username=username) & Q(patientname=name) & (Q(hospitalname=search) | Q(medicationname=search) | Q(username=search) | Q(disease=search) | Q(type_category=search)))
		return render(request,'Doctorhome/patientrecords.html',{'Medications':Medications,'name':name,'email':email,'search':search})

def viewuserappoit(request):
	username = request.session['username'] 
	Appointments=Appointment.objects.filter(Q(username=username)) 
	return render(request,'home/viewuserappoit.html',{'Appointments':Appointments})
	
def addmedication(request):
	return render(request,'home/addmedication.html')

def requestneed(request):
	return render(request,'home/requestneed.html')

def deletedoc(request,name):
	#User.objects.filter(id=id)#select * from user_table where id=id;
	Appointment.objects.filter(name=name).delete()
	Appointments=Appointment.objects.all()
	return render(request,"viewrequests.html",{'Appointments':Appointments})

def requestsdoc(request):
	Doctors=Doctor.objects.filter(Q(status='NotAccepted')) 
	return render(request,'requestsdoc.html',{'Doctors':Doctors})

def viewdoctors(request):
	Doctors=Doctor.objects.filter(Q(status='Accepted')) 
	return render(request,'viewdoctors.html',{'Doctors':Doctors})

def acceptdoc(request,name):
	#User.objects.filter(id=id)#select * from user_table where id=id;
	docuname = request.session['docuname']
	Appointment.objects.filter(name=name).update(status='Accepted')
	Appointment.objects.filter(name=name).update(docuname=docuname)
	return redirect("/viewrequests")

def deleteadmin(request,username):
	Doctor.objects.filter(username=username).delete()
	Doctors=Doctor.objects.filter(Q(status='NotAccepted'))
	return redirect('/requestsdoc')

def acceptadmin(request,username,email):
	Doctor.objects.filter(username=username).update(status='Accepted')
	Doctors=Doctor.objects.filter(Q(status='NotAccepted'))
	subject="Successful Registration"
	emails=email
	emails=EmailMessage(subject,"Welcome to Health Connect, otp = 2455",to=[emails])
	emails.send()
	return redirect('/requestsdoc')

def registrationuser(request):
	if request.method=="POST":
		uname=request.POST['uname']
		pwd=request.POST['pwd']
		print(uname,pwd)
		if uname=='admin' and pwd=='pwd':
			return redirect('loginuser')
		else:
			return redirect('registeruser')
	else:
		return redirect('registeruser')

def checkadmin(request):
	if request.method=="POST":
		uname=request.POST['username']
		pwd=request.POST['password']
		print(uname,pwd)
		if uname=='admin' and pwd=='admin':
			return redirect('/adminh')
		else:
			return redirect('registeruser')
	else:
		return redirect('registeruser')




import numpy as np
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sb
from io import BytesIO




def graphs(request):
    es = pd.DataFrame(Doctor.objects.all().values())
    ca = pd.DataFrame(User.objects.all().values())
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(12, 5))
    font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
    font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}
    title = 'Health-Connect'
    plt.title(title,fontdict=font1)
    if request.GET.get('esl'):
        plt.plot(es['specialization'], es['gender'],marker='*')
        plt.xlabel("specialization",fontdict=font2)
        plt.ylabel("gender",fontdict=font2)
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        graph = base64.b64encode(image_png)
        graph = graph.decode('utf-8')
        buffer.close()
    elif request.GET.get('ess'):
        plt.scatter(es['specialization'], es['gender'])
        plt.xlabel("specialization",fontdict=font2)
        plt.ylabel("gender",fontdict=font2)
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        graph = base64.b64encode(image_png)
        graph = graph.decode('utf-8')
        buffer.close()
    elif request.GET.get('esp'):
        plt.pie(es['gender'],labels=es['specialization'])
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        graph = base64.b64encode(image_png)
        graph = graph.decode('utf-8')
        buffer.close()
    else:
        plt.bar(es['specialization'], es['gender'])
        plt.xlabel("specialization",fontdict=font2)
        plt.ylabel("gender",fontdict=font2)
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        graph = base64.b64encode(image_png)
        graph = graph.decode('utf-8')
        buffer.close()
    context={
        'graph':graph
    }
    return render(request, 'graph.html',context)