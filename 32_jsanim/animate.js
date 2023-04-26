//heading

var c = document.getElementById("playground");
//get dot button
var dotButton = document.getElementById("buttonCircle");
//stop button
var stopButton = document.getElementById("buttonStop");
//dvd button
var dvdButton = document.getElementById("buttonDVD");

var ctx = c.getContext("2d");

ctx.fillStyle = '#7FFFD4';

const img = new Image();
img.src = "logo_dvd.jpg"

//global var for use with animation frames
var requestID;

var clear = (e) => {
    ctx.clearRect(0,0,c.clientWidth,c.clientHeight)
};

var radius = 0;
var growing = true;

var drawDot = () => {
    //clear
    clear();
    //repaint the circle
    ctx.beginPath();
    ctx.arc(c.clientWidth / 2, c.clientHeight / 2, radius, 0, 2 * Math.PI);
    ctx.fill();
    ctx.stroke();
    if (growing){
        radius++;
    } else {
        radius--;
    }

    if (radius == (c.clientWidth / 2) || radius == 0){
        growing = !growing;
    }
    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);
}
var x = Math.floor(Math.random() * (c.clientWidth-100));
var y = Math.floor(Math.random() * (c.clientWidth-100));
var x_change = 1;
var y_change = 1;

var drawDVD = () => {
    //clear
    clear();
    var s = 5;
    //console.log(img.width/10);
    //repaint the circle
    ctx.beginPath();
    x=x+x_change;
    y=y+y_change;
    ctx.drawImage(img, x+x_change, y+y_change,img.width/s, img.height/s);
    ctx.fill();
    ctx.stroke();
    if (x==0 || x==c.clientWidth-(img.width/s)){
        x_change = -x_change;
    }

    if (y==0 || y==c.clientWidth-(img.height/s)){
        y_change = -y_change;
    }

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDVD);
}

//var stopIt = function
var stopIt = () => {
    window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener( "click", drawDot);
stopButton.addEventListener( "click", stopIt);
dvdButton.addEventListener("click", drawDVD );
