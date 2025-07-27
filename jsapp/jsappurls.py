from django.urls import path
from . import views

urlpatterns=[
    path('jsapp/',views.jshome,name='jshome'),
    path('viewjobs/',views.viewjobs,name='viewjobs'),
    path('logout/',views.logout,name='logout'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('jsapply/<id>',views.jsapply,name='jsapply'),
    path('appliedjobs/',views.appliedjobs,name='appliedjobs'),
    path('viewprofile/',views.viewprofile,name='viewprofile'),
    path('response/',views.response,name='response'),
    path('search/', views.job_search, name='job_search')
    ]