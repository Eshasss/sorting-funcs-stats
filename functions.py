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
@megadec
def mergesort(z):
    if len(z) == 1:
        return z
    mid = len(z)//2
    return (MyList(merge(MyList(mergesort(MyList(z[0: mid]))), MyList(mergesort(MyList(z[mid: len(z)]))))))

def quicksort(arr: MyList) -> MyList:
    print(arr)
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
        return arr
# data = MyList([random.randint(-100, 100) for _ in range(100)])
# print(quicksort(data))
# @megarec
# def qfunc(arr):
#     return quicksort(arr)
# data = MyList([random.randint(-100, 100) for _ in range(100)])
# print(qfunc(data))
# def heapify(arr, n, ):
#     for i in range(n//2 - 1, -1, -1):
#         root = i
#         left = 2 * i + 1
#         right = 2 * i + 2
#         if left < n and arr[left] <= arr[root]:
#             root = left
#         if right < n and arr[right] <= arr[root]:
#             root = right
        
#         heapify(arr, root, i)
# def heapsort(arr):
#     n = len(arr)
#     heapify(arr)
#     i = n - 1
#     while i > 0:
#         heapify(arr, i, 0)
#         i -= 1
# def qfunc(data):
#     result = quicksort(data)
#     return result
# data = MyList([random.randint(-100, 100) for _ in range(100)])
# data1 = MyList([random.randint(-100, 100) for _ in range(100)])
# print(quicksort(data))
# quicksort(data)
# print(heapsort(data))