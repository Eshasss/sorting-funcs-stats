import unittest
import random
from functions import bubblesort, merge, mergesort, quicksort, insertsort
from decorators import megadec
from classes import MyList
data = MyList([9, 3, 9, 2, 0, 6])
def bubblesort(data):
    print(data)
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
print(bubblesort(data))




# import random
# class Mylist(list):
#     def __init__(self, *data):
#         self.list = list(data)
#         self.read = 0
#         self.write = 0
    
#     def append(self, a):
#         self.list.append(a)
#         self.write +=1
#         return self.write
#     def insert(self, elem):
#         return f"urapobeda"
# b = Mylist(4,5,6,7)
# print(b)
# b.append(8)sds
# print(b)
# easy =  [9, 3, 9, 2, 0, 6]
# small = [random.randint(-100, 100) for _ in range(10000)]
# big = [random.randint(-100, 100) for _ in range(1000000)]
# ordered = sorted([random.randint(-100, 100) for _ in range(10000)])
# almostordered =  sorted([random.randint(-100, 100) for _ in range(100)]).append([random.randint(-100, 100) for _ in range(100)])
# # empty = []
# fullrandom = [random.randint(-100, 100) for _ in range(random.randint(0, 10000))]
# print(easy, small, big, ordered, reverse, almostordered, empty, fullrandom)
# def bubblesort(data:list) -> list:
#     n = len(data)
#     while True:
#         swapped = False
#         for i in range(1, n):
#             if data[i-1] > data[i]:
#                 data[i-1], data[i] = data[i], data[i-1]
#                 swapped = True
#         n -= 1
#         if not swapped:
#             break
#     return data
# print(bubblesort(small))
# k = list(reversed([0, 5,8, 35, 88, 88, 91, 92, 99, 100, 102, 432, 799, 876, 8888, 9371, 39271]))
# print(k)
# def bubblesort(data:list) -> list:
#     done = False
#     n = len(data)
#     if n == 0:
#         return data
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

# almost = [r for r in range(100)].extend()
# t = 
# almost.extend(t)
# print(almost)
# print(bubblesort(almost))
# import psutil
# import time
# start_time = time.time()
# process = psutil.Process()
# mem_before = process.memory_info().rss
# print("hello!")
# p = [random.randint(-100, 100) for _ in range(5000)]
# k = bubblesort(p)
# print("hello?")
# end_time = time.time()
# mem_after = process.memory_info().rss
# print(f"Функция запускалась {end_time - start_time:.5f} секунд \nФункция использовала {mem_after - mem_before} байтов памяти")

# print(MyList(random.randint(-100, 100) for _ in range(100)))