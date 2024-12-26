class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return
            current = current.next

    def display_forward(self):
        '''Отображение элементов списка в прямом порядке'''
        current = self.head
        while current:
            if current == self.head:
                print(current.data, end='->')
            if current == self.tail:
                print(current.data, end='<-')
            else:
                print(current.data, end='<->')
            current = current.next

    def display_backward(self):
        '''Отображение элементов списка в обратном порядке'''
        current = self.tail
        while current:
            if current == self.tail:
                print(current.data, end=' ')
            if current == self.head:
                print(current.data, end=' ')
            else:
                print(current.data, end=' ')
            current = current.prev

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None

if __name__ == "__main__":
    dlk = DoubleLinkedList()
    dlk.append(1)
    dlk.append(2)
    dlk.append(3)

    print('Список вперед')
    dlk.display_forward()
    print('Список назад')
    dlk.display_backward()
    dlk.prepend(0)
    print("После добавления 0 в начало:")
    dlk.display_forward()

    dlk.delete(2)
    print("После удаления 2:")
    dlk.display_forward()

    node = dlk.search(3)
    if node:
        print(f"Узел с данными {node.data} найден.")
    else:
        print("Узел не найден.")