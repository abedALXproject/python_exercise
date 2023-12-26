#!/usr/bin/python3
"""
This code defines a Node class with two fields: data and next. The LinkedList class has three methods: add_node, delete_node, and find_node. The add_node method adds a new node to the beginning of the linked list. The delete_node method deletes a node with the given data from the linked list. The find_node method returns a pointer to the node with the given data, or None if no such node exists. The main function demonstrates how to use these methods to create, modify, and search a linked list
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, data):
        temp = self.head
        if (temp is not None):
            if (temp.data == data):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        if(temp == None):
            return
        prev.next = temp.next
        temp = None

    def find_node(self, data):
        temp = self.head
        while(temp is not None):
            if temp.data == data:
                return temp
            temp = temp.next
        return None

linked_list = LinkedList()
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)
linked_list.add_node(4)
linked_list.add_node(5)

print("Initial linked list: ", end="")
temp = linked_list.head
while(temp is not None):
    print(temp.data, end=" ")
    temp = temp.next
print()

linked_list.delete_node(3)

print("Linked list after deleting node with data 3: ", end="")
temp = linked_list.head
while(temp is not None):
    print(temp.data, end=" ")
    temp = temp.next
print()

node_2 = linked_list.find_node(2)
if node_2 is not None:
    print("Node with data 2 found")
else:
    print("Node with data 2 not found")
