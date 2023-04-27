// demo 2
// JS event propagation

var table = document.getElementsByTagName('table')[0];
var trs = document.getElementsByTagName('tr');
var tds = document.getElementsByTagName('td');

var clicky = function(e) {
  alert( this.innerHTML );
};

table.addEventListener('click', clicky);


for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky);
}



// Q: When user clicks on a cell, in what order will the pop-ups appear?
// The popups appear with child first, and then parent, the most nested tag first