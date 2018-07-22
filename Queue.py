import random

class Node(object):

    def __init__(self, value=None):
        
        self.next = None
        self.prev = None
        self.value = value

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, node):
        self.next = node

    def set_prev(self, node):
        self.prev = node

    def get_value(self):
        return self.value

class Queue(object):

    def __init__(self, value=None):
        node = Node(value)
        self.head = node
        self.tail = node
        if value == None:
            self.length = 0
        else:
            self.length = 1

    def add(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node

        else:
            node.set_prev(self.tail)
            self.tail.set_next(node)
            self.tail = node

        self.length+=1
        return self

    def pop(self):
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def __str__(self):

        print_node = self.head
        print_str = []
        while print_node:
            print_str.append(print_node.get_value())
            print_node = print_node.get_next()

        return str(print_str)

    def search(self, value):

        front = self.head
        back = self.tail
        count = 0
        while front != back:
            count+=1
            if front.get_value() == value:
                return (True, count)
            if back.get_value() == value:
                return (True, count)
            front = front.get_next()
            back = back.get_prev()
        return False

    def search_bad(self, value):

        front = self.head

        count = 0

        while front != None:
            count+=1
            if front.get_value() == value:
                return (True, count)
            front = front.get_next()

        return False
            

a = Queue(5)

print(a)

a.add(6).add(3).add(-500)
a.add(4)
print(a)

print(a.pop())
print(a)
a.add(500)
print(a)

print(a.search(3))

for x in range(2000):
    a.add(random.randint(0, 1000))

print(a.search(25))
print(a.search_bad(25))

            
        
