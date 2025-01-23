class Solutions:
    def redundant_braces(self, data):
        stack = []
        for char in data:
            if char == ')':
                count = 0
                while stack and stack[-1] != '(':
                    top = stack.pop()
                    if top in "*/-+":
                        count += 1
                if stack:
                    stack.pop()
                if count == 0:
                    return 1
            else:
                stack.append(char)
        return 0


output = Solutions()
output.redundant_braces('(((a+b))+(a+b))')
