class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued item is {self.rear.data}")

    def front_item(self):
        if self.front is None:
            print("Queue is empty")
            return None
        else:
            print(f"Front item is {self.front.data}")
            return self.front.data

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        else:
            temp = self.front
            self.front = temp.next
            deleted_item = temp.data
            if self.front is None:  # If the queue becomes empty
                self.rear = None
            del temp
            print(f"Dequeued item is {deleted_item}")
            return deleted_item

    def serve_customers(self):
        customer_ids = [101, 102, 103, 104, 105]
        print("Enqueueing customers:")
        for customer_id in customer_ids:
            self.enqueue(customer_id)
        
        print("\nServing customers:")
        while not self.is_empty():
            self.dequeue()
        
        if self.is_empty():
            print("\nAll customers have been served. The queue is empty now.")

q = Queue()
q.serve_customers()
