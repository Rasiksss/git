class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

    def display(self):
        if not self.head:
            print('Список пуст')
            return
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
            if current == self.head:
                break
        print(f'Голова({self.head.data})')


circular_list = CLL()
circular_list.append(1)
circular_list.append(2)
circular_list.append(3)

circular_list.display()