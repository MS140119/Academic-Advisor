from node import Node

    class LinkedList:
        def __init__(self):
            self.head = None #initializing the linked list with no head node

        def add(self, data): #this adds a new node to the end of the linked list
            new_node = Node(data)
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node

        def remove(self, student_id): #this removes a node by mathcing the student id
            current = self.head
            previous = None
            while current:
                if current.data.get_student_id() == student_id:
                    if previous:
                        previous.next = current.next
                    else:
                        self.head = current.next
                    return True
                previous = current
                current = current.next
            return False
        
        def find(self, student_id): #this finds a node by student id
            current = self.head
            while current:
                if current.data.get_student_id() == student_id:
                    return current.data
                current = current.next
            return None
        
        def __iter__(self): #this functions lets the linked list be iterable
            current = self.head
            while current:
                yield current.data
                current = current.next
        
        def __str__(self): #this is a string representation of the linked list
            if not self.head:
                return "There are no advisees here"
            result = []
            current = self.head
            while current:
                result.append(str(current.data))
                current = current.next
            return "\n".join(result)
