"""
Minimum Priority Queue using concepts from Min Heap
@Author: Mark Phan
Adapted from: Bui Viet Ha - Nhap Mon Thuat Toan

Note: Changing sign in line 36, 38 (ShiftDown), and 47 (ShiftUp) will create Maximum Priority Queue
"""

MAX = float("inf")


def parent(k):
    return (k - 1) // 2


def left(k):
    return 2 * k + 1


def right(k):
    return 2 * k + 2


def size(Q):
    return len(Q) - 1


def ShiftDown(Q, i):
    s = size(Q)
    k = i
    incorrect_position = True
    while incorrect_position:
        j = k
        l = left(k)
        r = right(k)
        if l <= s and Q[k] > Q[l]:
            k = l
        if r <= s and Q[k] > Q[r]:
            k = r
        incorrect_position = j != k
        if incorrect_position:
            Q[j], Q[k] = Q[k], Q[j]


def ShiftUp(Q, i):
    k = i
    while k > 0 and Q[k] < Q[parent(k)]:
        j = parent(k)
        Q[j], Q[k] = Q[k], Q[j]
        k = j


def DecreaseKey(Q, i, key):
    """
    Giảm khóa của phần tử thứ i xuống giá trị mới key
    """
    if Q[i] < key:
        raise ValueError("key is greater than the value to be replaced")
    Q[i] = key
    ShiftUp(Q, i)


def Minimum(Q):
    return Q[0]


def ExtractMin(Q):
    n = len(Q) - 1
    Min = Q[0]
    Q[0] = Q[n]
    del Q[n]
    ShiftDown(Q, 0)  # Đưa giá trị mới về đúng vị trí của nó
    return Min


def Insert(Q, v):
    n = len(Q)
    Q.append(MAX)
    DecreaseKey(Q, n, v)


def Insert_2(Q, v):
    n = len(Q)
    Q.append(v)
    ShiftUp(Q, n)


def BuildMinQueue(S):
    Q = S.copy()
    n = len(Q)
    for i in range(n // 2, -1, -1):
        ShiftDown(Q, i)
    return Q


if __name__ == '__main__':
    A = [5, 7, 1, 9, 10, 12, 2, 0, -4, -6]
    Q = BuildMinQueue(A)
    print(Q)
    Insert(Q, -8)
    print(Q)
