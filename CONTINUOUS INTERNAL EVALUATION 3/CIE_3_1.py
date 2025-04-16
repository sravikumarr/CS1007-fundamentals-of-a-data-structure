#Write a program to a class/structure CircularNode to represent a node in a circular linked list. Each node should have two attributes: data and next. Then, create a class/structure CircularLinkedList to represent the linked list itself. Implement the following operations:

class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = CircularNode(data)
        
        
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            
            
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    def delete_node(self, data):
        if self.head is None:
            print("The list is empty!")
            return

        
        if self.head.data == data and self.head.next == self.head:
            self.head = None
            return
        
    
        if self.head.data == data:
            temp = self.head
            
            while temp.next != self.head:
                temp = temp.next
        
            temp.next = self.head.next
            self.head = self.head.next
            return
        
        
        temp = self.head
        while temp.next != self.head and temp.next.data != data:
            temp = temp.next
        
        if temp.next == self.head:  
            print(f"Node with data {data} not found!")
            return
        
        
        temp.next = temp.next.next

    def display(self):
        if self.head is None:
            print("The list is empty!")
            return
        
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("... (circular)")

# Example Usage:
circular_list = CircularLinkedList()

# Insert elements at the beginning
circular_list.insert_at_beginning(10)
circular_list.insert_at_beginning(20)
circular_list.insert_at_beginning(30)

# Display the list
print("Circular Linked List after insertions:")
circular_list.display()

# Delete a node
circular_list.delete_node(20)

# Display the list again
print("\nCircular Linked List after deleting 20:")
circular_list.display()

# Delete a node that does not exist
circular_list.delete_node(40)

# Delete the head node
circular_list.delete_node(30)

# Display the list again
print("\nCircular Linked List after deleting 30:")
circular_list.display()


