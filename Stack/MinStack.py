class Solutions:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, item):
        self.stack.append(item)
        if not self.min:
            self.min.append(item)
            return
        min_value = self.min[-1]
        if min_value > item:
            self.min.append(item)
        else:
            self.min.append(min_value)

    def pop(self):
        if self.stack:
            self.min.pop()
            return self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return -1

    def get_min(self):
        if self.stack:
            return self.min[-1]
        return -1


data = Solutions()
data.push(6)
data.push(2)
data.push(1)
data.push(0)
data.push(3)
data.pop()
data.pop()
data.pop()
print(data.get_min())
