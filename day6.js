// Create a function that accepts an array of numbers and a number Y as a parameters. 
//Return a count of all of the numbers that are greater than Y. 
//Example (Given [1,2,3,4,5] and 2  return 3. In this case 2 will be our Y)

function countGreater(arr,y){
    let count = 0

    for(let i = 0 ;i<arr.length;i++){
        if(arr[i]>y){
            count++
        }
    }

    return count
}

console.log(countGreater([1,2,3,4,5],2))

// Given an array of numbers replace all negative values with the string “SkillSpire”. 
//Example (Given [1,-2,3,-4,5] return [1,”SkillSpire”,3,”SkillSpire,5)

function replaceNegatives(arr){
    for(let i = 0 ;i<arr.length;i++){
        if(arr[i]<0){
            arr[i] = "SkillSpire"
        }
    }

    return arr
}

console.log(replaceNegatives([1,-2,3,-4,5]))


//Given an array of numbers square all values in the Array. 
//Example (Given [1,2,3,4,5] return [1,4,9,16,25])

function squareValues(arr){
    for(let i = 0 ;i<arr.length;i++){
        arr[i] = arr[i] * arr[i]
    }

    return arr
}

console.log(squareValues([1,2,3,4,5]))

