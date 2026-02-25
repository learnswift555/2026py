# 作者：柚子皮
# 2026年02月24日17时19分09秒
# yexixi2333@gmail.com
import random
import time
import sys
sys.setrecursionlimit(100000)

class Sort:
    def __init__(self, n):
        self.len = n
        self.arr = [0] * n
        self.random_data()

    def random_data(self):
        for i in range(self.len):
            self.arr[i] = random.randint(1, 100)

    def partition(self, left, right):
        pivot = self.arr[right]
        while left < right:
            while left < right and self.arr[left] <= pivot:
                left += 1
            self.arr[right] = self.arr[left]
            while left < right and self.arr[right] >= pivot:
                right -= 1
            self.arr[left] = self.arr[right]
        self.arr[left] = pivot
        return left

    def QuickSort(self, left, right):
        if left >= right:
            return
        pivot = self.partition(left, right)
        self.QuickSort(pivot + 1, right)
        self.QuickSort(left, pivot - 1)

    def adjust(self, pos, arr_len):
        """
        :param pos: 被调整的元素位置
        :param arr_len: 列表总长度
        :return:
        """
        arr = self.arr
        dad = pos
        son = dad * 2 + 1
        if son >= arr_len:
            return
        if son + 1 < arr_len and arr[son] < arr[son + 1]:
            son += 1
        if arr[son] > arr[dad]:
            arr[dad], arr[son] = arr[son], arr[dad]
            self.adjust(son, arr_len)

    def heap_sort(self):
        for i in range(self.len // 2 - 1, -1, -1):
            self.adjust(i, self.len)
        arr = self.arr
        arr[0], arr[-1] = arr[-1], arr[0]
        for i in range(self.len - 1, 0, -1):
            self.adjust(0, i)
            arr[0], arr[i - 1] = arr[i - 1], arr[0]

    def test_time_use(self, sort_func, *args, **kwargs):
        start = time.time()
        sort_func(*args, **kwargs)
        end = time.time()
        print(f'总计用时{end - start}')


if __name__ == '__main__':
    my_sort = Sort(10000)
    # print(my_sort.arr)
    # my_sort.QuickSort(0, 9)
    # my_sort.heap_sort()
    my_sort.test_time_use(my_sort.heap_sort)
    # my_sort.test_time_use(my_sort.QuickSort,left=0,right=9999)
    # print(my_sort.arr)



