var startPageContainer = document.getElementsByClassName('pyluv-fade-in')[0];
var startPageButton = document.getElementsByClassName('pyluv-button')[0];
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

unfade(startPageContainer);

if(startPageButton){
    container.classList.remove('pyluv-container');
    document.title = 'Welcome to Pyluv'
    startPageButton.onclick = function(){
        window.location = 'home';
    }
}
else{
    navBar.classList.remove('pyluv-navbar-startpage');
}