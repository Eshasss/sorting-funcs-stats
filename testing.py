import unittest
import random
from functions import bubblesort

class SortTester(unittest.TestCase):
    def test_random1(self):
        ARR_SIZE = 100
        arr = [random.randint(-100, 100) for _ in range(ARR_SIZE)]
        arr = sorted(arr)
        self.assertEqual(bubblesort(arr), sorted(arr))

    def test_random2(self):
        ARR_SIZE = 100000
        arr = [random.randint(-100, 100) for _ in range(ARR_SIZE)]
        arr = sorted(arr)
        self.assertEqual(bubblesort(arr), sorted(arr))
    
    def test_random3(self):
        ARR_SIZE = 1000000
        arr = [random.randint(-100, 100) for _ in range(ARR_SIZE)]
        arr = sorted(arr)
        self.assertEqual(bubblesort(arr), sorted(arr))
    
    
    def test_s(self):
        arr = [1,3,4,5,6]
        self.assertEqual(bubblesort(arr), sorted(arr))



#python -m unittest testing.py






# 1) Лёгкий случай, который можно проверить руками
# 2) Случайно сгенерированный массив небольшого размера (<10000)
# 3) Случайно сгенерированный массив большого размера (>100000)
# 4) Отсортированный массив
# 5) Почти отсортированный массив
# 6) Инвертированный отсортированный массив
# 7) Пустой массив
# 8) Массив случайной длины из случайных значений