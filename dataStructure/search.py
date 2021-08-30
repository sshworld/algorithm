    # Membership Operators.
    # Linear Search.
    # Binary Search.
    # Jump Search.
    # Fibonacci Search.
    # Exponential Search.
    # Interpolation Search.

def linearSearch(arr, target) :
    i = 0
    while i < len(arr) : 
        if arr[i] == target :
            return i
        i += 1
    return "Fail"

def binarySearch(arr, target) :
    arr.sort()
    length = len(arr)

    left = 0
    right = length - 1

    while left <= right :
        mid = (left + right) // 2
        if arr[mid] == target :
            return mid + 1
        elif arr[mid] > target :
            right = mid - 1
        else :
            left = mid + 1

    return "Fail"

def jumpSearch(arr, target) :
    import math
    
    arr.sort()
    length = len(arr)
    interval = int(float(math.sqrt(length)))

    for i in range(0, length, interval) :
        if arr[i] == target :
            return i
        elif arr[i] > target :
            ret = linearSearch(arr[i-interval:i], target)
            return ret + i if ret != "Fail" else ret

    return "Fail"





if __name__ == '__main__' :
    arr = [30, 94, 27, 92, 21, 37, 25, 47, 53, 98, 19, 32, 7]
    target = 25
    # print(linearSearch(arr, target))
    # print(binarySearch(arr, target))
    print(jumpSearch(arr, target))