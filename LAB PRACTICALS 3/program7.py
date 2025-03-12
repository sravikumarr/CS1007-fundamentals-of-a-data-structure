class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        if self.head is None:  # If the list is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head  # New node's next is the current head
            self.head.prev = new_node  # Current head's previous points to the new node
            self.head = new_node  # New node becomes the new head

    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if self.tail is None:  # If the list is empty
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail  # New node's previous is the current tail
            self.tail.next = new_node  # Current tail's next points to the new node
            self.tail = new_node  # New node becomes the new tail

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()  # For moving to the next line after the traversal


# Example usage:
dll = DoublyLinkedList()

# Insert elements at the beginning
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
print("Doubly linked list after inserting 20, 10 at the beginning:")
dll.traverse_forward()

# Insert elements at the end
dll.insert_at_end(30)
dll.insert_at_end(40)
print("\nDoubly linked list after inserting 30, 40 at the end:")
dll.traverse_forward()

# Traverse the list forward
print("\nTraversing the doubly linked list forward:")
dll.traverse_forward()

