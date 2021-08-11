
def func1(n) :

    sum = 0

    for i in range(1, n+1) :
        if i % 3 == 0 or i % 5 == 0 :
            sum += i

    return sum

def func2(arr, n) :

    for i in range(n-1) :
        for j in range(i+1, n) :
            if arr[i] + arr[j] == 100 :
                return 1

    return 0

def func3(n) :

    count = 1

    while(True) :

        sqare = count * count

        if sqare == n :
            return 1
        elif sqare > n :
            return 0

        count += 1



print(func3(9))
print(func3(693953651))
print(func3(756580036))