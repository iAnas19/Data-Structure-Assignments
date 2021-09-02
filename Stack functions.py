Stack = []
top = None


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


def peek(stack):
    if(isEmpty(stack)):
        return False

    else:
        top = len(stack) - 1
        return stack[top]


def display(stack):
    if(isEmpty(stack)):
        print('Stack is empty!')

    else:
        top = len(stack) - 1
        print(stack[top], ' <== Top')
        for i in range(top-1, -1, -1):
            print(stack[i])


def rest():
    return(input('Press any  key to continue... '))


while 1:
    print("\n")
    print('Stack functions')
    print('1. Push')
    print('2. Pop')
    print('3. Reverse')
    print('4. Peek')
    print('5. Display')
    print('6. Exit')

    choice = input('Enter your Choice(1-5): ')
    if(choice == '1'):
        item = input('Enter Item you want to push: ')
        push(Stack, item)
        print('%s added successfully' % item)
        # rest()

    elif(choice == '2'):
        if(isEmpty(Stack)):
            print("Stack is empty!")
        else:
            item = pop(Stack)
            print('%s element popped' % item)
        # rest()

    elif(choice == '3'):
        stack = input('Enter values you want to reverse: ')
        item = reverse(stack)
        print('Reversed values are %s' % item)

    elif(choice == '4'):
        item = peek(Stack)
        if(isEmpty(Stack)):
            print("Stack is empty!")
        else:
            print('%s is at the top. ' % item)
        # rest()

    elif(choice == '5'):
        if(isEmpty(Stack)):
            print("Stack is Empty!")
        else:
            display(Stack)
        rest()

    elif(choice == '6'):
        break

    else:
        print('Wrong input. Try again')
