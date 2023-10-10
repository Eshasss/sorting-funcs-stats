import random
from functions import mergesort, merge
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

def bubblesort(data:list) -> list:
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

almost = [r for r in range(100)].extend([random.randint(0, 100) for _ in range(100)])
# t = 
# almost.extend(t)
print(almost)
print(bubblesort(almost))
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