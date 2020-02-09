//Given an array of numbers calculate the sum of all the numbers in that array. 
//Example (Given [1,2,3,4,5] return 15)


function sum(arr){
    let sum = 0

    for(let i = 0;i<arr.length;i++){
        sum += arr[i]
    }
    return sum
}

console.log(sum([1,2,3,4,5]))


//Given an UNSORTED array of numbers find the max, min and range of the numbers. 
//Example (Given [3,1,2,5,4] Max = 5 Min = 1 range = 4)

function mathOperations(arr){
    let max = arr[0],min=arr[0]

    for(let i = 0;i<arr.length;i++){
        if(arr[i]>max){
            max = arr[i]
        }
        if(arr[i]<min){
            min = arr[i]
        }
    }

    console.log("MAX = " + max)

    console.log("Min = " + min)

    console.log("Range = " + (max-min))
}

mathOperations([3,1,2,5,4])

//Given a shape and dimensions return the area of that shape. 
//Example (Given “Square”, 4, 10 return 40). 
//This algorithm will only focus on rectangles and triangles. 
//Area of triangle = (1/2 Base * Height). Area of rectangle = (Base * Height).

function areaShape(shape,base,height){
    if(shape.toLowerCase() == "square"){
        return base*height
    }
    else if(shape.toLowerCase() == "triangle"){
        return (1/2)*(base)*(height)
    }
    else{
        return "Not a valid shape"
    }
}

console.log(areaShape("triangle",2,2))