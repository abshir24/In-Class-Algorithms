def printNum(dictionary,arr):
    # value = sum(arr) - sum(dictionary)

    # return value

    for num in arr:
        if num not in dictionary:
            return num

    return "All numbers are accounted for"   

print(printNum({1:1,3:3},[1,2,3]))

arr = [1,2,3,4,5,1] 

def modeNum(arr):
    dictionary = {}

    for num in arr:
        if num not in dictionary:
            dictionary[num] = 0
        else:
            dictionary[num] += 1
    
    return max(dictionary.values())


print(modeNum(arr))
