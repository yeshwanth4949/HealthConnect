from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def demofunction(request):
	return HttpResponse("Demo Project")

def mainpage(request):
	return render(request,"project.html")

def demofunction1(request):	
	empdict={"id":30324,"name":"Yeshwanth"}
	return JsonResponse(empdict)

def usersfunction11(request):
	return render(request,"display.html")

def basefunction(request):
	return render(request,"base.html")