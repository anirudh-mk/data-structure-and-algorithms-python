class Solutions:

    def valid_parenthesis(self, data):
        stack = []
        parenthesis_dict = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for parenthesis in data:
            if parenthesis in ['(', '[', '{']:
                stack.append(parenthesis)
            else:
                if stack:
                    if stack[-1] == parenthesis_dict[parenthesis]:
                        stack.pop()
                    else:
                        return False
        if stack:
            return False
        return True


solution = Solutions()
print(solution.valid_parenthesis('({}[])('))
