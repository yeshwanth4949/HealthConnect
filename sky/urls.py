"""sky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.contrib.auth.models import User

class OTPAdmin(OTPAdminSite):
    pass

admin_site=OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo',views.demofunction,name="demo"),
    path('demo1',views.demofunction1,name="demo1"),
    path('main/',views.mainpage,name="main"),

    path('users1',views.usersfunction11,name="users1"),
    path('base/',views.basefunction,name="base"),
    
    path('dadmin/',admin.site.urls),
    #qwer
    path('',include('myapp.urls')),
    path('',include('registerapp.urls')),
]
