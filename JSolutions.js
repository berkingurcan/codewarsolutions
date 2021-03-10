// 8 and 7 Kyu problems


/* Story
Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.

Task
Write a function that returns both the minimum and maximum number of the given list/array. */

/*Solution*/

function minMax(arr){
  var x = arr.sort(function(a,b){return a-b;});

  return [x[0],x[arr.length -1]];
}



/*Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.*/

function booleanToString(b){
  return b.toString();
}


/*Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"*/

function bmi(weight, height) {
  var wh = weight / (height**2);
  if(wh <= 18.5){
    return "Underweight";
  }
  else if(wh <= 25.0){
    return "Normal";
  }
  else if(wh <= 30.0){
    return "Overweight";
  }
  else{
    return "Obese";
  }
}

/*Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

Examples
Input: [1, 5.2, 4, 0, -1]
Output: 9.2

Input: []
Output: 0

Input: [-2.398]
Output: -2.398

Assumptions
You can assume that you are only given numbers.
You cannot assume the size of the array.
You can assume that you do get an array and if the array is empty, return 0.
What We're Testing
We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.
Advanced users may find this extremely easy and can easily write this in one line.*/

// Sum Numbers
function sum (numbers) {
    var x = 0;
    numbers.forEach(lele);
    function lele(i){
      x += i;
    }
    
    return x;
};



/*Description:
Make a simple function called greet that returns the most-famous "hello world!".

Style Points
Sure, this is about as easy as it gets. But how clever can you be to create the most creative hello world you can think of? What is a "hello world" solution you would want to show your friends?*/


function greet(){
  return "hello world!";
  }// Write a function "greet" that returns "hello world!"


/*In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

highAndLow("1 2 3 4 5");  // return "5 1"
highAndLow("1 2 -3 4 5"); // return "5 -3"
highAndLow("1 9 3 4 -5"); // return "9 -5"
Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.*/

function highAndLow(numbers){
  var x = numbers.split(" ");
  var y = x.sort(function(a,b){return a-b});
  return y[y.length -1] + " "+ y[0]
}

/*Write a function called repeat_str which repeats the given string src exactly count times.

repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"*/

function repeatStr (n, s) {
  var x = "";
  for(i=0; i < n; i++){
   x += s;
  }
  return x;
}



/*It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.*/


function removeChar(str){
 var str = str.slice(1,-1);
 return str;
}


/*Summation
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

For example:

summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8*/

var summation = function (num) {
  var x = 0;
  for (i=1; i < num+1; i++){
    x += i;
  }
  return x;
}


/*Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'*/

function solution(str){
  return str.split('').reverse().join('')
}

/*Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples
basicOp('+', 4, 7)         // Output: 11
basicOp('-', 15, 18)       // Output: -3
basicOp('*', 5, 5)         // Output: 25
basicOp('/', 49, 7)        // Output: 7*/

function basicOp(operation, value1, value2)
{
  if(operation == '+') 
  {return value1 + value2;}
  else if(operation == '-') { return value1 - value2;}
  else if(operation == '*') { return value1 * value2;}
  
  else{return value1/value2;}
}

