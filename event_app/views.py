from django.http import HttpResponse
from django.template import loader
from .models import Event,Participant
from django.core.mail import EmailMessage
from twilio.rest import Client


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
        'msg':"For Registering your Event with us"
        
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
    parts=Participant.objects.all()
    cons=""
    for part in parts:
        print(part.event_id)
        if int(part.event_id) == int(eid):
            cons += str(part.phone) + "/"

    event = Event.objects.get(id=eid)
    context={
        'event':event,
        'registered':cons
    }
    return HttpResponse(template.render(context , request))

def Participant_sub(request):
    template = loader.get_template('thank.html')
    name=request.POST['name']
    phno=request.POST['phno']
    mail=request.POST['email']
    rtype=request.POST['type']
    nos=request.POST.get('no' , 1)
    eid=request.POST['eid']
    Part = Participant(
        name=name , phone=phno, email=mail, participation_type=rtype, no_of_people=nos, event_id=eid
    )
    Part.save()
    parti = Participant.objects.latest('id')
    eve = Event.objects.get(id =eid)
    
    client=Client(account_sid,auth_token)
    msg2 = "Thank you "+name + " for registering your participation with us.\n\nParticipant Id : "+str(parti.id) 
    msg2+= "\nEvent Name : "+eve.name +"\nLocation : "+eve.location +"\nDate(s) : "+str(eve.fromdate) + " - " +str(eve.todate)
    msg2 += "\nTime : "+eve.fromtime+" - "+eve.totime + "\nParticipation Type : "+rtype + "\nNo. of People : "+str(nos)
    msg2 += "\n\nEVENT MANIA"
    msg=client.messages.create(
        body=msg2,
        from_ ='+15595308067',
        to='+91'+phno,
    )
    context = {
        'msg' : "For Registering your Participation with us"
    }
    return HttpResponse(template.render(context , request))



def dashboard(request):
    template = loader.get_template('Event_Dashboard.html')
    ps = Participant.objects.all()
    eids = "/"
    for p in ps:
        eids += str(p.event_id) + "/"
    parts=[]
    err = " "
    if request.method=='POST':
        eid=request.POST['eid']
        pas=request.POST['hpass']
        eve = Event.objects.get(id=eid)
        if eve.host_pass == pas: 
            parts = Participant.objects.filter(event_id = eid)
        else:
            err = "  * Invalid Password !!  "
    context = {
        'parts' : parts,
        'part_ids':eids,
        'error' : err
    }
    return HttpResponse(template.render(context , request))

