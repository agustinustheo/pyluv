var homeContainer = document.getElementsByClassName('pyluv-fade-in')[0];

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

if(homeContainer){
    unfade(homeContainer);
}