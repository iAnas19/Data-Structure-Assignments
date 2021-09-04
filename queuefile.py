class CircularQueue():

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):

        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full \n")

        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
            print('%s is added.' % data)

        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
            print('%s is added.' % data)

    def dequeue(self):
        if (self.front == -1):
            print("Queue is Empty\n")

        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            print(temp, ' is dequeued')
            return temp

        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            print(temp, ' is dequeued')
            return temp

    def display(self):

        if(self.front == -1):
            print("Queue is Empty")

        elif (self.rear >= self.front):
            print("Elements in the Circular queue are:",
                  end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        else:
            print("Elements in Circular Queue are:",
                  end=" ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full")


if __name__ == '__main__':
    size = int(input('Size of Circular Queue: '))
    obj = CircularQueue(size)

    while 1:
        choice = input(
            '\n 1. Enqueue \n 2. Dequeue \n 3. display queue \n 4. Exit \n ')

        if choice == '1':
            data = input('Enter your variable you want to enqueue: ')
            obj.enqueue(data)

        elif choice == '2':
            obj.dequeue()

        elif choice == '3':
            obj.display()
        elif choice == '4':
            exit()

        else:
            print('Wrong choice')
