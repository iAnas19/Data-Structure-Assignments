Stack = []


def isEmpty(stack):
    if(stack == []):
        return True
    else:
        False


def push(stack, item):
    stack.append(item)


def pop(stack):
    if(isEmpty(stack)):
        return False
    else:
        s = stack.pop()
    return s


def reverse(stack):
    n = len(stack)
    emptyStk = []

    for i in range(0, n, 1):
        push(emptyStk, stack[i])

    stack = ''

    for i in range(0, n, 1):
        stack += pop(emptyStk)
    return stack


while True:
    stack = input('Enter values you want to reverse: ')
    item = reverse(stack)
    print('Reversed values are %s' % item)
