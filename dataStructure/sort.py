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
        for j in range(1, 1+i) :
            if x[j] > x[maxNum] :
                maxNum = j
        swap(x, maxNum, i)
    print(time.time() - start)
    return x

def insertSort(x) :
    start = time.time()
    for i in range(1, len(x)) :
        num = x[i]
        j = i
        while j > 0 and x[j-1] > num :
            x[j] = x[j-1]
            j -= 1
        x[j] = num
    print(time.time() - start)
    return x

def shellSort(x) :
    start = time.time()
    gap = len(x) // 2

    while gap > 0 :
        for i in range(gap) :
            gapInsertionSort(x, i, gap)
        gap = gap // 2
    print(time.time() - start)
    return x


def gapInsertionSort(x, i , gap) :
    for num in range(i + gap, len(x), gap) :
        val = x[num]
        targetNum = num
        while targetNum > i :
            if x[targetNum - gap] > val :
                x[targetNum] = x[targetNum - gap]
            else :
                break
            targetNum -= gap
        x[targetNum] = val

def mergeSort(x) :
    if len(x) > 1 :
        mid = len(x) // 2
        lx, rx = x[:mid], x[mid:]
        mergeSort(lx)
        mergeSort(rx)
    
        li, ri, i = 0, 0, 0
        while li < len(lx) and ri < len(rx) :
            if lx[li] < rx[ri] :
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1
            i += 1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]
    print(x)
    return(x)

def pivotFirst(x, lmark, rmark):
    pivot_val = x[lmark]
    pivot_idx = lmark
    while lmark <= rmark:
        while lmark <= rmark and x[lmark] <= pivot_val:
            lmark += 1
        while lmark <= rmark and x[rmark] >= pivot_val:
            rmark -= 1
        if lmark <= rmark:
            swap(x, lmark, rmark)
            lmark += 1
            rmark -= 1
    swap(x, pivot_idx, rmark)
    return rmark

def quickSort(x, pivotMethod=pivotFirst):
    def _qsort(x, first, last):
        if first < last:
            splitpoint = pivotMethod(x, first, last)
            _qsort(x, first, splitpoint-1)
            _qsort(x, splitpoint+1, last)
    _qsort(x, 0, len(x)-1)
    return x

if __name__ == '__main__' :
    # x = [10, 8, 6, 20, 4, 3, 22, 1, 0, 15, 16]
    x = [21, 10, 12, 20, 25, 13, 15, 22]
    # print(bubbleSort(x))
    # print(selectionSort(x))
    # print(insertSort(x))
    # print(shellSort(x))
    print(mergeSort(x))
    # print(quickSort(x))
