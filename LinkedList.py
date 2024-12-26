class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print('None')

    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            return

        prev.next = current.next
        current = None

    def sortirovka(self):
        if self.head is None:
            return
        flag = True
        while flag:
            flag = False
            current = self.head
            while current and current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    flag = True
                current = current.next



if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.append(1)
    linkedlist.append(5)
    linkedlist.append(4)
    linkedlist.append(3)
    linkedlist.append(6)
    print("Список")
    linkedlist.display()
    linkedlist.sortirovka()
    linkedlist.display()
