"""
QUESTION:
Implement a function named `median` that calculates the median of a list of numbers without using built-in sorting functions or sorting algorithms. The function should be able to handle lists with an even or odd number of prime numbers, duplicates, negative numbers, and fractional numbers. The function should also accept a custom comparison function `cmp_func` for comparisons. The function should return the median of the input list.
"""

class Heap:
    def __init__(self, cmp_func):
        self.list = []
        self.cmp_func = cmp_func
    def push(self, value):
        self.list.append(value)
        self.heapify_up(len(self.list) - 1)
    def pop(self):
        value = self.list[0]
        self.list[0] = self.list[len(self.list) - 1]
        self.list.pop()
        self.heapify_down(0)
        return value
    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.cmp_func(self.list[index], self.list[parent]) < 0:
                self.list[parent], self.list[index] = self.list[index], self.list[parent]
                index = parent
            else:
                break
    def heapify_down(self, index):
        while index < len(self.list):
            left = index * 2 + 1
            right = index * 2 + 2
            smallest = index
            if left < len(self.list) and self.cmp_func(self.list[smallest], self.list[left]) > 0:
                smallest = left
            if right < len(self.list) and self.cmp_func(self.list[smallest], self.list[right]) > 0:
                smallest = right
            if smallest != index:
                self.list[smallest], self.list[index] = self.list[index], self.list[smallest]
                index = smallest
            else:
                break

def median(numbers, cmp_func):
    min_heap = Heap(cmp_func)
    max_heap = Heap(lambda a, b: -cmp_func(a, b))
    for num in numbers:
        if len(max_heap.list) == 0 or cmp_func(num, max_heap.list[0]) < 0:
            max_heap.push(num)
        else:
            min_heap.push(num)
        if len(min_heap.list) > len(max_heap.list):
            max_heap.push(min_heap.pop())
        elif len(max_heap.list) > len(min_heap.list) + 1:
            min_heap.push(max_heap.pop())
    if len(numbers) % 2 == 0:
        return (min_heap.list[0] + max_heap.list[0]) / 2
    else:
        return max_heap.list[0]