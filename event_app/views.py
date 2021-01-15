from django.http import HttpResponse
from django.template import loader
from .models import Event,Participant
from django.core.mail import EmailMessage


def index(request):
    template = loader.get_template('index.html')
    context = {
    }
    return HttpResponse(template.render(context , request))

def registration(request):
    template = loader.get_template('registration.html')
    context = {
        
    }
    return HttpResponse(template.render(context , request))

def registration_sub(request):
    template = loader.get_template('thank.html')
    ename=request.POST['ename']
    desc=request.POST['edesc']
    loc=request.POST['eloc']
    fdate=request.POST['fdate']
    tdate=request.POST['tdate']
    edate=request.POST['edate']
    ftime=request.POST['ftime']
    ttime=request.POST['ttime']
    etime=request.POST['etime']
    hmail=request.POST['hemail']
    hpass=request.POST['hpass']
    event_obj = Event(  name=ename , description=desc, location=loc, fromdate=fdate, 
                        fromtime=ftime, todate=tdate, totime=ttime, enddate=edate, 
                        endtime=etime ,host_email=hmail , host_pass=hpass)
    event_obj.save() 
    evid = Event.objects.latest('id')
    ctx={ 'name':ename , 'eid':evid.id}
    msg=loader.get_template('mail.html').render(ctx)
    message = EmailMessage(
        'Event Registration Successful',
        msg,
        'rutuchudasama.2000@gmail.com',
        [hmail]
    )
    message.content_subtype="html"
    message.send()
    context = {
        
    }
    return HttpResponse(template.render(context , request))

def participant(request):
    template = loader.get_template('participant.html')
    parts=Event.objects.all()
    context = {
        'events' : parts,
    }
    return HttpResponse(template.render(context , request))

def participant_registration(request):
    template = loader.get_template('Participant_register.html')
    eid=request.GET['id']
    event = Event.objects.get(id=eid)
    context={
        'event':event
    }
    return HttpResponse(template.render(context , request))

def Participant_sub(request):
    template = loader.get_template('thank.html')
    name=request.POST['name']
    phno=request.POST['phno']
    mail=request.POST['email']
    rtype=request.POST['type']
    nos=request.POST['no']
    eid=request.POST['eid']
    Part = Participant(
        name=name , phone=phno, email=mail, rtype=rtype, participants=nos, event=eid
    )
    Part.save()
    context = {
    }
    return HttpResponse(template.render(context , request))

