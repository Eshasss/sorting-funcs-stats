import random

def bubblesort(data):
    done = False
    n = len(data)
    if n == 0:
        return data
    while done != True:
        count = 0
        for i in range(1, n):
            #print(i, i-1)
            if data[i-1] > data[i]:
                data[i], data[i-1] = data[i-1], data[i]
                count += 1
        if count == 0:
            done = True
    return data

def insertsort(data:list) -> list:
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def merge(a,b):
    c = []
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

def mergesort(z):
    if len(z) == 1:
        return z
    mid = len(z)//2
    return (merge(mergesort(z[0: mid]), mergesort(z[mid: len(z)])))


def quicksort(arr: list):
    if len(arr) <= 1:
        return arr
    else:
        left = []
        right = []
        pivot = 0
        for i in range(len(arr)):
            if i != pivot:
                if arr[i] <= arr[pivot]:
                    left.append(arr[i])
                else:
                    right.append(arr[i])
        left = quicksort(left)
        right = quicksort(right)
        res = []
        for elem in left:
            res.append(elem)
        res.append(arr[pivot])
        for elem in right:
            res.append(elem)
        return res
