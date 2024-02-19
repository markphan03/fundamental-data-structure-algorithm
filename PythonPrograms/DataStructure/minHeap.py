"""
    Min Heap with array
    @Author: Mark Phan
    Adapted from: Bui Viet Ha - Nhap Mon Thuat Toan
    E.g: MinHeap - [1, 5, 2, 7, 10, 12, 19]
"""


def parent(k):
    return (k - 1) // 2


def left(k):
    return 2 * k + 1


def right(k):
    return 2 * k + 2


def ShiftDown(A, i, s):
    """
    Algorithm description:
        -Step 1: Compare with the left child node A[l], if A[i] > A[l] with the condition that the index of the left child node is less than the last index,
        then get the value of the left child node (Idx = l).
        -Step 2: If we know that node A[i] is greater than the left child node A[l] and A[l] is greater than the right child node A[r], then take the value
        of the right child node. Additionally, if A[i] <= A[l] and A[i] > A[r], then get the value of the right child node (Idx = r).
        -Step 3: Variable incorrect_position to detect if A[i] is in the wrong position. If so, then change the position of A[i] with
        A[Idx] (is the left or right child node), and update i = Idx for the next operation
        -Step 4: Repeat steps 1, 2, 3 until incorrect_postion = False

    :param A: an array
    :param i: a position needs to be shifted down
    :param s: usually the size of an array, but it can act like the maximum index i can be shift down
    :return void
    """
    incorrect_position = True
    while incorrect_position:
        l = left(i)
        r = right(i)
        Idx = i
        if l <= s and A[i] > A[l]:
            Idx = l
        if r <= s and A[Idx] > A[r]:
            Idx = r
        incorrect_position = Idx != i  # Check to see if Idx changes left or right from the old position i.
        if incorrect_position:
            A[i], A[Idx] = A[Idx], A[i]
            i = Idx


def ShiftDown_rec(A, i, n):
    l = left(i)
    r = right(i)
    Idx = i
    if l <= n and A[i] > A[l]:
        Idx = l
    print(Idx)
    print(r)
    if r <= n and A[Idx] > A[r]:
        Idx = r
    if Idx != i:  # if i is in the wrong position
        A[i], A[Idx] = A[Idx], A[i]
        ShiftDown_rec(A, Idx, n)


"""
Another way to write ShiftUp:
def ShiftUp(A, i):
    p = parent(i)
    while i > 0 and A[i] < A[p]:
        A[i], A[p]] = A[p], A[i]
        i = parent(i)
        p = parent(i)
"""


def ShiftUp(A, i):
    """
    The purpose of this algorithm is to push A[i] to a higher position because in minHeap, the smallest node will be taken first.
    Algorithm description:
        Continuously compare A[i] with parent node A[p] if i > 0 and A[i] < A[p], then swap A[i] and A[p], then update again
    i = p.
    """
    while i > 0 and A[i] < A[parent(i)]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


"""
*range(len(A) // 2, -1, -1)
starting point: len(A) // 2
stopping point: -1 (>=0)
increment: -1
"""


def buildMinHeap(A):
    s = len(A) - 1
    for i in range(len(A) // 2, -1, -1):  # for i = floor(n/2) to 0
        ShiftDown(A, i, s)


def ExtractMin(A):
    n = len(A) - 1
    Min = A[0]
    A[0] = A[n]
    del A[n]
    n = n - 1
    ShiftDown(A, 0, n)
    return Min


def minHeapSort(A):
    buildMinHeap(A)
    sortedList = []
    n = len(A)
    while len(sortedList) < n:
        Min = ExtractMin(A)
        sortedList.append(Min)
    return sortedList


if __name__ == '__main__':
    A = [1, 1, 1, 1, 1, 1, 1, 1]
    sortedList = minHeapSort(A)
    print(sortedList)
