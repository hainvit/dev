'''
* Mỗi phần tử  trong ds có 2 con trỏ
-> Một con trỏ, trỏ đến phần tử trước nó
-> Một con trỏ, trỏ đến phần tử sau nó
'''
class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # add beginning node
    def push(self, new_val):
        node = Node(new_val)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node

    # print linked list
    def print_doubly_linked_list(self):
        node = self.head
        while node is not None:
            print(node.data_val)
            node = node.next

doubly_linked_list = DoublyLinkedList()
node1 = Node(1)
doubly_linked_list.head = node1
doubly_linked_list.push(2)
doubly_linked_list.print_doubly_linked_list()
