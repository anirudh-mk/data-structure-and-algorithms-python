def infix_to_postfix(infix):
    postfix = []
    stack = []

    priority = {'/': 1, '*': 2, '+': 3, '-': 4}

    for element in infix:
        if element == "(":
            stack.append(element)
        elif element == ")":
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        elif element not in ['+', '-', '*', '/']:
            postfix.append(element)
        else:
            while stack and priority[stack[-1]] <= priority[element]:
                postfix.append(stack.pop())
            stack.append(element)
    while stack:
        postfix.append(stack.pop())
    return postfix
