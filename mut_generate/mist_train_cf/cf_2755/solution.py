"""
QUESTION:
Create a function `findPrimeNumbers` that takes a range of numbers defined by a starting number and an ending number as input. The function should check each number in the range to determine if it's a prime number and store the prime numbers in a doubly linked list. Finally, it should return the prime numbers in the list in reverse order. The function should also handle the case where no prime numbers are found within the given range and return an error message in that case. The input range is defined by two positive integers where the starting number is less than or equal to the ending number.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def remove_last(self):
        if self.tail is None:
            return None
        value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return value

    def is_empty(self):
        return self.head is None


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_prime_numbers(start, end):
    primes = DoublyLinkedList()
    for i in range(start, end + 1):
        if is_prime(i):
            primes.add(i)
    if primes.is_empty():
        return "No prime numbers found within the given range."
    else:
        output = []
        while not primes.is_empty():
            output.append(primes.remove_last())
        return output