class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node
            self.head = new_node

    def traverse(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("HEAD")

cll = CircularLinkedList()
cll.insert_at_beginning(101)
cll.insert_at_beginning(201)
cll.insert_at_beginning(301)

cll.traverse()
