from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from .views import graphs

app_name="user"
urlpatterns = [
    path('',views.indexfunction,name="indexs"),
    path('graphs/',graphs,name="graph"),
    path('user',views.userfunction,name="user"),
    path('guest',views.guestfunction,name="guest"),
    path('adminh',views.adminh,name="adminhs"),
    path('doctorhome',views.doctorhome,name="doctorhome"),
    path('viewappoit',views.viewappoit,name="viewappoit"),
    path('viewsearch',views.viewsearch,name="viewsearch"),
    path('viewsearchappoit',views.viewsearchappoit,name="viewsearchappoit"),
    path('coverpage',views.coverpage,name="coverpage"),
    #app urls

    path('viewsearchpatientrecords',views.viewsearchpatientrecords,name="viewsearchpatientrecords"),
    path('patientrecords/<str:username>,<str:name>,<str:email>',views.patientrecords,name="patientrecords"),
    path('logindoc',views.logindoc,name="logindoc"),

    path('loginadmin',views.loginadmin,name="loginadmin"),

    #path('registeruser/',views.registeruser,name="registeruser"),
    path('homeuser',views.homeuser,name="homeruser"),
    path('adminhome',views.adminhome,name="adminhome"),

    path('viewuserappoit',views.viewuserappoit,name="viewuserappoit"),
    path('addmedication',views.addmedication,name="addmedication"),
    path("uploadfile",views.uploadfile,name="uploadfile"),
    path('viewmedication',views.viewmedication,name="viewmedication"),
    path('requestneed',views.requestneed,name="requestneed"),
    path('addlifebank',views.addlifebank,name="addlifebank"),
    path('myneeds',views.myneeds,name="myneeds"),
    path('allneeds',views.allneeds,name="allneeds"),
    path('removemyneeds/<str:id>',views.removemyneeds,name="removemyneeds"),

    path('registerdoc',views.doc,name="registerdoc"),
    path('adddoc', views.adddoc,name="adddoc"),
    path('checkdoc/',views.checkdocfunction,name="checkdoc"),


    path('viewrequests', views.viewrequests,name="viewrequests"),
    path('requestsdoc', views.requestsdoc,name="requestsdoc"),
    path('viewdoctors', views.viewdoctors,name="viewdoctors"),


    path('deletedoc/<str:name>',views.deletedoc,name="deletedoc"),
    path('acceptdoc/<str:name>',views.acceptdoc,name="acceptdoc"),

    path('deleteadmin/<str:username>',views.deleteadmin,name="deleteadmin"),
    path('acceptadmin/<str:username>,<str:email>',views.acceptadmin,name="acceptadmin"),

    path('addrequest', views.addrequest,name="addrequest"),
    #path('registrationuser/',views.registrationuser,name="registrationuser"),
    path('checkadmin/',views.checkadmin,name="checkadmin"),


    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
