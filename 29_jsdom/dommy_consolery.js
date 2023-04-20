// Team UHhh :: FMC, JM
// SoftDev pd02
// K29 -- Building Castles in the Sand
// 2023-04-20r
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello"; // i may be redefined to an object that's not a string
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30; // does not change the value of j outside the function 
  return j+x; // uses the j value defined in the function
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) { // callable with o.func(x)
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li"); // creates an element with the property li, so it continues numbering the list
  newitem.innerHTML = text; 
  list.appendChild(newitem); 
};

// Adding Text
var addText = function(id, text) {
  var list = document.getElementById(id);
  var newitem = document.createElement("text");
  newitem.innerHTML = text; 
  list.appendChild(newitem); 
};


var removeItem = function(n) { // standard index convention starting at 0
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red'); // appends red to the class list
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...

// FIB

var fib = function(n) {
  if (n == 0) {
      return 0;
  }
  if (n == 1) {
      return 1;
  }
  return fib(n - 1) + fib(n - 2);
};

// FAC

var fact = function(n) {
  if (n > 1) {
      return n * fact(n - 1);
  } else {
      return 1;
  }
};

// GCD

var gcd = function(m, n) {
  if (m % n == 0) {
    return n;
  }
  return gcd(n, m % n);
};



// LE BUTTONS
var isJinged = false;
var isRyaned = false;
var isFanged = false;

var jing = function() {
  if (!(isJinged)) {
    addText("fib0", fib(0));
    addText("fib5", fib(5));
    isJinged = true;
  }
};

var but1 = document.getElementById("fibby");
but1.addEventListener('click', jing);

var ryan = function() {
  if (!(isRyaned)) {
    addText("fact0", fact(0));
    addText("fact5", fact(5));
    isRyaned = true;
  }
}

var but2 = document.getElementById("facty");
but2.addEventListener('click', ryan);

var fang = function() {
  if (!(isFanged)) {
    addText("gcd0_1", gcd(0,1));
    addText("gcd10_15", gcd(10,15));
    isFanged = true;
  }
};

var but3 = document.getElementById("gcdee");
but3.addEventListener('click', fang);