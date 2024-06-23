class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__cnt = 0
        self.__list_stack = []

    def is_empty(self):
        return not self.__cnt

    def is_full(self):
        return self.__cnt == self.__capacity

    def pop(self):
        value = None
        if not self.is_empty():
            value = self.__list_stack[self.__cnt - 1]
            self.__list_stack.pop(self.__cnt - 1)
            self.__cnt -= 1
        return value

    def push(self, value):
        if not self.is_full():
            self.__list_stack.append(value)
            self.__cnt += 1

    def top(self):
        if not self.is_empty():
            return self.__list_stack[self.__cnt - 1]


stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
