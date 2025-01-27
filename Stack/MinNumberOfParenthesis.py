class Solutions:
    def min_number_of_parenthesis(self, data):
        is_ok = [0] * len(data)
        stack = []
        for index, item in enumerate(data):
            if item in "(":
                stack.append(index)
            elif item in ")":
                if stack:
                    is_ok[stack.pop()] = 1
                    is_ok[index] = 1
                else:
                    continue
            else:
                continue
        result = ''
        for index, item in enumerate(data):
            if item in "()":
                if is_ok[index]:
                    result += item
                else:
                    pass
            else:
                result += item

        print(result)


output = Solutions()

string = '(a()s)'
output.min_number_of_parenthesis(string)


# class Solutions:
#     def output(self, data):
#         stack = []
#         is_ok = [0]* len(data)
#
#         for index, item in enumerate(data):
#             if item == '(':
#                 stack.append(index)
#             elif item == ')':
#                 if stack:
#                     is_ok[stack.pop()] = 1
#                     is_ok[index] = 1
#                 else:
#                     continue
#             else:
#                 continue