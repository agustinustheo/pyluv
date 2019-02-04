var apiTitleContainer = document.getElementsByClassName('pyluv-fade-in')[0];
var idSMSClassifyButton = document.getElementsByClassName('pyluv-api-button')[0];

function unfade(element) {
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
    
function getFirstFormInput(formElement){
    inputElement = formElement.getElementsByTagName("input")[0];
    return inputElement.value;
}

unfade(apiTitleContainer);

if(idSMSClassifyButton){
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