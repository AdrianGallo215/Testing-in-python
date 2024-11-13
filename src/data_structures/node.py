class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value

    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, value):
        self._next = value