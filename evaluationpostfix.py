# set of operators allowed in expression
OPERATORS = set(['*', '-', '+', '%', '/', '**'])


def evaluate_postfix(expression):

    stack = []  # empty stack for storing numbers

    for i in expression:

        if i not in OPERATORS:

            stack.append(i)  # contains numbers

        else:

            a = stack.pop()  # if ch==operator then pop 2 numbers

            b = stack.pop()

            if i == '+':

                res = int(b)+int(a)  # old val <operator> recent value

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

            stack.append(res)  # final result

    return(''.join(map(str, stack)))


expression = input('Enter the postfix expression ')

print()

print('postfix expression entered: ', expression)

print('Evaluation result: ', evaluate_postfix(expression))
