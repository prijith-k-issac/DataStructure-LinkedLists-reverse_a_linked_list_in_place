# Reverse a linked list in-place overview
# Interview Question #8
#
# Construct an in-place algorithm to reverse a linked list!


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):

        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            node.next_node = self.head
            self.head = node

    def traverse(self):
        node = self.head

        while node is not None:
            print(node.data)
            node = node.next_node

    def reverse(self):
        next = None
        previous = None
        current_node = None
        while self.head is not None:
            current_node = self.head
            next = self.head.next_node
            self.head.next_node = previous
            self.head = next
            previous = current_node

        if self.head is None:
            self.head = previous


linkedlist = LinkedList()
linkedlist.insert(5)
linkedlist.insert(13)
linkedlist.insert(2)
linkedlist.insert(10)
linkedlist.traverse()
linkedlist.reverse()
print("after reversing")
linkedlist.traverse()

