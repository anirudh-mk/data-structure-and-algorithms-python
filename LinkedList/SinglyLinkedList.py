class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def items(self):
        current_node = self.head
        item_list = ''
        while current_node:
            item_list += f"{current_node.data} => "
            current_node = current_node.next
        item_list += 'None'
        print(item_list)

    def insert(self, item, index):
        if index < 0:
            print('Index out of range')
            return

        current_node = self.head
        count = 0

        new_node = Node(item)
        if index == 0:
            new_node.next = current_node
            self.head = new_node
            return

        while current_node and count < index - 1:
            current_node = current_node.next
            count += 1

        if current_node:
            new_node.next = current_node.next
            current_node.next = new_node
            return
        print("index out of range")

    def insert_at_end(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def search(self, item):
        current_node = self.head
        while current_node:
            if current_node.data == item:
                return True
            current_node = current_node.next
        return False

    def delete_at_beginning(self):
        if self.head:
            self.head = self.head.next
            return
        print("no data found")

    def delete_at_end(self):
        if not self.head:
            print("linked list is empty")
            return
        if not self.head.next:
            self.head = None
            return
        current_node = self.head
        if current_node.next and current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def delete_at_specific_point(self, index):
        if not self.head:
            print("empty linked list")
            return
        if index < 0:
            print("index out of range")
            return

        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head
        count = 0
        while count < index - 1 and current_node:
            count += 1
            current_node = current_node.next

        if not current_node or not current_node.next:
            print('Index out of range')
            return

        current_node.next = current_node.next.next

    def reverse(self):
        current_node = self.head
        prev_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def modify(self, item, index):
        if not self.head:
            print("empty linked list")
            return
        if index == 0:
            self.head.data = item
            return
        current_node = self.head
        count = 0

        while current_node and count < index - 1:
            current_node = current_node.next
            count += 1

        if current_node:
            current_node.data = item
            return

        print("Index out or range")


linked_list = LinkedList()
linked_list.insert_beginning(1)
linked_list.insert_beginning(4)
linked_list.insert(5, 1)
linked_list.modify(10, 1)
linked_list.items()
