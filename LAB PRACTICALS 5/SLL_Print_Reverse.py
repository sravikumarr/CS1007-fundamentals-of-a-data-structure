class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse(self):
        prev, current = None, self.head
        while current:
            current.next, prev, current = prev, current, current.next
        self.head = prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

# Example usage
linked_list = SinglyLinkedList()
for value in ['a', 'b', 'c', 'd']:
    linked_list.append(value)

print("Original Linked List:")
linked_list.display()

linked_list.reverse()
print("Reversed Linked List:")
linked_list.display()
