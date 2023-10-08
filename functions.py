from decorators import count, benchmark
import random
# from testing import 

# @count
# @benchmark(iters=5)
# def bubble_sort(data:list) -> list:
#     done = False
#     n = len(data)
#     while done != True:
#         count = 0
#         for i in range(1, n):
#             #print(i, i-1)
#             if data[i-1] > data[i]:
#                 data[i], data[i-1] = data[i-1], data[i]
#                 count += 1
#         if count == 0:
#             done = True
#     return data


def bubblesort(elements):
    swapped = False
    # Looping from size of array from last index[-1] to index [0]
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                swapped = True
                # swapping data if the element is less than next element in the array
                elements[i], elements[i + 1] = elements[i + 1], elements[i]        
        if not swapped:
            # exiting the function if we didn't make a single swap
            # meaning that the array is already sorted.
            return elements
# def insert_sort(data:list, n = 1, check_indx = 0) -> list:
#     n = len(data)-1
#     step_indx = check_indx + 1
#     num = data[step_indx]
#     if n > 0:
#         while data[check_indx] > num and check_indx >= 0:
#             data[check_indx+1] = data[check_indx]
#             check_indx -= 1
#         data[step_indx+1] = num
#         #insert_sort(data, n-1, check_indx)
        
    # return data

def merge(a,b):
    c = []
    n = 0
    k = 0
    f = 0
    while f != len(a) + len(b):
        if int(a[n]) >= int(b[k]):
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
def merge_sort(z):
    if len(z) == 1:
        return z
    mid = len(z)//2
    return (merge(merge_sort(z[0: mid]), merge_sort(z[mid: len(z)])))
    
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

  
# print(len([4,3,7,8,2,9,7,9]))
# print([4,3,7,8,2,9,7,9])
#print(bubblesort1([1,3,4,5,6]))
# #print(insert_sort([4,3,7,8,2,9,7,9]))
# print(merge_sort([random.randint(-100, 100) for _ in range(100)]))
# print(quick_sort([random.randint(-100, 100) for _ in range(100)]))

