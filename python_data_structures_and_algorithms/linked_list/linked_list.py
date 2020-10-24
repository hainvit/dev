'''
* Các phần tử trong ds trỏ đến phần tử tiếp theo của ds
'''

class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_node = None


class SLinkedList:
    def __init__(self):
        self.head_node = None

    def print_list(self):
        node = self.head_node
        while node is not None:
            print(node.data_val)
            node = node.next_node

    # insert at begining
    def insert_begining(self, new_data):
        node = Node(new_data)
        node.next_node = self.head_node
        self.head_node = node

    # insert at end linked list
    def insert_end(self, new_data):
        node = Node(new_data)
        if self.head_node is None:
            self.head_node = node
            return

        # find node end
        node_end = self.head_node
        while node_end.next_node is not None:
            node_end = node_end.next_node

        node_end.next_node = node

    # insert between
    def insert_between(self, middle_node, new_data):
        if middle_node is None:
            return

        node = Node(new_data)
        new_data.next_node = middle_node.next_node
        middle_node.next_node = node

    # remove node
    def remove_node(self, remove_key):
        head_node = self.head_node
        prev_node = None
        current_node = None
        while head_node is not None:
            if head_node.data_val == remove_key:
                current_node = head_node
                break
            prev_node = head_node
            head_node = head_node.next_node

        if current_node is not None:
            prev_node.next_node = current_node.next_node


# create linked list
linked_list = SLinkedList()
linked_list.head_node = Node(1)
node2 = Node(2)
node3 = Node(3)

# link first Node to second node
linked_list.head_node.next_node = node2
node2.next_node = node3

# print liked list
print('* Print data of liked list')
linked_list.print_list()

print('* Insert at begining linked list')
linked_list.insert_begining(0)
linked_list.print_list()

print('* Insert at end linked list')
linked_list.insert_end(-100)
linked_list.print_list()

print('* Remove item of list by key')
linked_list.remove_node(2)
linked_list.print_list()
