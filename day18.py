# Given an array of strings remove all EVEN length strings from the array. 
# To remove from an array in python would look something like arr.remove(value). 

def removeEven(arr):
    for string in arr:
        if len(string) % 2 == 0:
            arr.remove(string)
    
    return arr

# Given a string remove all empty space characters 
# from that string and return the new string. 
# Example “S T R I N G” => “STRING”

def removeWhiteSpace(string):
    returnString = ""

    for i in range(len(string)):
        if string[i] != ' ':
            returnString += string[i]

    return returnString


# Given an array and a value add the given value to the front of the array. 
# Example: [2,3,4,5],1 => [1,2,3,4,5]

def addFront(arr,val):
    return [val] + arr








