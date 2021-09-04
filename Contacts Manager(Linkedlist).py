class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:

    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def get_lenght(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.ref

        return count

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
            return
        else:
            self.head = self.head.ref

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def insert_at(self, index, data):
        if index < 0 or index > self.get_lenght():
            raise Exception("Invalid exception")

        if index == 0:
            self.add_begin(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data)
                node.ref = itr.ref
                itr.ref = node
            itr = itr.ref
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_lenght():
            raise Exception("Invalid index")

        elif index == 0:
            self.head = self.head.ref
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.ref = itr.ref.ref
                break
            itr = itr.ref
            count += 1

    def search(self, data):
        if self.head is None:
            print('List has no element')
            return
        else:
            itr = self.head
            while itr is not None:
                if itr.data == data:
                    return True
                itr = itr.ref
            return False


if __name__ == '__main__':
    LL1 = LinkedList()

    while True:
        choice = input('Welcome to Contact manager \n1.Add at the beginning \n2. Add at the end \n3. Add at specific '
                       'index \n4. Delete from beginning \n5. Delete from the end \n6. Delete from specific index '
                       '\n7. Search \n8. Exit \n9.Show Contacts\n=> ')
        if choice == '1':
            name = input('Name of contact: ')
            number = input('Name of number: ')
            LL1.add_begin([name, number])

        elif choice == '2':
            name = input('Name of contact: ')
            number = input('Name of number: ')
            LL1.add_end([name, number])

        elif choice == '3':
            name = input('Name of contact: ')
            number = input('Name of number: ')
            indexNo = int(input('At which index: '))
            LL1.insert_at(indexNo, [name, number])

        elif choice == '4':
            LL1.delete_begin()

        elif choice == '5':
            LL1.delete_end()

        elif choice == '6':
            IndexNo = int(input('From which index: '))
            LL1.remove_at(IndexNo)

        elif choice == '7':
            name2 = input('Name you want to search: ')
            contact2 = input('Contact number: ')
            print('Searching for [%s,%s]...' %
                  (name2, contact2))
            if LL1.search([name2, contact2]):
                print("Contact found")
            else:
                print("Contact not found")

        elif choice == '8':
            exit()
        elif choice == '9':
            LL1.print_ll()

        else:
            print('Wrong input')
