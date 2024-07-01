class Node:
    def __init__ (self, initial_value):
        self.data = initial_value
        self.next = None

    def getValue(self):
        return self.data
        
    def getNext(self):
        return self.next
        
    def setValor(self, new_value):
        self.data = new_value
        
    def setNext(self, new_next):
        self.next = new_next

class UnorderedList:
    def __init__(self):
        self.head = None
    
    def add(self, value):
        node = Node(value)
        node.setNext(self.head)
        self.head = node

    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next = current.getNext()
            current.setNext(previous)
            previous = current
            current = next
        self.head = previous

def print_linked_list(list):
    current = list.head
    while current is not None:
        print(current.getValue(), end=" -> ")
        current = current.getNext()
    print("X")
        
list = UnorderedList()
list.add(99)
list.add(37)
list.add(12)

print_linked_list(list)
list.reverse()
print_linked_list(list)

list2 = UnorderedList()
list2.add(11)
list2.add(33)
list2.add(29)
list2.add(55)
list2.add(77)
list2.add(1)
list2.add(123)
list2.add(9)
list2.add(29)
list2.add(26)
list2.add(44)
list2.add(512)

print_linked_list(list2)
list2.reverse()
print_linked_list(list2)