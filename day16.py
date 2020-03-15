# Given an array of integers return the SAME array
# with all duplicate values removed


def removeDupes(arr):
    dictionary = {}
    for value in arr:
        # If the value doesn't exist in the dictionary then add it
        if value not in dictionary: 
            dictionary[value] = value
        else:
            # if it does exist in the dictionary then this means that
            # we have a duplicate value and we need to remove that value
            arr.remove(value) 
        
    return arr




def fib(stop):
    a = 0
    b = 1
    print(a)
    print(b)
    stop-=2
    while stop>0:
        c = a+b
        print(c)
        a = b
        b = c 
        stop -= 1
    
    return

fib(7)