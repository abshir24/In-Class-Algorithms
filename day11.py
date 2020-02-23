# Create a function that accepts a list input and shifts all the values 
# in the list to the left by 1. Then set the last value in the list equal 
# to zero this must be done in place. Given: [1,2,3,4,5] => [2,3,4,5,0]

def shiftLeft(arr):
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    
    arr[len(arr)-1] = 0
    return arr

print(shiftLeft([1,2,3,4,5]))


#Create a function that accepts a list and returns the element that is 
# N-from-array’s-end. Given ([5,2,3,6,4,9,7],3) , return 4 . 
# If the array is too short, return null .

def nthAway(arr,n):
    if len(arr) < n:
        return None

    return arr[len(arr)-n]

print(nthAway([1,2,3,4,5],4))

# Create a function that accepts a list input. Move the lowest element to array’s front, 
# shifting backward any elements previously ahead of it. Do not otherwise change the 
# array’s order. [3,4,1,2,5] => [1,3,4,2,5]

def moveMin(arr):
    # this line of code locates and stores the minimum index of an array 
    minIndex = arr.index(min(arr))

    for i in range(minIndex,0,-1):
        temp = arr[i]
        arr[i] = arr[i-1]
        arr[i-1]=temp
    
    return arr

print(moveMin([2,4,1,3,5]))


