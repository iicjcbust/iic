from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name="home"),
    path('iicStudent',views.iicStudent,name="iicStudent"),
    path('iicFaculty',views.iicFaculty,name="iicFaculty"),
    path('ExternalExperts',views.ExternalExperts,name="ExternalExperts"),
    path('incubationCell',views.incubationCell,name="incubationCell"),
    path('innovationCell',views.innovationCell,name="innovationCell"),
    path('upcomingEvents',views.upcomingEvents,name="upcomingEvents"),
    path('previousEvents',views.previousEvents,name="previousEvents"),
    path('eventDesc/<str:slug>',views.eventDesc,name="eventDes"),
    path('innovation_ambassador',views.innovationAmbassador,name="innovationAmbassador"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('joinIIC',views.joinIIC,name="joinIIC"),


    
]