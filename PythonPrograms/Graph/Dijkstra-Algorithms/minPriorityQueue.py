# Thiết lập Indexed Min Priority Queue dùng cho Dijkstra algorithm

# Các phần tử của Qcos dạng [v, d[v]] và giá trị được tính theo d[v]


"""
keys = dict mapping v --> index ò v in Q[][0], at first keys[Q[i][0]] = i
Example:
    key = {
        v1: 7
        ...
        v6: 1
    }

    Nếu gọi lệnh Swap keys[v1], keys[v6] = keys[v6], keys[v1], thì keys sẽ trở thành:
    key = {
        v1: 1
        ...
        v6 = 7
    }
"""
INF = float("inf")
keys = dict() # tạo dictionary rỗng


def minQueue(): # dành cho Dijkstra_bfs
    return []

def parent(k):
    return (k-1)//2

def left(k):
    return 2*k+1

def right(k):
    return 2*k+2

def size(Q):
    return len(Q)-1

def ShiftDown(Q, i):
    s = size(Q)
    k = i
    incorrected_position = True
    while incorrected_position:
        # đặt j là vị trí của của k - nút đang xét.
        j = k
        l = left(k)
        r = right(k)
        if l <= s and Q[k][1] > Q[l][1]: # so sánh dựa theo distance d[v]
            k = l
        if r <= s and Q[k][1] > Q[r][1]:
            k = r
        incorrected_position = k != j
        if incorrected_position:
            Q[j], Q[k] = Q[k], Q[j]
            keys[Q[j][0]], keys[Q[k][0]] = keys[Q[k][0]], keys[Q[j][0]]  # Q[j][0] trả về vi (vertex)

def ShiftUp(Q, i):
    k = i
    while k > 0 and Q[k][1] < Q[parent(k)][1]:
        j = parent(k)
        Q[j], Q[k] = Q[k], Q[j]
        keys[Q[j][0]], keys[Q[k][0]] = keys[Q[k][0]], keys[Q[j][0]]
        k = j

def DecreaseKey(Q, i, key):
    if key > Q[i][1]:
        raise RuntimeError("Key is larger than value to be replaced!")
    Q[i][1] = key
    ShiftDown(Q, i)

def Minimum(Q):
    return Q[0]

def ExtractMin(Q):
    n = size(Q)
    del keys[Q[0][0]]
    Min = Q[0]
    Q[0] = Q[n]
    del Q[n]
    ShiftDown(Q, 0)
    return Min

def Insert(Q, p): # p in form [v, d[v]]
    n = len(Q)
    Q.append([p[0], INF])
    keys[p[0]] = n
    DecreaseKey(Q, n, p[1])

# BuildQueue takes O(n)
def BuildQueue(S=[]): # S is a matrix
    Q = S.copy()
    # Thiết lập keys
    for i in range(len(Q)):
        keys[Q[i][0]] = i
    n = len(Q)
    for i in range(n//2, -1, -1):
        ShiftDown(Q, i)
    return Q

def findIndex(v):
    """
    Tìm chỉ số tương ứng với cặp [v, d[v]] trong MinQueue, nếu ko tìm thấy thì trả lại -1. Thời gian: O(1)
    """
    return keys.get(v, -1)

def getvalues(v):
    """
    Trả lại chỉ số (index) của cặp [v, d[v]] trong MinQueue. Thời gian: O(1)
    """
    return keys[v]

