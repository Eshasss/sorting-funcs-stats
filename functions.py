import random
from classes import MyList
from decorators import megadec, megarec
@megadec
def bubblesort(data):
    done = False
    n = len(data)
    if n == 0:
        return data
    while done != True:
        count = 0
        for i in range(1, n):
            if data[i-1] > data[i]:
                data[i], data[i-1] = data[i-1], data[i]
                count += 1
        if count == 0:
            done = True
    return data

@megadec
def insertsort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def merge(a,b):
    c = MyList([])
    n = 0
    k = 0
    f = 0
    while f != len(a) + len(b):
        if a[n] >= b[k]:
            c.append(b[k])
            k += 1
            f += 1
        else:
            c.append(a[n])
            n += 1
            f += 1
        if n == len(a):
            c = c + b[k:len(b)]
            f = len(a) + len(b)
        elif k == len(b):
            c = c+ a[n:len(a)]
            f = len(a) + len(b)
    return (c)
@megarec
def mergesort(z):
    if len(z) == 1:
        return z
    mid = len(z)//2
    return (MyList(merge(MyList(mergesort(MyList(z[0: mid]))), MyList(mergesort(MyList(z[mid: len(z)]))))))

@megarec
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        left = MyList([])
        right = MyList([])
        pivot = 0
        for i in range(len(arr)):
            if i != pivot:
                if arr[i] <= arr[pivot]:
                    left.append(arr[i])
                else:
                    right.append(arr[i])
        left = quicksort(left)
        right = quicksort(right)
        res = MyList([])
        for elem in left:
            res.append(elem)
        res.append(arr[pivot])
        for elem in right:
            res.append(elem)
        return res

def heapify(data, count, root):
    largest = root
    left_child = 2 * root + 1
    right_child = 2 * root + 2
    if left_child < count and data[left_child] > data[largest]:
        largest = left_child
    if right_child < count and data[right_child] > data[largest]:
        largest = right_child
    if largest != root:
        data[root], data[largest] = data[largest], data[root]
        heapify(data, count, largest)
@megadec
def heapsort(data):
    length = len(data)
    for i in range(length // 2 - 1, -1, -1):
        heapify(data, length, i)
    for i in range(length - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)
    return data
