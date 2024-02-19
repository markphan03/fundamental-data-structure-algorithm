"""
Max Heap with array
@Author: Mark Phan
Adapted from: Bui Viet Ha - Nhap Mon Thuat Toan
"""


def parent(k):
    return (k - 1) // 2


def left(k):
    return 2 * k + 1


def right(k):
    return 2 * k + 2


def ShiftDown(A, i, n):
    incorrect_position = True
    while incorrect_position:
        l = left(i)
        r = right(i)
        Idx = i
        if l <= n and A[i] < A[l]:
            Idx = l
        if r <= n and A[Idx] < A[l]:
            Idx = r
        incorrect_position = Idx != i
        if incorrect_position:
            A[i], A[Idx] = A[Idx], A[i]
            i = Idx


def ShiftUp(A, i):
    while i > 0 and A[i] > A[parent(i)]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def buildMaxHeap(A):
    n = len(A) - 1
    for i in range(len(A) // 2, -1, -1):
        ShiftDown(A, i, n)


def maxHeapSort(A):
    """
    Algorithm description:
        -The following maxHeapSort(A) algorithm will sort array A in ascending order using max-heap.
        -Before sorting, you need to set transform A to max-heap in line 2
        -After this command, A is the max-heap, so A[0] will be the last element of A.
        -The sorting algorithm will alternately swap A[0] and the last element of the sequence (command line 4.)
        -Then use ShiftDown(A,0,n-2) to convert A[0] to its correct position.
        -The swap process continues for the new max-heap with n-2, n-3, n-k, ..., n-(n-1) elements, after each swap,
        The largest elements are moved last.
        -After n-1 steps as above, the sorting process ends.
    """
    buildMaxHeap(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        ShiftDown(A, 0, i - 1)
