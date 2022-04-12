from django.urls import path
from registerapp import views

app_name="register"
urlpatterns = [
    path('',views.indexfunction,name="register"),
    path('pages/',views.pagefunction,name="pages"),
    path('loginuser',views.loginfunction,name="loginuser"),
    path('registeruser',views.registeruserfunction,name="registeruser"),
    path('viewusers', views.viewusers,name="viewusers"),
    path('adduser/', views.adduser,name="adduser"),
    path('checklogin/',views.checkloginfunction,name="checklogin"),

    #path('sendemail/<str:email>',views.sendemail,name="sendemail"),
]