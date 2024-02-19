"""
Data Structure - custom Queue constructed by arrays
@Author: Mark Phan
Adapted from: Bui Viet Ha - Nhap Mon Thuat Toan
"""


class Queue:
    def __init__(self):
        self.items = []
        self.frontIdx = 0


def enqueue(Q, x):
    Q.items.append(x)


def compress(Q):
    """
    This command has the function of deleting the elements in front of Q.frontIdx.
    Method:
        + Do not directly delete (according to Python's mechanism), but create a new Q.items array with parts from since
    Q.frontIdx to end (len(Q.items) - 1).
    """
    newItems = []
    for i in range(Q.frontIdx, len(Q.items)):
        newItems.append(Q.items[i])
    Q.items = newItems
    Q.frontIdx = 0


# Time complexity of dequeue is O(1) in average case, but O(n) in worst case, which is far better than using del or pop(0)
def dequeue(Q):
    if isEmpty(Q):
        raise RuntimeError("Queue is empty")
    if Q.frontIdx * 2 > len(Q.items):
        compress(Q)
    item = Q.items[Q.frontIdx]
    Q.frontIdx = Q.frontIdx + 1
    return item

# def dequeue(Q): # cost O(n) in average case
#     if isEmpty(Q):
#         raise RuntimeError("Queue is empty")
#     item = Q.items[0]
#     del Q.items[0] # cost O(n) in average case
#     return item


def isEmpty(Q):
    return Q.frontIdx == len(Q.items)


def front(Q):
    if isEmpty(Q):
        raise RuntimeError("Queue is empty")
    return Q.items[Q.frontIdx]


if __name__ == '__main__':
    name = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    Q = Queue()
    for ch in name:
        enqueue(Q, ch)

    for i in range(Q.frontIdx, len(Q.items)):
        print(Q.items[i], end=" ")
    print()

    dequeue(Q)
    for i in range(Q.frontIdx, len(Q.items)):
        print(Q.items[i], end=" ")
    print()







