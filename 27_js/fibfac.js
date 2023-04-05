// Team Hair Investment Uncles :: Daniel He, Justin Mohabir
// SoftDev pd2
// K27 -- Basic functions in JavaScript
// 2023-04-04t
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn

function fac(n) {
  if (n<2){
    return 1
  }
  return n * fac(n-1);
}

function fib(n) {
  if (n==0){
    return 0
  }
  if (n==1){
    return 1
  }
  return fib(n-1) + fib(n-2);
}

//Test Cases

console.log("factorial:", fac(1), fac(2), fac(3), fac(4), fac(5))
console.log("fib:", fib(1), fib(2), fib(3), fib(4), fib(5))


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
