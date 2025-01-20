from collections import deque

stack = deque()

print(dir(stack))

stack.append(1)
stack.append(4)
print(stack)
stack.pop()
count = stack.count(2)
print(stack)