"""
# 19
# Data Structures Challenge
# Implement a linked list and perform basic operations like insertion and deletion.
# Difficulty: Hard

Code Explanation
The provided code defines a simple linked list in Python. A linked list is a linear data structure where each element (node) contains a reference (link) to the next element in the sequence. This implementation includes two classes: Node and LinkedList.

Attributes:
head: A reference to the first node in the list (initially None).
Methods:
__init__: Initializes an empty linked list with head set to None.
append: Adds a new node with the given data to the end of the list.
Creates a new node.
If the list is empty (head is None), sets head to the new node.
Otherwise, traverses the list to find the last node and sets its next to the new node.
print_list: Prints the data of each node in the list, separated by arrows (->).
"""

# To create the linked list we need to have a class for the nodes and classes for the linked list itself

# Node Class
class Node:
    def __init__(self, data):
        self.data = data # Stores the value of the node
        self.next = None # Refers to the next node in the list. Initially None

# Class for Linked List
class LinkedList:
    def __init__(self):
        self.head = None # References to the first node in the list (None)

    def append(self, data):
        new_node = Node(data) # Create a new node with the given data
        if not self.head: # If the list is empty, set the new node as the head
            self.head = new_node
            return
        
        last_node = self.head # Start from the head node
        while last_node.next: # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node # Set the next of the last node to the new node

    def print_list(self):
        current_node = self.head # Stores the linked list value as temp variable current_node
        while current_node: # While loop to print each node of the linked list
            print(current_node.data, end=" ") # Print the data of the current node and separate them with a space
            current_node = current_node.next # Move to the next node
        print() # Print a newline at the end

    def remove(self, key):
        current_node = self.head # Start from the head node

        # If the head node itself holds the key to be deleted
        if current_node and current_node.data == key:
            self.head = current_node.next # Change head to the next node
            current_node = None # Free the old head node
            return

        # Search for the key to be deleted, keep track of the previous node
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        # If the key was not present in the linked list
        if current_node is None:
            return

        # Unlink the node from the linked list
        prev.next = current_node.next
        current_node = None # Free the node to be deleted


# LinkedList Ussage
ll = LinkedList()

# Add values to the LinkedList
ll.append("Owen")
ll.append(21)
ll.append("Loves tacos")
ll.print_list()
ll.remove(21)
ll.print_list()
ll.append(22)
ll.print_list()