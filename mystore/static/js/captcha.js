function validateForm(){
    document.getElementById('log').innerHTML = '';
    var string1 = removeSpaces(document.getElementById('mainCaptcha').value);
    var string2 = removeSpaces(document.getElementById('txtInput').value);
    if (string1 != string2 || string2 == ""){
    Captcha();
    document.getElementById('log').innerHTML += '<span style="font-size:16px; padding: 25px;">Entered Invalid Captcha</span> ';
    return false;
    }
    }
    function Captcha(){
    var alpha = new Array('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0');
    var i;
    for (i=0;i<6;i++){
    var a = alpha[Math.floor(Math.random() * alpha.length)];
    var b = alpha[Math.floor(Math.random() * alpha.length)];
    var c = alpha[Math.floor(Math.random() * alpha.length)];
    var d = alpha[Math.floor(Math.random() * alpha.length)];
    var e = alpha[Math.floor(Math.random() * alpha.length)];
    var f = alpha[Math.floor(Math.random() * alpha.length)];
    var g = alpha[Math.floor(Math.random() * alpha.length)];
    }
    var code = a + ' ' + b + ' ' + ' ' + c + ' ' + d + ' ' + e + ' '+ f + ' ' + g;
    document.getElementById("mainCaptcha").value = code
    var colors = ["#B40404", "#beb1dd", "#b200ff", "#faff00", "#0000FF", "#FE2E9A", "#FF0080", "#2EFE2E", ];
    var rand = Math.floor(Math.random() * colors.length);
    $('#mainCaptcha').css("background-color", colors[rand]);
    }
    function removeSpaces(string){
    return string.split(' ').join('');
    }