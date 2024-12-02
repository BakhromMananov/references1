'use strict'

// 3 TYPES OF VARIABLES
var; // function scope
const; // block scope
let; // block scope


// 7 FORMS OF PRIMITIVE DATA TYPES
let string = "hi, how are you?"; 
let number = 0.75;                
let boolean = true;  
let undefined;  
    null;   
let symbol 
let BigInt 


// LOGICAL OPERATORS
x < 10  &&  x!==5  
y > 9   ||  x===5  
!       !  (x===y)


// COMPARISON OPERATORS
x > 10;       
x >= 5;       
x < -50;           
x <= 100;     
x == "5";           
x != "b";               
x === "5";      
x !== "5";     


// ARITHMETIC OPERATORS
1 + 1  
2 - 1  
4 / 2  
2 * 6
5 % 2  
1 ++ 
2 -- 

// IF/ELSE CONDITIONALS
if(1<2) {
    console.log('cool')
} else if (2<3) {
    console.log('very cool')
} else {
    console.log('not cool')
};


// TERNARY OPERATOR
let fn = 'john'; let age=19;
age>=18 ? cl(fn + ' drinks beer') : cl(fn + ' drinks juice')
let drink = age >=18 ? 'beer' : 'juice';


//SWITCH OPERATOR
const firtName= 'John'; const job = 'teacher'; 
switch (job) {
    case 'teacher':
    case 'instructor':
        return firstName + 'teaches';
    break;
    case 'driver':
        return firstName + 'drives';
    break;
    default: firstName + 'does smth else'; 


/* falsy values: undefined, null, 0, '', NaN */
/* truthy values: not falsy values; */

// LOOPS
// for loop
let john = ['john', 'smith', 1990, 'designer', false]; 
for ( let i=0; i<john.length; i++) { console.log (john[i])}; 
for ( let i=john.length -1; i>=0; i--) { console.log (john[i])}; 

let coolStuff = ['jacket', 'bullet', 'battery' ]

for (let i = 0; i<coolStuff.length; i++) { 
    if (typeof coolStuff[i] !=='string') continue; // CONTINUE STATEMENT will ignore numbers
    console.log(coolStuff[i]);     
};

for (let i = 0; i<coolStuff.length; i++) { 
    if (typeof coolStuff[i] !=='string') break; // BREAK STATEMENT will stop if item is string 
    console.log(coolStuff[i]);     
};


const calcTips = function() {
    let tips = []; 
    let finalValues = [];
    let bills = [124, 48, 268, 180, 42];
    for (let i=0; i < bills.length; i++) {
        let percentage;
        let bill = this.bills[i];
        if (bill < 50) {
            percentage =.2;
        } else if (bill >= 50 && bill < 200) {
            percentage=.15;
        } else {
            percentage =.1
        }
        tips[i].push = bill * percentage;
        finalValues[i].push = bill + bill*percentage; 
    }
calcTips(); 

// while loop
let i = 0; 
while (i<john.length) {console.log (john[i]); i++ }; 

// do while loop

// for of loop - new version of forEach 
const menu =[`Focassia`, 'Bruschetta', ' Garlic bread', 'Caprese salad','Pizza', 'Pasta', 'Risotto' ]
for(const item of menu) {
    console.log(item)
}

//  forEach LOOP
const array =[1,2,10,16]
const double=[]
const newArray=array.forEach((num)=> {   // forEach does not return anything
    double.push(num*2); 
})
console.log(double)




// CONSOLE
console.log(); 
console.table(); 
console.error(); 
console.table(); 
console.dir(); 
console.trace(); 




// STRINGS
let user = new String('jonas') // one way to create string
let greeting = 'Hi' + 'Molly';  // + concatanating two strings
    greeting +=' how are you doing?'; // += adding new value to string


// string operators
const firstName = 'John'; const lastName ='Smith';
const fullName = `${firstName} ${lastName}`;
fullName[0] 
fullName.startsWith('j'); 
fullName.endsWith('Sm'); 
fullName.includes('oh'); 
fullName.repeat(5); 
fullName.toUpperCase();
fullName.toLowerCase();
fullName.indexOf();
fullName.lastIndexOf();
fullName.slice(3,2);
fullName.splice(3,4);
fullName.trim(); //cutting out empty space 
fullName.replace(lastName, givenName)
fullName.split('');
fullName.join('');
fullName.padStart(10,'+');
fullName.padEnd(10, ''); 


// converting value to string
String(); 


// NUMBERS
let firstNumber = 1234;

// converting value to number
parseInt();
parseFloat();
Number();

// math methods 
Math.round(); 
Math.ceil(); 
Math.trunc(); 
Math.floor(); 
Math.random(); 
Math.sqrt();
Math.abs();  


// ARRAYS
let  numbers = [1,'jack',true,4,5,6]; // every element of array has index value
numbers[i] // index value of array starts from 0 

// array methods
numbers[2]; // accesing items in arrays
numbers[0] = 'mary' /*mutating array */
numbers.indexOf('jack') /* returns index position of element in array*/ 
numbers.length() // see how many items in array 


numbers.toFixed(2); //rouding decimals  

// methods that mutate arrays
numbers.push(7, 8, 9); // adding data to the end of array
numbers.unshift(0); //adding data to the beginning of array

numbers.pop(); // this method removes last item
numbers.shift(); // this method removes 1st item 
numbers.splice()  // cut part of array that you need

numbers.reverse()
numbers.sort()
numbers.fill()

// methods creating new array
numbers.map()
numbers.filter() // filter using condition
numbers.slice(2,6) // cut slice part of array
numbers.concat ["value1", "value2"]; // concatanating arrays
numbers.flat () // flattening nested array
numbers.flatMap() // flattening nested array

// array index
numbers.indexOf()
numbers.findIndex() //based on test condition

//array element
numbers.find()

//know if array includes
numbers.includes()
numbers.some()
numbers.every()

// new string
numbers.join(', ') //this is a method to add sybols bwt arrays

//transform to value
numbers.reduce()

//to loop array 
numbers.forEach()


// array destructuring
const restaurant = {
    name: 'Classico Italiano',
    location: 'Via Angelo Tavanti',
    categories: ['Italian', 'Pizzaria', 'Vegetarian']
}

const [first, second] = restaurant.categories;
console.log(first, second)

// OBJECTS
// when copying variables, objects use reference while primitives use copy
// creating new object
const hotel = new Object ();
hotel.name='Quay';
hotel.rooms=50,
hotel.booked= 25,
hotel.gym=true,
hotel.roomTypes = ['twin', 'triple', 'suite'],
hotel.prototype.checkAvailability=function() { // this function is object method, never ever use arrow functions for object methods 
    return this.room - this.booked; 
}

//object literal - set of variables & functions containing keys & values
const hotel = { 
    name: 'Quay',
    rooms: 50,
    booked: 25,
    gym: true,
    roomTypes: ['twin', 'double', 'suite'],
    checkAvailability: function () {
        return this.room - this.booked; 
    }
}; 


// creating new objects with object.create
let personProto = {
    name= 'john',
    yearOfBirth= 1990,
    job = 'teacher', 
    calcAge: function () {
        console.log(2016 - this.yearOfBirth);
    }
}

// option 1
let john = Object.create(personProto);
john.name= 'john';
john.yearOfBirth= 1990;
john.job = 'teacher'

// option 2
let jane = Object.create(personProto, {
    name: {value: 'Jane'},
    yearOfBirth: {value: 1969},
    job: {value: 'designer'}
});

// creating copy of object
const jessica = {
    firstName: 'Jessica',
    lastName: 'Williams',
    age: 27,
}

const jessicaCopy = Object.assign({}, jessica);
jessicaCopy.lastName='Davis';
console.log('Before marriage', jessica)
console.log('After marriage', jessicaCopy)


// object destructuring
const restaurant = {
    name: 'Classico Italiano',
    location: 'Via Angelo Tavanti',
    categories: ['Italian', 'Pizzaria', 'Vegetarian']
}

const {name, location, categories} = restaurant;  // use brackets like in object
console.log(name, location, categories)

const {name: restaurantName, location:street, categories:tags} = restaurant; // you can rename destructured elements
console.log(restaurantName, street, tags) 

// object keys, values, entries
const keys=Object.keys(restaurant);
console.log(keys);

const values=Object.values(restaurant);
console.log(values);

const entries=Object.entries(restaurant);
console.log(entries)

//SETS - list of unique values, use it to find out unique values repeated in maps
const ordersSet= new Set ([
    'pasta',
    'pizza',
    'pizza',
    'risotto',
    'pasta'
])

// set methods
ordersSet.size
ordersSet.has('pizza')
ordersSet.add('garlic bread')
ordersSet.delete('risotto')

// converting array to set & backwards
const staff = ['waiter', 'chef', 'waiter', 'manager', 'waiter']
const staffUnique= ([...new Set(staff)])


// MAPS
const question = new Map ();
question.set('question', 'what is JS') // you can add info with set
.set(1, 'es5')
.set(2, 'es6') // you can set info without map itself
.set(3, 'es7')
.get('question')

const question = new Map ([  // this is another way to create a map 
    ['question', 'what is JS'],
    [1, 'coding language'],
    [2, 'game to play'],
    ['correct', 3],
    [true, 'correct']
])

question.get('question') // this is how you extract information 
question.get(1)
question.has(1)



// SCOPE OF FUNCTIONS: 
// SCOPE - environment in which certain variables are declared
// SCOPE CHAIN - order in which functions are written in the code, every scope has access to its outer scope but not vice-versa.
// LEXICAL SCOPE - functions, blocks & keywords are placed in the code, they are not visible
// GLOBAL SCOPE - var is created outside of function & can be used anywhere; 
// FUNCTION SCOPE - var is function scoped;
// BLOCK SCOPE - const & let are block scoped; 


// HOISTING - making some variables accessible/usable in code before they are actually declared - function declation gets hoisted, var becomes undefined as byproduct of hoisting, const & let become uninitialized because of Temporal Dead Zone(TDZ)
// FUNCTION DECLARATION, the only function that can be hoisted
yearsTillRetirement(2021, 'Jody') 
function yearsTillRetirement (year, name) {
    var age =calcAge(year);  // calling another function as variable
    var retirement = 65 - age; 
    if (retirement> 0 || retirement===-1) {
        var retirement = 65 - age;
    console.log(name + ' retires in ' + retirement + " years")
    } else {
        console.log(name + ' is already retired, he is ' + age + ' years old')
    }
}


// FUNCTION EXPRESSION
var yearsTillRetirement =function  (year, name) {
    var age =calcAge(year);  /* calling another function as variable*/
    var retirement = 65 - age; 
    if (retirement> 0 || retirement===-1) {
        var retirement = 65 - age;
    console.log(name + ' retires in ' + retirement + " years")
    } else {
        console.log(name + ' is already retired, he is ' + age + ' years old')
    }
}
yearsTillRetirement(1989, 'Jack'); 


// ANONYMOUS FUNCTION STORED IN VARIABLE
    var alertRandNum = function () {
    var randNum = Math.floor(Math.random()*6) +1;
    alert(randNum); 
}; 
alertRandNum(); // to execute function, you call by this way




// FUNCTION WITH MORE THAN ONE INPUT/ARGUMENT/PARAMETER; ARITY - number of parameters a function can take, do not put more than 3 
function getRandomNumber (upper, lower) { 
    var randNum = upper * lower; 
    return randNum; 
}
console.log(getRandomNumber(10, 50));


// ARROW FUNCTIONS, they have lexical THIS keyword
const sayName = (namePer) => {
    const message = "My name is " + namePer;
    console.log (message);
}; 


// PASSING FUNCTION INTO ANOTHER FUNCTION  
let years = [1990, 1965, 1937, 2005,1998] /*data for processing*/
function arrayCalc(arr, fn) {  /*function that accepts data and another function*/ 
    var arrRes = [],
    for(let i =0; i<arr.length; i++) {
        arrRes.push(fn(arr[i]));
    }
    return arrRes;
}

function calcAge(el) {
    return 2016 - el;
}

function isFullAge(el) {
    return el>=18;
}

let ages=arrayCalc(years, calcAge);
let fullAges = arrayCalc(ages, isFullAge) 

// NEW ES6 function inside object 
const user = {
    firstName: 'John',
    lastName:'Travolta',
    birthYear: 1997,
    calcAge(birthYear) { //you skip function keyword & semicolons
        const now = new Date;
        const year=now.getFullYear()
        const age= year- birthYear;
        return age
    }
}
user.calcAge(); 


// CONSTRUNCTOR FUNCTION , name starts with capital letter in function constructors
const Person = function (name, yearOfBirth, job) { 
    this.name=name;
    this.yearOfBirth=yearOfBirth;
    this.job=job;
    this.calcAge = function () {
        console.log(2016 - this.yearOfBirth)
    }
}
const user = new Person('Jonas', 1996, 'coder')


// this function is joined to function constructor
Person.prototype.calcAge = function () {
    console.log(2016- this.yearOfBirth); 
}

// you can join properties also to function constructor & it will work ok
Person.prototype.lastName='Smith'

// you can create as many new objects as you want with function constructor
let john = new Person ('john', 1990, 'teacher')

// calling function inside function constructor
john.calcAge();
user.hasOwnProperty()
Person.prototype.isPrototypeOf(user)
user.__proto__===Person.prototype


// ES6 CLASS- SYNTACTIC SUGAR FOR CONSTRUCTOR FUNCTION 
class Person {
    constructor (firstName, birthYear) {
        this.firstName=firstName;
        this.birthYear=birthYear; 
    }
}

// IMMEDIATELY INVOKED FUNCTION EXPRESSIONS - IIFE
(function (goodLuck) {
    let score = Math.random() *10;
    console.log(score>=5 - goodLuck)
}) (5); 


// CLOSURE - a function ran. the function executed. its never going to execute again. but its going to remember that there are references to those variables so the child scope always has access to the parent scope. Children always have access to parent scope. but parents never have access to child scopes
const greet = function (greeting) {
    return function (firstName) {
        console.log(`${greeting} ${firstName}`); 
    };
};

const greeterHey= greet('Hey');
greeterHey('Jonas');
greeterHey('Steven'); 
greet('hello') ('Jonas'); 

function retirement (retirementAge) {
    let a ='years left until retirement';
    return function (yearOfBirth) {
        let age = 2016 - yearOfBirth;
        console.log((retirementAge - age) + a)
    }
}

let retirementUS = retirement(66);
retirementUS(1990);
retirement(66) (1990)


// DELAYING FUNCTION WITH SETTIMEOUT
window.setTimeout((smth) => {
    console.log(smth);
}, 3000, 'greetings to you!'); // 3000 sec delaying, this is setTimeout()

// event bubbling & delegation, the event object  
document.addEventListener('click',(event)=> {
    console.log(event.target);  
} ); 




// CURRYING
const multiply=(a,b) => a*b;
const curriedMultiply = (a) => (b) => a * b;
curriedMultiply (3) (5)
15

// COMPOSE
const compose = (f, g) => (a) => f(g(a));
const sum = (num) => num +1
compose (sum, sum) (5);


// MAP,FILTER, REDUCE
const yearsArray = [1990, 1965, 1982, 1937];
const mapArray=yearsArray.map(num => num * 2); 
const mapArray1=yearsArray.map(function(el) { return Math.abs(el -2021)});
const mapArray2 = yearsArray.map((el, index) => `Age element ${index +1}: ${2037-el}`);

let ages = [12,17,8,21,14,11];
let full=ages.map(function(cur) {
    return cur>=18;
})
console.log(full)
// filter 
const filterArray = array.filter(num => num>5);

// reduce 
const reduceArray = array.reduce ((accumulator, num ) => {
    return accumulator + num 
}, 0 ); 


// destructuring - extracting data from object or array
const john = ['John', 26];
const [name1, year] = ['John', 26];
console.log(name1)
console.log(year)

const obj = {
    firstName: 'John',
    lastName: 'Smith'
}

const {firstName, lastName} = obj;
console.log(firstName)
console.log(lastName)

const {firstName: a, lastName: b} = obj;
console.log(a)
console.log(b)



// call, apply, bind methods

let john = {
    name: 'John',
    age: 26,
    job: 'teacher',
    presentation: function (style, timeOfDay) {
        if(style==='formal') {
            console.log (`Good + ${timeOfDay}, Ladies and Gentlemen. I'm ${this.name}, ${this.job} & I'm ${this.age} years old`);
        } else if (style==='friendly') {
            console.log (`What's up. I'm ${this.name}, ${this.job} & I'm ${this.age} years old`)
    }
}
};

let emily = {
    name: 'emily',
    age: 35,
    job: 'designer'
}

john.presentation('formal', 'morning') 
john.presentation.call(emily, 'friendly', 'afternoon');   // call method

let johnFriendly= john.presentation.bind(john, 'friendly'); //bind method
johnFriendly('morning');
johnFriendly('night')

let emilyFormal= john.presentation.bind(emily, 'formal');
emilyFormal('afternoon');


// ASYNCRONOUS JAVASCRIPT
// setTimeOut()
const ingredients = ['olives', 'spinach']
const pizzaTimer=setTimeout((ing1, ing2) => console.log(`here is your pizza with ${ing1} and ${ing2}`), 3000, ...ingredients);
console.log('waiting...');
if(ingredients.includes('spinach')) clearTimeout(pizzaTimer)

// setInterval()
setInterval(function() {
    const now=new Date();
    console.log(now);
}, 1000)


// DATE & TIME
const date= new Date(2037, 10, 19, 15, 23)
date.getFullYear();
date.getDay();
date.getHours();
date.toISOString();


// DOM SELECTORS
getElementByTagName
getElementByClassName
getElementById
querySelector
querySelectorAll
getAttribute
setAttribute

// selecting elements for manipulation
const myTextInput= document.querySelector('myHeading'); // this is selector
const myTextInput= document.querySelectorAll('myHeading'); // this is selector  
const myTextInput= document.getElementById('#myHeading');  // this is id selector 
const myTextInput= document.getElementByClassName('.myHeading'); // this is class selector 
const myTextInput= document.getElementByTagName('myHeading'); // this is tag selector 




// traversing DOM
addEventListener()
removeEventListener() 
find()
closest ()
parent ()
parents ()
children ()
siblings ()
next ()
nextAll ()
prev ()
prevAll ()
innerHTML
classList.add('c')
classList.remove('c')
classList.toggle('c')
classList.contains('c')

.children 
.parentElement
.textContent
.childNodes()
.parentNode()
.cloneNode()
.append()
.prepend()
.remove()
.insertAdjacentHTML()
.querySelector()
.closest()
.matches()
.scrollIntoView()
.setProperty()
.setAttribute()

// add & filter elements 
.add ()
.filter ()
.find ()
.not () / not ()
.has () / has ()
contains ()


HTTP 
client
server
request
response
GET
POST
PUT
DELETE
//HTTP status code


// EVENTS IN WEBSITE
click
dbclick
mousedown
mouseup
mousemove
mouseover
mouseout
keydown
keyup
keypress
load
unload
error
resize
scroll
focus // focusin
blur // focusout 
input
change
submit
reset
cut
copy
paste
select


// browser      node
// window       global
// document     process
// history      module
// location     __filename
// navigator    require(./)


//node js commands 
// cls commmnad clear terminal
// const arg=process.argv
//console.log(argv) 
