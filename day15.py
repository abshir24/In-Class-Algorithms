# Given an array of values take all the values that are strings 
# and store then into a dictionary. Return that dictionary

def convertLi(arr):
    dictionary = {}
    for value in arr:
        if type(value) == str:
            dictionary[value] = value
    
    return dictionary

# Create a standalone function that accepts an input string, 
# removes leading and trailing white space (at beginning and end only), 
# capitalizes the first letter of every word, and return that string.

def removeSpaces(string):
    firstLetterIndex = 0
    lastLetterIndex = len(string) -1

    returnString = ""

    # Bypass all leading whitespaces
    while string[firstLetterIndex] == ' ':
        firstLetterIndex += 1


    # Bypass all trailing whitespaces
    while string[lastLetterIndex] == ' ':
        lastLetterIndex -= 1

    for i in range(firstLetterIndex, lastLetterIndex+1):
        if string[i-1] == ' ':
            # Capitalize the first letter of every word
            returnString += string[i].upper()
        else:
            returnString += string[i]

    return returnString
    

print(removeSpaces("        Whitspaces     are     cool        "))




    
        