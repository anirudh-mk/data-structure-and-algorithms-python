class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, item):
        new_node = Node(item)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def insert_after_a_node(self, node, item):
        if not self.head:
            print('linked list is empty')
            return
        new_node = Node(item)
        current_node = self.head
        while current_node:
            if current_node.item == node:
                new_node.next = current_node.next
                new_node.prev = current_node
                current_node.next = new_node
                if current_node.next:
                    new_node.next.prev = new_node
                return
            current_node = current_node.next
        print('index out of range')

    def insert_before_a_node(self, node, item):
        if not self.tail:
            print('linked list is empty')
            return
        current_node = self.tail
        new_node = Node(item)
        while current_node:
            if current_node.item == node:
                new_node.prev = current_node.prev
                new_node.next = current_node
                if current_node.prev:
                    current_node.prev.next = new_node
                current_node.prev = new_node
                return
            current_node = current_node.prev
        print('index out of range')

    def insert_at_specific_index(self, item, index):
        if not self.head:
            print("Linked list is empty")
            return
        new_node = Node(item)
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        count = 0
        current_node = self.head
        while current_node and count < index - 1:
            current_node = current_node.next
            count += 1
        if current_node:
            new_node.next = current_node.next
            new_node.prev = current_node.prev
            if current_node.next:
                current_node.next.prev = new_node
            else:
                self.tail = new_node
            current_node.next = new_node
            return
        print("index out of range")

    def display_from_beginning(self):
        current_node = self.head
        items = ''
        while current_node:
            items += f"[{current_node.item}] => "
            current_node = current_node.next
        items += 'None'
        print(items)

    def display_from_end(self):
        current_node = self.tail
        items = ''
        while current_node:
            items += f"[{current_node.item}] => "
            current_node = current_node.prev
        items += 'None'
        print(items)

    def remove_from_beginning(self):
        if not self.head:
            print('Linked list is empty')
            return
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
            return
        self.head = None
        self.tail = None


my_linked_list = DoubleLinkedList()
my_linked_list.insert_at_beginning(2)
my_linked_list.insert_at_beginning(4)
# my_linked_list.insert_at_beginning(2)
# my_linked_list.insert_at_beginning(3)
# my_linked_list.insert_at_beginning(5)
# my_linked_list.insert_at_end(34)
# my_linked_list.insert_at_end(3124)
# my_linked_list.insert_after_a_node(34, 70)
# my_linked_list.insert_before_a_node(70, 450)
# my_linked_list.insert_at_specific_index(18, 7)
# my_linked_list.display_from_beginning()
my_linked_list.remove_from_beginning()
my_linked_list.display_from_end()
