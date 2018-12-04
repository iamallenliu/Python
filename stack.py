class mystack:
    def __init__(self, stack, top, size):
        self.stack = stack
        self.top = top
        self.size = size

    def isFull(self):
        if self.top == self.size:
            return True

    def isEmpty(self):
        if self.top == 0:
            return True

    def pop(self):
        if self.isEmpty() != True:
            self.stack[self.top-1] = ""
            self.top = self.top - 1
            print(self.stack)
        else:
            print("Stack is empty.")

    def peek(self):
        print(self.stack[self.top-1])

    def push(self, item):
        if self.isFull() != True:
            self.stack[self.top] = item
            self.top = self.top + 1
            print(self.stack)
        else:
            print("Stack is full.")


stack = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
stack = mystack(stack, len(stack), 5)

print(stack.stack)

print(stack.stack[1])
