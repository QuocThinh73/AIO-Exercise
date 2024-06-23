class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__list_queue = []
        self.__cnt = 0

    def is_empty(self):
        return not self.__cnt

    def is_full(self):
        return self.__cnt == self.__capacity

    def dequeue(self):
        value = None
        if not self.is_empty():
            value = self.__list_queue[0]
            self.__list_queue.pop(0)
            self.__cnt -= 1
        return value

    def enqueue(self, value):
        if not self.is_full():
            self.__list_queue.append(value)
            self.__cnt += 1

    def front(self):
        if not self.is_empty():
            return self.__list_queue[0]


queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())
