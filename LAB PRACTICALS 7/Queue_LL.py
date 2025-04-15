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

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        else:
            temp = self.front
            self.front = temp.next
            deleted_item = temp.data
            del temp
            print(f"Dequeued item is {deleted_item}")
            return deleted_item

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
