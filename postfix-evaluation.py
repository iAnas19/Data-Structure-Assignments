OPERATORS = set(['*', '-', '+', '%', '/', '**'])


def evaluate_postfix(expression):
    stack = []

    for i in expression:
        if i not in OPERATORS:
            stack.append(i)

        else:
            a = stack.pop()
            b = stack.pop()

            if i == '+':
                res = int(b)+int(a)

            elif i == '-':
                res = int(b)-int(a)

            elif i == '*':
                res = int(b)*int(a)

            elif i == '%':
                res = int(b) % int(a)

            elif i == '/':
                res = int(b)/int(a)

            elif i == '**':
                res = int(b)**int(a)
            stack.append(res)

    return(''.join(map(str, stack)))


expression = input('Enter the postfix expression ')
print()

print('postfix expression entered: ', expression)
print('Evaluation result: ', evaluate_postfix(expression))
