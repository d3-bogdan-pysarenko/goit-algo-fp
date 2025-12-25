class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elements) + " -> None")

def reverse_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev


def insertion_sort(linked_list):
    sorted_head = None
    current = linked_list.head
    
    while current:
        next_node = current.next
        
        if sorted_head is None or sorted_head.data >= current.data:
            current.next = sorted_head
            sorted_head = current
        else:
            temp = sorted_head
            while temp.next and temp.next.data < current.data:
                temp = temp.next
            current.next = temp.next
            temp.next = current
            
        current = next_node
    
    linked_list.head = sorted_head


def merge_sorted_lists(list1, list2):
    dummy_node = Node(0)
    tail = dummy_node
    
    l_1 = list1.head
    l_2 = list2.head
    
    while l_1 and l_2:
        if l_1.data < l_2.data:
            tail.next = l_1
            l_1 = l_1.next
        else:
            tail.next = l_2
            l_2 = l_2.next
        tail = tail.next
    
    tail.next = l_1 if l_1 else l_2
    
    new_ll = LinkedList()
    new_ll.head = dummy_node.next
    return new_ll

#-----------------------------------------------------------------------------
# Checking time
ll = LinkedList()
for val in [3, 1, 4, 2]: ll.insert(val)
print("Original:")
ll.display()

insertion_sort(ll)
print("Sorted:")
ll.display()

reverse_list(ll)
print("Reversed:")
ll.display()