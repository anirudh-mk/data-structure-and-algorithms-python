import operator


class Solutions:
    def evaluate_reverse_polish_notation(self, postfix):
        stack = []
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        for element in postfix:
            if element not in ['+', '-', '*', '/']:
                stack.append(int(element))
            else:
                stack.append(int(operators[element](stack.pop(), stack.pop())))
        return stack[0]
