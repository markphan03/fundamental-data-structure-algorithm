"""
Cấu trúc dữ liệu Single Linked List đơn giản!
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = None

def search(L, k):
    """ Search node with key = k, if find none then return None """
    x = L.head
    while x != None and x.key != k:
        x = x.next
    return x

def insert(L, k):
    """ Insert k at the top of the linked list"""
    node = Node(k)
    node.next = L.head
    L.head = node

def delete(L, k):
    """ Delete node with key k """
    if L.head != None:
        if L.head.key == k:
            L.head = L.head.next
        else:
            predecessor_node = deleted_node = L.head
            while deleted_node != None and deleted_node.key != k:
                predecessor_node = deleted_node
                deleted_node = deleted_node.next
            if deleted_node != None:
                predecessor_node.next = deleted_node.next

def insert_last(L, k):
    """ Insert node key k at the end of the linked list """
    node = Node(k)
    y = L.head
    if y != None:
        L.head = node
    else:
        while y.next != None:
            y = y.next
        y.next = node

def insert_before(L, k, nk):
    """ Insert node k before nk
    Muốn insert node k before nk thì phải insert nốt k giữa nốt nk-1 và nk.
    """
    x = Node(k) # new node
    if L.head != None:
        if L.head.key == nk:
            x.next = L.head
            L.head = x
        else:
            z = y = L.head # z is the node before y.
            while y != None and y.key != nk:
                z = y
                y = y.next
            if y != None:
                # Muốn chèn x trước y, thì để x sau z.
                x.next = y
                z.next = x

def delete_first(L):
    if L.head != None:
        L.head = L.head.next

def delete_last(L):
    """ Xóa phần tử cuối của dãy.
    Để làm được thì ta phải tìm phần tử cuối, và phần tử kế cuối để update kế cuối.next = None
    """
    if L.head != None:
        y = L.head
        x = L.head
        while x.next != None:
            y = x
            x = x.next
        y.next = None

def isEmpty(L):
    return L.head == None

def show(L):
    x = L.head
    while x != None:
        print(x.key, end="")
        x = x.next
    print()








