function valid_dashboard()
{
    var eid = document.getElementById("eid").value;
    var pass = document.getElementById("hpass").value;
    var pids = document.getElementById("pids").value;
    var search = "/"+eid+"/";
    document.getElementById('error').innerHTML="";
    document.getElementById('error').style.backgroundColor = 'transparent';
    document.getElementById('eid').style.borderColor='black';

    if (eid == ""){
        document.getElementById('errorid').innerHTML="*please enter event id";
        document.getElementById('eid').style.borderColor='red';
        return false;
    }
    else{
        document.getElementById('errorid').innerHTML="";
        document.getElementById('eid').style.borderColor='black';
    }

    if (pass == ""){
        document.getElementById('errorpass').innerHTML="*please enter password";
        document.getElementById('hpass').style.borderColor='red';
        return false;
    }
    else{
        document.getElementById('errorpass').innerHTML="";
        document.getElementById('hpass').style.borderColor='black';
    }

    if(! pids.includes(search) ){
        document.getElementById('error').innerHTML="  *the given event id does not exists !  ";
        document.getElementById('error').style.backgroundColor = 'red';
        document.getElementById('eid').style.borderColor='red';
        return false;
    }
    else{
        document.getElementById('error').innerHTML="";
        document.getElementById('eid').style.borderColor='black';
    }
}