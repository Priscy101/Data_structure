class Node:
    def __init__(self, data = None):
        self.data = data
        self.next_node = None

    def __str__(self):
        return str(self.data)