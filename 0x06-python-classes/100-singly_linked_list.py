#!/usr/bin/python3
"""Linked List class"""


class Node:
    """Node class"""
    def __init__(self, data, next_node=None):
        """Constructor for Node Class"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter function for __data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter function for __data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for __next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for __next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """Linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a node"""
        new_node = Node(value)
        if not self.__head or self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node

        # elif self.__head.data >= new_node.data:
        #     new_node.next_node = self.__head
        #     self.__head = new_node

        else:
            current = self.__head
            while (current.next_node and
                   current.next_node.data < new_node.data):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """String method of Linked List"""
        s = ""
        current = self.__head
        while current:
            s += str(current.data) + "\n"
            current = current.next_node
        return s[:-1]
