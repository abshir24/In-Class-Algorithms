//max average function

function data(num1,num2,num3){
    var max = num1;
    var avg;

    if(num2>max){
        max = num2 
    }

    if(num3>max){
        max = num3
    }
    
    console.log("The maximum number is " + max)

    var avg = (num1+num2+num3)/3

    console.log("The average number is " + ((num1+num2+num3)/3))
}

data(2,1,3)

//reversed string algorithm
function reverse(string){
    var reversed = ""

    for(let i = string.length;i>=0;i--){
        newString += string[i]
    }

    return reversed
}

