//Given a string return the number of parenthesis in the string. 
//(Example: Given “(Test)” return 2)
function countParens(string){
    var count = 0
    for(let i = 0;i<string.length;i++){
        if(string[i] == "(" || string[i] == ")" ){
            count++
        }
    }
    return count
}

//Given a string input return true or false if the parenthesis in the string are valid.
// Meaning check to see if all opening and closing parenthesis match. 
//(Example: Given string “(Valid)” this would return true. Given string ”(Invalid)” 
//return false.)

function parensValid(string){
    var parensCheck = 0;

    for(let i = 0; i<string.length;i++){
        if(string[i] == "("){
            parensCheck++
        }
        if(string[i] == ")"){
            parensCheck--;
        }
    }

    //if parensCheck = 0 then it will return true. If not it will return false
    return (parensCheck == 0)
}