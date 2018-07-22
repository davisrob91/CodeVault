class Node(object):
    """ Private Data type for LinkedList
    methods within are used by LinkedList """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def get_data(self):
        return self.value

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, next_node):
        self.next = next_node
        return self

    def set_prev(self, prev_node):
        self.prev = prev_node
        return self

    def __str__(self):
        return str(self.value)

class DoublyLinkedList(object):

    def __init__(self, head=None):
        self.head = Node(head)

    def insert(self, value):

        if self.head.get_data() == None:
            node = Node(value)
            self.head = node
            node.set_next = None
            return self

        node = Node(value)
        self.head.set_prev(node)
        node.set_next(self.head)
        self.head = node

        return self

    def insert_at(self, value, pos):

        if self.length() < pos:
            return
        
        else:
            count = 1
            node = self.head
            while count < pos:
                count+=1
                node = node.get_next()
            new_node = Node(Value)
            new_node.set_next(node.get_next())
            new_node.set_prev(node)
            node.set_next(new_node)

    def pop(self):
        value = self.head.get_data()
        self.head = self.head.get_next()
        return value

        
    def length(self):
        """ Returns the number of values stored within the linked list """
        count = 1
        node = self.head
        if self.is_empty():
            return 0
        while node.get_next() != None:
            count+=1
            node = node.get_next()
        return count

    def is_empty(self):
        """ Checks to see if the linked list is empty """
        return self.head.get_data() == None
    
    def __str__(self):
        """ The items of the linked list are placed in a list
        and returned as a string """
        print_node = self.head
        return_lst = []
        while(print_node):
            return_lst.append(print_node.get_data())
            print_node = print_node.get_next()
        return str(return_lst)

    def print_backwards(self):

        node = self.head
        count = 0
        
        while count < self.length() - 1:
            node = node.get_next()
            
            count+=1

        return_lst = []
        count = self.length()

        while count:
            return_lst.append(node.get_data())
            node = node.get_prev()
            count-=1

        return str(return_lst)


a = DoublyLinkedList()

print(a)


a.insert(25).insert(15).insert(-2).insert(-5).insert(26).insert(0)

print(a)

print(a.print_backwards())
