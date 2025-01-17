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
            self.head = self.head
            new_node.next = self.head
            return
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next
        current_node.next = new_node
        new_node.next = self.head

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
