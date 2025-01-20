class Solutions:
    def simplify_path(self, path: str) -> str:
        stack = []
        for directory in path.split('/'):
            print(directory)
            if directory == ' ':
                pass
            if directory == '.':
                pass
            elif directory == '..':
                if stack:
                    stack.pop()
                else:
                    pass
            else:
                stack.append(directory)

        return "/" + "".join(stack)


solution = Solutions()
correct_path = solution.simplify_path('/home/../../temp//./')
print(correct_path)
