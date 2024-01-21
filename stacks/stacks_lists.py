# push ------> append
# pop  ------> pop

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def __str__(self):
        return str(self.stack)
    

my_stack = Stack()

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print(my_stack)

my_stack.pop()
print(my_stack)

print(my_stack.peek())