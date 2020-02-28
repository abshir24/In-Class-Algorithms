# Create a function that accepts a string input and returns a string with all 
# the blanks removed. Example: “S T R ” => “STR”

def removeSpaces(string):
    returnStr = ""

    for i in range(len(string)):
        if string[i] != " ":
            returnStr += string[i]
    return returnStr

print(removeSpaces("S T R"))


#Create a function that accepts a number of American cents, 
# compute and print how to represent that amount with smallest number of coins. 
# Common American coins are pennies (1 cent), nickels (5 cents), dimes (10 cents), 
# and quarters (25 cents). Hint: Use modulus operator.

def generateCoinChage(amount):
    # By using the int() method our answer will be rounded
    quarters = int(amount/25)
    amount = amount % 25
    dimes = int(amount/10)
    amount = amount % 10
    nickels = int(amount/5)
    amount = amount % 5
    pennies = amount
    print("Quarters: {}, Dimes: {}, Nickels {}, Pennies {}".format(quarters,dimes,nickels,pennies))


generateCoinChage(111)

# Create a function that accepts a list input. 
# Swap positions of successive pairs of values of given array. 
# If length is odd, do not change the final element. 
# For [1,2,3,4] , return [2,1,4,3] . For example, change input ["Brendan",true,42] to [true,"Brendan",42] . 
# As with all array challenges, do this without using any built-in array methods.


def swapPairs(arr):
    # We have to make sure that the array has at least 2 elements
    if len(arr) >= 2:
        for i in range(0,len(arr)-1,2):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    
    return arr

print(swapPairs([1,2,3,4,5]))