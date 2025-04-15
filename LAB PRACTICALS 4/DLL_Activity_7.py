class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete_node(self):
        if self.head is None:
            return None
        current = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        del current
        return self.head


    def traverse_backward(self):
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

dll = DoublyLinkedList()
dll.insert_at_beginning(1)
dll.insert_at_beginning(2)
dll.insert_at_beginning(3)
dll.insert_at_beginning(4)

print("Traversing backward:")
dll.traverse_backward()

dll.delete_node()
print("After deleting the first node")
dll.traverse_backward()