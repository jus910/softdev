// demo 3
// JS event propagation

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];

var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  e.stopPropagation();
  // Only one element gives an alert, the alert will be the most nested element, unless a higher element has true
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky,true);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky,true);
}

//Predict, then test...
//Q: What effect does the boolean arg have?
//   (Leave exactly 1 version uncommented to test...)
// Propagates from child to parent

//table.addEventListener('click', clicky, true);
table.addEventListener('click', clicky,true);

// Q: When user clicks on a cell, in what order will the pop-ups appear?
// Only one popup appears, and that will be the most nested element, unless a less nested element has true