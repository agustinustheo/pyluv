var apiTitleContainer = document.getElementsByClassName('pyluv-fade-in')[0];
var idSMSClassifyButton = document.getElementById('idSMSClassifyButton');
var fakeNewsClassifyButton = document.getElementById('fakeNewsClassifyButton');
var idFakeNewsClassifyButton = document.getElementById('idFakeNewsClassifyButton');
var navBar = document.getElementsByClassName('pyluv-navbar')[0];
var container = document.getElementsByClassName('pyluv-container')[0];

function unfade(element) {
    if(element){
        var op = 0.001;  // initial opacity
        var timer = setInterval(function () {
            if (op >= 1){
                clearInterval(timer);
            }
            element.style.opacity = op;
            element.style.filter = 'alpha(opacity=' + op * 100 + ")";
            op += op * 0.1;
        }, 10);
    }
}
    
function getFirstFormInput(formElement){
    if(formElement){
        inputElement = formElement.getElementsByTagName("input")[0];
        return inputElement.value;
    }
}

unfade(apiTitleContainer);

if(idSMSClassifyButton){
    container.classList.remove('pyluv-container');
    document.title = document.title + " - Indonesian SMS Classifier"

    idSMSClassifyButton.onclick = function(e){
        e.preventDefault();
    
        var smsText = getFirstFormInput(document.getElementsByTagName("form")[0]);
    
        axios.get('id/classify', {
            params: {
                sms_text : smsText
            }
         })
         .then(response => {
            if(response.data === "normal"){
                alert('This is a normal message');
            }
            else if(response.data === "promo"){
                alert('This is a promo message');
            }
            else if(response.data === "spam"){
                alert('This is a spam message');
            }
         })
         .catch(ex => {
            console.log(ex);
         })
    }
}
else if(fakeNewsClassifyButton){
    container.classList.remove('pyluv-container');
    document.title = document.title + " - Fake News Detector"

    fakeNewsClassifyButton.onclick = function(e){
        e.preventDefault();
    
        var article = getFirstFormInput(document.getElementsByTagName("form")[0]);
    
        axios.get('en/classify', {
            params: {
                article : article
            }
         })
         .then(response => {
            alert(response.data)
         })
         .catch(ex => {
            console.log(ex);
         })
    }
}
else if(idFakeNewsClassifyButton){
    container.classList.remove('pyluv-container');
    document.title = document.title + " - Indonesian Fake News Detector"
    
    idFakeNewsClassifyButton.onclick = function(e){
        e.preventDefault();
    
        var article = getFirstFormInput(document.getElementsByTagName("form")[0]);
    
        axios.get('id/classify', {
            params: {
                article : article
            }
         })
         .then(response => {
            alert(response.data)
         })
         .catch(ex => {
            console.log(ex);
         })
    }
}
else{
    navBar.classList.remove('pyluv-navbar-api');
}