import unittest
import random
from functions import bubblesort, merge, mergesort, quicksort, insertsort
from decorators import megadec
from classes import MyList
#python -m unittest testing.pyj
class SortTester(unittest.TestCase):
    def setUp(self):
        self.easy = MyList([9, 3, 9, 2, 0, 6])
        self.small = MyList([random.randint(-100, 100) for _ in range(10000)])
        self.big = [random.randint(-100, 100) for _ in range(100000)]
        self.ordered = [i for i in range(10000)]
        self.revers = [k for k in range(10000, 0, -1)]
        self.almost = [r for r in range(100)]
        l2 = [random.randint(-100, 100) for t in range(100)]
        self.almost.extend(l2)
        self.empty = []
        self.fullrandom = [random.randint(-100, 100) for _ in range(random.randint(0, 10000))]

    @megadec
    def test_1bubblesort_easy(self):
        self.assertEqual(bubblesort(self.easy), sorted(self.easy))

    # @megadec
    # def test_2bubblesort_small(self):
    #     self.assertEqual(bubblesort(self.small), sorted(self.small))

    # @megadec
    # def test_3bubblesort_big(self):
    #     self.assertEqual(bubblesort(self.big), sorted(self.big))

    # @megadec
    # def test_4bubblesort_ordered(self):
    #     self.assertEqual(bubblesort(self.ordered), self.ordered)

    # @megadec
    # def test_5bubblesort_reversed(self):
    #     self.assertEqual(bubblesort(self.revers), sorted(self.revers))

    # @megadec
    # def test_6bubblesort_almost(self):
    #     self.assertEqual(bubblesort(self.almost), sorted(self.almost))
    
    # @megadec
    # def test_7bubblesort_empty(self):
    #     self.assertEqual(bubblesort(self.empty), self.empty)
    
    # @megadec
    # def test_8bubblesort_random(self):
    #     self.assertEqual(bubblesort(self.fullrandom), sorted(self.fullrandom))
    
    # @megadec
    # def test_1quicksort_easy(self):
    #     self.assertEqual(quicksort(self.easy), sorted(self.easy))
    
    # @megadec
    # def test_2quicksort_small(self):
    #     self.assertEqual(quicksort(self.small), sorted(self.small))
    
    # @megadec
    # def test_3quicksort_big(self):
    #     self.assertEqual(quicksort(self.big), sorted(self.big))
    
    # @megadec
    # def test_4quicksort_ordered(self):
    #     self.assertEqual(quicksort(self.ordered), self.ordered)
    
    # @megadec
    # def test_5quicksort_revers(self):
    #     self.assertEqual(quicksort(self.revers), sorted(self.revers))
    
    # @megadec
    # def test_6quicksort_almost(self):
    #     self.assertEqual(quicksort(self.almost), sorted(self.almost))
    
    # @megadec
    # def test_7quicksort_empty(self):
    #     self.assertEqual(quicksort(self.empty), self.empty)
    
    # @megadec
    # def test_8quicksort_fullrandom(self):
    #     self.assertEqual(quicksort(self.fullrandom), sorted(self.fullrandom))
    
    # @megadec
    # def test_1mergesort_easy(self):
    #     self.assertEqual(mergesort(self.easy), sorted(self.easy))

    # @megadec
    # def test_2mergesort_small(self):
    #     self.assertEqual(mergesort(self.small), sorted(self.small))

    # @megadec
    # def test_3mergesort_big(self):
    #     self.assertEqual(mergesort(self.big), sorted(self.big))
        
    # @megadec
    # def test_4mergesort_ordered(self):
    #     self.assertEqual(mergesort(self.ordered), self.ordered)
    
    # @megadec
    # def test_5mergesort_revers(self):
    #     self.assertEqual(mergesort(self.revers), sorted(self.revers))

    # @megadec
    # def test_6mergesort_almost(self):
    #     self.assertEqual(mergesort(self.almost), sorted(self.almost))
    
    # @megadec
    # def test_7mergesort_empty(self):
    #     self.assertEqual(mergesort(self.empty), self.empty)
    
    # @megadec
    # def test_8mergesort_fullrandom(self):
    #     self.assertEqual(mergesort(self.fullrandom), sorted(self.fullrandom))
    
    # @megadec
    # def test_2insertsort_easy(self):
    #     self.assertEqual(insertsort(self.easy), sorted(self.easy))
    
    # @megadec
    # def test_3insertsort_small(self):
    #     self.assertEqual(insertsort(self.small), sorted(self.small))

    # @megadec
    # def test_1insertsort_big(self):
    #     self.assertEqual(insertsort(self.big), sorted(self.big))

    # @megadec
    # def test_4insertsort_ordered(self):
    #     self.assertEqual(insertsort(self.ordered), self.ordered)
    
    # @megadec
    # def test_5insertsort_revers(self):
    #     self.assertEqual(insertsort(self.revers), sorted(self.revers))

    # @megadec
    # def test_6insertsort_almost(self):
    #     self.assertEqual(insertsort(self.almost), sorted(self.almost))
    
    # @megadec
    # def test_7insertsort_empty(self):
    #     self.assertEqual(insertsort(self.empty), self.empty)
    
    # @megadec
    # def test_8insertsort_fullrandom(self):
    #     self.assertEqual(insertsort(self.fullrandom), sorted(self.fullrandom))

        


# 1) Лёгкий случай, который можно проверить руками
# 2) Случайно сгенерированный массив небольшого размера (<10000)
# 3) Случайно сгенерированный массив большого размера (>100000)
# 4) Отсортированный массив
# 5) Почти отсортированный массив
# 6) Инвертированный отсортированный массив
# 7) Пустой массив
# 8) Массив случайной длины из случайных значений
