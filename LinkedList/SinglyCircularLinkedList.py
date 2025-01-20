class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next
        current_node.next = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next
        current_node.next = new_node
        new_node.next = self.head

    def insert_at_specific_index(self, data, index):
        if index < 0:
            print('Index out of range')
            return
        new_node = Node(data)
        if not self.head:
            if index == 0:
                new_node.next = self.head
                self.head = new_node
                return
            print('Linked list is empty')
            return
        if index == 0:
            new_node.next = self.head
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            self.head = new_node
            return
        current_node = self.head
        count = 0
        while current_node.next != self.head and count < index - 1:
            current_node = current_node.next
            count += 1

        if count < index - 1:
            print('index out of range')
            return
        new_node.next = current_node.next
        current_node.next = new_node

    def insert_after_specific_node(self, node, data):
        if not self.head:
            print('Linked list is empty')
            return
        new_node = Node(data)
        current_node = self.head
        while True:
            if current_node.data == node:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
            if current_node == self.head:
                break
        print('Node not found')

    def delete_at_beginning(self):
        if not self.head:
            print("Linked list is empty")
            return
        if self.head.next == self.head:
            self.head = None
            return
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next
        current_node.next = self.head.next
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            print('linked list is empty')
            return
        if self.head.next == self.head:
            self.head = None
            return
        current_node = self.head
        while current_node.next.next != self.head:
            current_node = current_node.next
        current_node.next = self.head
