
function valid()
{
    var name=document.getElementById('ename').value;
    var desc=document.getElementById('edesc').value;
    var loc=document.getElementById('eloc').value;
    var fdate=document.getElementById('fdate').value;
    var ftime=document.getElementById('ftime').value;
    var tdate=document.getElementById('tdate').value;
    var ttime=document.getElementById('ttime').value;
    var edate=document.getElementById('edate').value;
    var etime=document.getElementById('etime').value;
    var email=document.getElementById('hemail').value;
    var pass=document.getElementById('hpass').value;

    

    if(name == ""){
        document.getElementById('errorname').innerHTML="*please enter name";
        document.getElementById('ename').style.borderColor='red';
        return false; 
    }
    else{
        document.getElementById('errorname').innerHTML="";
        document.getElementById('ename').style.borderColor='black';
    }
    if(desc == ""){
        document.getElementById('errordesc').innerHTML="<br>*please enter description";
        document.getElementById('edesc').style.borderColor='red';
        return false;
    }
    else{
        document.getElementById('errordesc').innerHTML="";
        document.getElementById('edesc').style.borderColor='black';
    }
    if(loc==""){
        document.getElementById('errorloc').innerHTML="*please enter location";
        document.getElementById('eloc').style.borderColor='red';
        return false;
    }
    else{
        document.getElementById('errorloc').innerHTML="";
        document.getElementById('eloc').style.borderColor='black';
    }
    if(fdate == ""){
        document.getElementById('errorfdate').innerHTML="*please enter from date";
        document.getElementById('fdate').style.borderColor='red';
        return false;
    }
    else{
        document.getElementById('errorfdate').innerHTML="";
        document.getElementById('fdate').style.borderColor='black';
    }
    if(ftime == ""){
        document.getElementById('errorfdate').innerHTML="*please enter from time";
        document.getElementById('ftime').style.borderColor='red';
        return false;
    }
    else{
        document.getElementById('errorfdate').innerHTML="";
        document.getElementById('ftime').style.borderColor='black';
    }
    if(tdate == ""){
        document.getElementById('errortdate').innerHTML="*please enter to date";
        document.getElementById('tdate').style.borderColor='red';
        return false;
    }
    else{
        document.getElementById('errortdate').innerHTML="";
        document.getElementById('tdate').style.borderColor='black';
    }
    if(ttime == ""){
        document.getElementById('errortdate').innerHTML="*please enter to time";
        document.getElementById('ttime').style.borderColor='red';
        return false;
    }
    else{
        document.getElementById('errortdate').innerHTML="";
        document.getElementById('ttime').style.borderColor='black';
    }
    if(edate == ""){
        document.getElementById('erroredate').innerHTML="<br>*please enter deadline date";
        document.getElementById('edate').style.borderColor='red';
        return false;
    }
    else{
        document.getElementById('erroredate').innerHTML="";
        document.getElementById('edate').style.borderColor='black';
    }
    if(etime == ""){
        document.getElementById('erroredate').innerHTML="<br>*please enter deadline time";
        document.getElementById('etime').style.borderColor='red';
        return false;
    }
    else{
        document.getElementById('erroredate').innerHTML="";
        document.getElementById('etime').style.borderColor='black';
    }
    if(email == ""){
        document.getElementById('erroremail').innerHTML="*please enter host email";
        document.getElementById('hemail').style.borderColor='red';
        return false;
    }
    else{
        document.getElementById('erroremail').innerHTML="";
        document.getElementById('hemail').style.borderColor='black';
    }
    if(pass == ""){
        document.getElementById('errorpass').innerHTML="*please enter password";
        document.getElementById('hpass').style.borderColor='red';
        return false;
    }
    else{
        document.getElementById('errorpass').innerHTML="";
        document.getElementById('hpass').style.borderColor='black';
    }
}
