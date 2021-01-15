
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
}

$(document).ready(function()
{
	$("#subreg").click(function()
	{
        alert("call");
        var name=$("#ename").val().trim();
        var desc=$("#edesc").val().trim();
        var loc=$("#eloc").val().trim();
        var fdate=$("#fdate").val().trim();
        var ftime=$("#ftime").val().trim();
        var tdate=$("#tdate").val().trim();
        var ttime=$("#ttime").val().trim();
        var edate=$("#edate").val().trim();
        var etime=$("#etime").val().trim();
        var email=$("#hemail").val().trim();
        var pass=$("#hpass").val().trim();
        alert("call");

        if(name==''){
            $('#errorname').html('please enter name');
            evereg.ename.focus();
            return false;
        }
        
        var re = /^[a-zA-Z ]*$/;
        if(!re.test(name)) 
        {
            $('#errorname').html('Username must contain only letters');
            evereg.ename.focus();
            return false;
        }
        else
        {
            $('#errorname').html('');
        }
    });
});