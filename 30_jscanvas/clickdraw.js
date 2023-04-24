
var c = document.getElementById("slate");
var ctx = c.getContext("2d");

var mode = "rect";


var toggleMode = (e) => {

    return 3
}

var drawRect = function(e) {  
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick", mouseX, mouseY);

    ctx.fillRect(mouseX, mouseY, 100, 100);

}

var draw = (e) => {
    drawRect(e);
}
c.addEventListener("click",drawRect);
