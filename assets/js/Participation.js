document.getElementById("no").disabled = true;

function group_sel()
{
    document.getElementById("no").disabled = false;
    document.getElementById("no").min=2;
    document.getElementById("no").value=2;
}

function individual_sel()
{
    document.getElementById("no").disabled = true;
    document.getElementById("no").value=1;
}

function check()
{
    var name=document.getElementById('name').value;
    var phno=document.getElementById('phno').value;
    var email=document.getElementById('email').value;
    var no=document.getElementById('no').value;
    if(name == ""){
        document.getElementById('errorname').innerHTML="*please enter name";
        document.getElementById('name').style.borderColor='red';
        return false; 
    }
    else{
        document.getElementById('errorname').innerHTML="";
        document.getElementById('name').style.borderColor='black';
    }
    var pat=/^[0-9]{10,}$/;
    if(phno == ""){
        document.getElementById('errorphno').innerHTML="*please enter Contact no";
        document.getElementById('phno').style.borderColor='red';
        return false; 
    }
    else if (phno.length != 10)
    {
        document.getElementById('errorphno').innerHTML="*please enter 10 digits";
        document.getElementById('phno').style.borderColor='red';
        return false;
    }
    else if (! pat.test(phno) )
    {
        document.getElementById('errorphno').innerHTML="*only digits are allowed";
        document.getElementById('phno').style.borderColor='red';
        return false;
    }
    else{
        document.getElementById('errorphno').innerHTML="";
        document.getElementById('phno').style.borderColor='black';
    }

    if(email == ""){
        document.getElementById('erroremail').innerHTML="*please enter email";
        document.getElementById('email').style.borderColor='red';
        return false; 
    }
    else{
        document.getElementById('erroremail').innerHTML="";
        document.getElementById('email').style.borderColor='black';
    }
    if(!(document.getElementById('grp').checked  || document.getElementById('ind').checked ))
    {
        document.getElementById('errortype').innerHTML="<br>*please select participation";
        return false; 
    }
    else{
        document.getElementById('errortype').innerHTML="";
    }
}