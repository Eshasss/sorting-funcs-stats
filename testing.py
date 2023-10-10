import unittest
import random
from functions import bubblesort, merge, mergesort, quicksort
from decorators import megadec
#python -m unittest testing.py
class SortTester(unittest.TestCase):
    #@classmethod
    def setUp(self):
        self.easy = [9, 3, 9, 2, 0, 6]
        self.small = [random.randint(-100, 100) for _ in range(10000)]
        self.big = [random.randint(-100, 100) for _ in range(100000)]
        self.ordered = [i for i in range(1000)]
        self.revers = [k for k in range(1000, 0, -1)]
        self.almost = [r for r in range(100)]
        l2 = [random.randint(-100, 100) for t in range(1000)]
        self.almost.extend(l2)
        self.empty = []
        self.fullrandom = [random.randint(-100, 100) for _ in range(random.randint(0, 1000))]

    @megadec
    def test_bubblesort_easy(self):
        #print(self.big)
        self.assertEqual(bubblesort(self.easy), sorted(self.easy))

    @megadec
    def test_bubblesort_small(self):
        self.assertEqual(bubblesort(self.small), sorted(self.small))

    @megadec
    def test_bubblesort_big(self):
        self.assertEqual(bubblesort(self.big), sorted(self.big))

    @megadec
    def test_bubblesort_ordered(self):
        self.assertEqual(bubblesort(self.ordered), self.ordered)

    @megadec
    def test_bubblesort_reversed(self):
        self.assertEqual(bubblesort(self.revers), sorted(self.revers))

    @megadec
    def test_bubblesort_almost(self):
        self.assertEqual(bubblesort(self.almost), sorted(self.almost))
    
    @megadec
    def test_bubblesort_empty(self):
        self.assertEqual(bubblesort(self.empty), self.empty)
    
    @megadec
    def test_bubblesort_random(self):
        self.assertEqual(bubblesort(self.fullrandom), sorted(self.fullrandom))

    # def test_quicksort(self):
    #     self.assertEqual(quicksort(self.easy), sorted(self.easy))
        # self.assertEqual(quicksort(self.small), sorted(self.small))
        # self.assertEqual(quicksort(self.big), sorted(self.big))
        # self.assertEqual(quicksort(self.ordered), self.ordered)
        # self.assertEqual(quicksort(self.reverse), self.ordered)
        # self.assertEqual(quicksort(self.almostordered), sorted(self.almostordered))
        # self.assertEqual(quicksort(self.empty), self.empty)
        # self.assertEqual(quicksort(self.fullrandom), sorted(self.fullrandom))
    # @megadec
    # def test_mergesort(self):
    #     self.assertEqual(mergesort(self.big), sorted(self.big))
        #self.assertEqual(mergesort(self.easy), sorted(self.easy))
        #self.assertEqual(mergesort(self.small), sorted(self.small))
        
        # self.assertEqual(mergesort(self.ordered), self.ordered)
        # self.assertEqual(mergesort(self.reverse), self.ordered)
        # self.assertEqual(mergesort(self.almostordered), sorted(self.almostordered))
        # self.assertEqual(mergesort(self.empty), self.empty)
        # self.assertEqual(mergesort(self.fullrandom), sorted(self.fullrandom))        
    # @megadec
    # def test_mergesort1(self):
    #     self.assertEqual(mergesort(self.small), sorted(self.small))

        


# 1) Лёгкий случай, который можно проверить руками
# 2) Случайно сгенерированный массив небольшого размера (<10000)
# 3) Случайно сгенерированный массив большого размера (>100000)
# 4) Отсортированный массив
# 5) Почти отсортированный массив
# 6) Инвертированный отсортированный массив
# 7) Пустой массив
# 8) Массив случайной длины из случайных значений