class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None

        data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    # Test the Queue class
    queue = Queue()

    # Enqueue elements
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Display the queue
    print("Queue after enqueuing 1, 2, and 3:")
    queue.display()

    # Dequeue elements
    print("Dequeued element:", queue.dequeue())
    print("Dequeued element:", queue.dequeue())

    # Display the queue after dequeuing
    print("Queue after dequeuing two elements:")
    queue.display()
