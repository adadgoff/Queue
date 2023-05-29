class Queue:
    def __init__(self):
        self._size = 0
        self._capacity = 10
        self._array = [None] * self._capacity
        self._head = self._capacity // 3
        self._tail = self._capacity // 3

    def front(self):
        return self._array[self._head]

    def back(self):
        return self._array[self._tail - 1]

    def pop_front(self):
        self._head = (self._head + 1) % self._capacity
        self._size -= 1

    def push_back(self, value):
        if self._size == self._capacity:
            self._array = [None] * (self._capacity // 2) + self._array[self._head:] + self._array[:self._head] + [None] * (self._capacity // 2)
            self._head = self._capacity // 2
            self._tail = self._capacity + self._capacity // 2
            self._capacity = self._capacity * 2
        self._array[self._tail] = value
        self._tail = (self._tail + 1) % self._capacity
        self._size += 1

    def size(self):
        return self._size
