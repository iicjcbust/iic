from django.shortcuts import render,redirect
from . models import Contact,announcement,Events,JoinIIC
import datetime 

# Create your views here.
def home(request):
    ann = announcement.objects.all().order_by('-createdDate')
    context = {"announcement":ann}
    return render(request,'home/index.html',context)

def iicStudent(request):
    return render(request,'home/iic-student.html')
def iicFaculty(request):
    return render(request,'home/iic-faculty.html')
def ExternalExperts(request):
    return render(request,'home/external-experts.html')
def incubationCell(request):
    return render(request,'home/incubation.html')
def innovationCell(request):
    return render(request,'home/innovation.html')
def about(request):
    return render(request,'home/about.html')
def upcomingEvents(request):
    x = datetime.datetime.now()
    events=Events.objects.filter(dateEvent__gte=x).order_by('dateEvent')
    context={"events":events}
    return render(request,'home/upcoming-events.html',context)
def previousEvents(request):
    x = datetime.datetime.now()
    events=Events.objects.filter(dateEvent__lt=x).order_by('dateEvent')
    context={"events":events}
    return render(request,'home/previous-events.html',context)

def innovationAmbassador(request):
    return render(request,'home/innovation_ambassador.html')

def contact(request):
    context = {}
    if request.method == 'POST':
        person_name = request.POST['person_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        obj1 = Contact(name=person_name,email=email,subject=subject,message=message)
        obj1.save()
        context = {"message":True}
    return render(request,'home/contact.html',context)

def joinIIC(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        college = request.POST['college']
        course = request.POST['course']
        year = request.POST['year']
        if JoinIIC.objects.filter(email=email).exists() or JoinIIC.objects.filter(phone=phone).exists():
            message = "You are already a IIC member"
        else:
            obj = JoinIIC(first_name=fname,last_name=lname,email=email,phone=phone,college=college,course=course,year=year)
            obj.save()
            message = "Thankyou for joining IIC, we will contact you soon"
        ann = announcement.objects.all().order_by('-createdDate')
        context = {"announcement":ann,"message":message}
        return render(request,'home/index.html',context)

def eventDesc(request,slug):
    event = Events.objects.filter(title=slug).first()
    organize = event.Eventorganizers.all()
    return render(request,'home/eventDescription.html',{"event":event,"organize":organize})

