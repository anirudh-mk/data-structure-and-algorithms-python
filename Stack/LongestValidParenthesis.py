class Solutions:
    def longest_valid_parenthesis(self, data):
        stack = []
        is_ok = [0] * len(data)

        for index, item in enumerate(data):
            if item == "(":
                stack.append(index)
            else:
                if stack:
                    is_ok[stack.pop()] = 1
                    is_ok[index] = 1
                else:
                    pass

        count = 0
        answer = 0
        for index in range(len(data)):
            if is_ok[index]:
                count += 1
            else:
                count = 0
            answer = max(answer, count)
        print(answer)

my_data = Solutions()
my_data.longest_valid_parenthesis('((()')
