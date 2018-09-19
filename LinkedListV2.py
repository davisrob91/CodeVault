class Node(object):
    """ Private Data type for LinkedList
    methods within are used by LinkedList """
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_data(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node
        return self

    def __str__(self):
        return str(self.value)

class LinkedList(object):

    def __init__(self, head=None):

        self.head = Node(head)
        if (head==None):
            self.length = 0
        else:
            self.length = 1

    def insert(self, value):

        node = Node(value)

        if self.length < 1:
            self.head = node
            node.set_next(None)
            self.length+=1
            return self

        node.set_next(self.head)
        self.head = node
        self.length+=1

        return self

    def insert_at(self, value, pos):
        """ insert_at(value, position) - inserts that value at that location
        within the linked list. Will not insert if position is greater than length """
        if self.length < pos:
            return
        else:
            count = 1
            node = self.head
            while count < pos:
                print(node.get_data())
                count+=1
                node = node.get_next()
            new_node = Node(value)
            new_node.set_next(node.get_next())
            node.set_next(new_node)
            self.length+=1

    def pop(self):
        """ Removes the first value in the linked list and returns that value """
        if self.is_empty():
            return None
        else:
            data = self.head.get_data()
            self.head = self.head.get_next()
            self.length-=1
            return data

    def remove(self, value):
        """ Removes first instance of value if found within linked list. """

        if self.is_empty():
            return
        node = self.head
        
        while node.get_next() != None:
            if node.get_next().get_data() == value:
                node.set_next(node.get_next().get_next())
                return
            node = node.get_next()
            
    def get_max(self):
        """ Returns the largest value stored within the linked list class """
        if self.is_empty():
            return None
        node = self.head
        max_node = node.get_data()
        while node.get_next() != None:
            if max_node < node.get_next().get_data():
                max_node = node.get_next().get_data()
            node = node.get_next()
        return max_node

    def get_min(self):
        """ Returns the smallest value stored within the linked list class """
        if self.is_empty():
            return None
        node = self.head
        min_node = node.get_data()
        while node.get_next() != None:
            if min_node > node.get_next().get_data():
                min_node = node.get_next().get_data()
            node = node.get_next()
        return min_node

    def search(self, value):
        """ search(value) - Returns the first position within the linked list
        that this value is found at. If the value is not found
        a -1 is returned """
        pos = 0
        if self.is_empty():
            return None
        node = self.head
        
        while node.get_next() != None:
            if node.get_data() == value:
                return pos
            pos+=1
            node = node.get_next()
            
        return -1

    def reverse(self):
        current = self.head
        prev = None
        temp = current.get_next()
        while current:
            current.set_next(prev)
            prev = current
            current = temp
            if current:
                temp = temp.get_next()
                
        self.head = prev

    def print_reverse(self):
        
        node = self.head
        reverse(node)
        print()

    def reverse_recur(self, node=None):

        #Check if node is head of old LinkedList
        if node == None:
            node = self.head


        #When end of LinkedList is found set as head
        if node.get_next() == None:
            self.head = node
            return

        #Traverse to end of list, at end last node will return
        self.reverse_recur(node = node.get_next())

        #Second to last node code, create temp node that holds last node(head)
        new_node = node.get_next()

        #switch direction nodes point
        new_node.set_next(node)
        node.set_next(None)
     
        
            
    def get_length(self):
        """ Returns the number of values stored within the linked list """
        return self.length
    
    def is_empty(self):
        return self.length==0
    
    def __str__(self):
        """ The items of the linked list are placed in a list
        and returned as a string """
        print_node = self.head
        return_lst = []
        while(print_node):
            return_lst.append(print_node.get_data())
            print_node = print_node.get_next()
        return str(return_lst)

def reverse(node):
    if node != None:
            reverse(node.get_next())
    else:
            return
    print(node, end=", ")
a = LinkedList()

print(a)

a.insert(25).insert(15).insert(-2).insert(-5).insert(26).insert(0)

print(a)

print(a.pop())

print(a)

print(a.get_max())

print(a.get_min())

print(a.get_length())
print(a)

print(a.search(-2))

print()
a.insert_at(100, 3)
print(a)
a.insert_at(50, 13)
print(a)

a.remove(-2)
print(a)

a.insert(-2)
print(a)
print(a.get_max())

print(a)
a.reverse()
print(a)

a.print_reverse()

a.reverse_recur()
print(a)
