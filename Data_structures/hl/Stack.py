from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        self.container.pop()

    def isEmpty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def peek(self):
        return self.container[-1]


s = Stack()
s.push(5)
print(s.peek())
