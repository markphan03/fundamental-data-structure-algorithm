"""
    The general Stack data structure uses arrays
    - All Stack operations have a time complexity of O(1).
    @Author: Mark Phan
    Adapted from: Bui Viet Ha - Nhap Mon Thuat Toan

"""

class Stack():
    def __init__(self):
        self.items = []


def isEmpty(S):
    return len(S.items) == 0


def Push(S, x):
    S.items.append(x)


def Pop(S):
    if isEmpty(S):
        raise RuntimeError("Stack is empty")
    topIdx = len(S.items) - 1
    x = S.items[topIdx]
    del S.items[topIdx]
    return x


def Top(S):
    if isEmpty(S):
        raise RuntimeError("Stack is empty")
    topIdx = len(S.items) - 1
    x = S.items[topIdx]
    return x

