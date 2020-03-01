# Given a sorted array and a value, return whether the array contains that value. 
# Do not sequentially iterate the array. Instead, ‘divide and conquer’, taking advantage 
# of the fact that the array is sorted . As always, only use built-in functions that 
# you are prepared to recreate (write yourself) on demand!

def binarySearch(arr,val):
    start = 0
    end = len(arr)-1
    # using the int function allows the number to be turned from a decimal to 
    # a whole number

    while start <= end:
        # find the mid point between the start and end pointers
        mid = int((start + end)/2)
        
        if arr[mid] == val:
            return True
        else:
            if arr[mid] > val:
                end = mid-1
            else:
                start = mid+1        

    return False

# test case
print(binarySearch([1,2,3,4,5],1))


# Given an array, return a dictionary containing the array’s max, 
# min and average values.

def arrayToDictionary(arr):
    dictionary = {}

    dictionary["max"] = max(arr)
    dictionary["min"] = min(arr)
    dictionary["average"] = sum(arr)/2

    return dictionary


# Given an array of values take all the values that are strings and store then into a dictionary. 
# Return that dictionary

def placeStringsInDictionary(arr):
    dictionary = {}

    for i in range(len(arr)):
        if type(arr[i]) is str:
            dictionary[arr[i]] = arr[i]

    return dictionary


print(placeStringsInDictionary(["1",2,"3",4,"5"]))
