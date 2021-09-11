# lst_queue = []
#
# lst_queue.insert(0, 12)
# lst_queue.insert(0, 22)
# lst_queue.insert(0, 33)
# lst_queue.pop()

# from collections import deque
#
# q = deque()
#
# q.appendleft(12)
# q.appendleft(52)
# q.appendleft(32)
#
# q.pop()
# print(q)


from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        self.buffer.pop()

    def isEmpty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


D = Queue()

D.enqueue(12)
D.enqueue(32)
D.enqueue(42)

print(D.buffer)

D.dequeue()
print(D.buffer)
