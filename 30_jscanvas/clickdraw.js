// Team Hair Investment Uncles :: Daniel He, Justin Mohabir, Sir, Alfred
// SoftDev pd2
// K30-- JS Paint
// 2023-04-24m
// --------------------------------------------------

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
ctx.fillStyle = "red";

var mode = "rect";


var toggleMode = (e) => {
  console.log("toggling...");
  if (mode == "rect") {
    mode = "circ";
    bToggler.innerHTML = "circ";
  } else {
    mode = "rect";
    bToggler.innerHTML = "rect";
  }
}

var drawRect = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick", mouseX, mouseY);

    ctx.fillRect(mouseX, mouseY, 100, 200);

}

var drawCircle = function(e) {
  var mouseX = e.offsetX;
  var mouseY = e.offsetY;
  console.log("mouseclick", mouseX, mouseY);

  ctx.beginPath();
  ctx.arc(mouseX, mouseY, 50, 0, Math.PI * 2, true);
  ctx.stroke();
  ctx.fill();

}


var draw = (e) => {
  if (mode == "rect") {
    drawRect(e);
  } else {
    drawCircle(e);
  }
  console.log(e);
}

var wipeCanvas = () =>{
  ctx.clearRect(0, 0, 10000, 10000);
}

c.addEventListener("click",draw);

var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);

var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);
