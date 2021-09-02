class Cqueue:
    que = []

    def isEmpty(self):
        return True if len(self.que) == [] else False

    def insert(self, lenQ):
        if len(self.que) == lenQ:
            print('Queue is full')

        else:
            data = input('Enter element in the queue: ')
            self.que.append(data)

    def remove(self):
        if self.isEmpty == True:
            print('Queue is already empty')

        else:
            pdta = self.que.pop(0)
            print('%s from Circular Queue is popped' % pdta)

    def display(self):
        if self.isEmpty == True:
            print('queue is empty')
        else:
            print('Data of queue are: ')
            for i in self.que:
                print(i)


if __name__ == '__main__':
    obj = Cqueue()
    # creating the object
    lenQ = int(input('Enter the length of queue: '))
    while 1:
        choice = input(
            '\n 1. insert data \n 2. pop data \n 3. display queue \n 4. Exit \n ')

        if choice == '1':
            obj.insert(lenQ)
        elif choice == '2':
            obj.remove()
        elif choice == '3':
            obj.display()
        elif choice == '4':
            exit()

        else:
            print('Wrong choice')
