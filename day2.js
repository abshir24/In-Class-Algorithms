//Print the product of all numbers from 1 to 5.
var product = 1;
for(let i = 1;i<=5;i++){
    product *= i
}

console.log(product)

//Given a restaurant bill of $125 (before taxes) 
//calculate the total amount of the bill 
//after 10% sales tax. Then print the bill before 
//tax and the bill after tax.

let billbeforetax = 125

let tax = billbeforetax * .1

let billaftertax = billbeforetax + tax

console.log("Bill before tax " + billbeforetax)

console.log("Bill after tax " + billaftertax)