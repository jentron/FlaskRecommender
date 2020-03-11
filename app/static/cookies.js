function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  var expires = "expires="+d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function setSessionCookie(cname, cvalue) {
  var expires = "expires=0"; // a session cookie
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function deleteCookie(cname) {
  var d = new Date();
  d.setTime(d.getTime() - (24 * 60 * 60 * 1000));
  var expires = "expires="+d.toUTCString();
  document.cookie = cname + "=" + "" + ";" + expires + ";path=/";
}


function getCookie(cname) {
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function toggleSelection(id){
            cvalue = getCookie("selected").split(",");
            var idx = cvalue.indexOf(id.toString());
            if(idx < 0) {
document.getElementById('movie'+id).classList.add('selected'); //add
              if(cvalue == "") cvalue = [id];
              else cvalue.push(id);
            } else {
document.getElementById('movie'+id).classList.remove('selected'); //remove
              cvalue.splice(idx, 1);
            }
            setSessionCookie("selected", cvalue.toString());
    };

function markAllSelected(){
  cvalue = getCookie("selected").split(",");
  cvalue.forEach(function(item, index){
     e=document.getElementById('movie'+item);
     if(e != null) e.classList.add('selected'); 
  });
}

