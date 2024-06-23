class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cnt = 0
        self.list_stack = []

    def is_empty(self):
        return not self.cnt

    def is_full(self):
        return self.cnt == self.capacity

    def pop(self):
        value = None
        if not self.is_empty():
            value = self.list_stack[self.cnt - 1]
            self.list_stack.pop(self.cnt - 1)
            self.cnt -= 1
        return value

    def push(self, value):
        if not self.is_full():
            self.list_stack.append(value)
            self.cnt += 1

    def top(self):
        if not self.is_empty():
            return self.list_stack[self.cnt - 1]


stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
