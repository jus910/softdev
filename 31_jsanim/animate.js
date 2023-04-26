// Team UHhh - FMC, JM
// SoftDev pd2
// K31 -- Paint, Paint, Paint
// 2023-04-26w

var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");
ctx.fillStyle = "#00FFFF";

var requestID; // init global var

var clear = (e) => {
  // console.log("wiping canvas...");
  ctx.clearRect(0, 0, 500, 500);
};

var radius = 0;
var growing = true;

var drawDot = () => {
  // console.log("start drawing...");
  stopIt();

  var draw = () => {
    if (radius == 250) {
      growing = false;
    }
    if (radius == 0) {
      growing = true;
    }
  
    if (growing) {
      radius = radius + 1;
    } else {
      radius = radius - 1;
    }
  
    clear();
    ctx.beginPath();
    ctx.arc(250, 250, radius, 0, 2 * Math.PI);
    ctx.fill();
    // ctx.stroke();
    
    requestID = window.requestAnimationFrame(draw);
  }

  requestID = window.requestAnimationFrame(draw);
};

var stopIt = () => {
  // console.log("stopping it...");
  console.log(requestID);
  window.cancelAnimationFrame(requestID)
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
