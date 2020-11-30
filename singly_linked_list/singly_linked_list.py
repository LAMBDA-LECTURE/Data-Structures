# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

#     def get_value(self):
#         return self.value

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def add_to_tail(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
#         self.tail.next = new_node
#         self.tail = new_node

#     def add_to_head(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
#         old_head = self.head
#         self.head = new_node
#         self.head.next = old_head
#         return

#     def remove_head(self):
#         if self.head is None:
#             return
#         data = self.head.get_value()
#         self.head = self.head.next
#         return data

#     def remove_tail(self):
#         if self.head is None:
#             return
#         data = self.tail.get_value()
#         if self.head.next is None:
#             self.head = None
#             self.tail = None
#         cursor = self.head
#         while cursor.next.next is not None:
#             cursor = cursor.next
#         cursor.next = None
#         self.tail = cursor
#         return data
# # arr = [1, 2, 3, 4]
# # Every Node is a List
# # 1 => 1, 2, 3, 4, None
# # 2 => 2, 3, 4, None
# # 3 => 3, 4, None
# # 4 => 4, None
# # None is a valid, but empty, value
# # A node is a single element in the list
# # That single element can be ANYTHING

# ## FATIMA's VERSION with her notes:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None: #The "is" operator compares the identity of two objects while "==" compares the value of two objects
            self.head = new_node
            self.tail = new_node
            return #You could use "break" here instead, but it would still continue to line 20 so maybe don't. Return will end the function
        self.tail.next = new_node
        self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value)  #Created the new_node
        if self.head is None:   #Just in case there isn't already a head, meaning the list is empty
            self.head = new_node
            self.tail = new_node
            return
        old_head = self.head    #This way, the old head doesn't disappear and we can link it to the new one
        self.head = new_node    #Assigning the new_node to the head
        self.head.next = old_head #Reassigning the old head to the next of the new one

    def remove_head(self):
        if self.head is None: #There's nothing to remove if the list is empty, which it is if head is empty
            return
        data = self.head.get_value()
        self.head = self.head.next
        return data

    def remove_tail(self):
        data = self.tail.get_value()
        cursor = self.head  #Can also be pointer. Start at the head
        # Using cursor.next.next so that when the next item of our next item is none, we know that our item is the item before the tail
        while cursor.next.next is not None:   #We don't know how long the list is, hence a while loop
            cursor = cursor.next    #Move the cursor to the next one
        self.tail = cursor   #Set linked list's tail to the cursor
        self.tail.next = None   #Get rid of the connection/arrow to the old tail
        return data


