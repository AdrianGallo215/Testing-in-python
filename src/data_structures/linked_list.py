from data_structures.node import Node

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def add(self, node):
        if self.head is None :
            self.head = node
        else:
            current = self.head
            
            while current.next:
                current = current.next

            current.next = node

    def display(self):
        current = self.head
        while(current):
            print(current.data, end="\n")
            current=current.next

    def len(self):
        current = self.head
        len = 0
        while(current):
            len = len + 1
            current = current.next
        return len

