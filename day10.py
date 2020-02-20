# Create a function that accepts a string and returns a 
# Boolean based on if the string is a palindrome. 
# Example(“Car”=> False, “mom” => True)


def isPalindrome(string):
    start = 0
    end = len(string)-1

    while start <= end:
        if(string[start] != string[end]):
            return False
        else:
            start+=1
            end-=1
    
    return True



# Create a function that accepts a list input and returns that list with all its 
# values reversed. This does not need to be done in-place. 
# But the most optimal solution is in-place. 
# Example(Given:[1,2,3,4,5]=>[5,4,3,2,1])

def reverseList(numlist):
    start = 0
    end = len(numlist)-1

    while start <= end:
        temp = numlist[start]
        numlist[start] = numlist[end]
        numlist[end] = temp
        start+=1
        end-=1

    return numlist

print(reverseList([1,2,3,4,5]))
