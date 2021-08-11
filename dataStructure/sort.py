import time

def swap(x, i, j) :
    x[i], x[j] = x[j], x[i]

def bubbleSort(x) :
    start = time.time()
    for i in reversed(range(len(x))) :
        for j in range(i) :
            if x[j] > x[j+1] :
                swap(x, j, j+1)

    # for i in reversed(range(len(x))) :
    #     temp = x[:i+1]
    #     maxNum = max(temp)
    #     swap(x, temp.index(maxNum), i)
    print(time.time() - start)
    return x

def selectionSort(x) :
    start = time.time()
    for i in reversed(range(len(x))) :
        maxNum = 0
        for j in range(i) :
            if x[j] > x[maxNum] :
                maxNum = j
        swap(x, maxNum, j)
    print(time.time() - start)
    return x

def insertSort(x) :
    pass



if __name__ == '__main__' :
    x = [7, 1, 6, 2, 4, 3, 9, 10, 5]
    print(bubbleSort(x))
    print(selectionSort(x))
