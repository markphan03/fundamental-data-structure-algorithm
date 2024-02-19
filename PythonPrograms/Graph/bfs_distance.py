from DataStructure.Queue import *

INF = float("inf")


def BuildGraph(fname):
    f = open(fname)
    n = int(f.readline())
    A = []
    for line in f:
        A.append([int(ch) for ch in line.split()])
    V = []
    for i in range(n):
        V.append(i)
    E = []
    for i in range(n):
        for j in range(i, n):
            if A[i][j] == 1:
                E.append({i, j})
    f.close()
    return n, V, E, A


def AdjList(A):
    n = len(A)
    Adj = []
    for i in range(n):
        tdj = []
        for j in range(n):
            if A[i][j] == 1:
                tdj.append(j)
        Adj.append(tdj)
    return Adj


def BFS(s):
    Q = Queue()
    d[s] = 0
    enqueue(Q, (None, s))
    while not isEmpty(Q):
        p, v = dequeue(Q)
        if not mark[v]:
            mark[v] = True
            prev[v] = p
            if v != s:  # to avoid p := None in the first iteration
                d[v] = d[p] + 1
            for u in Adj[v]:
                enqueue(Q, (v, u))


def BFS_2(s):
    """
    This algorithm is taken inspiration from the book - Introduction to Algorithms by Thomas H. Cormen.
    Idea:
        Mark the vertices before enqueue them to the Queue.
    """
    Q = Queue()
    mark[s] = True
    d[s] = 0
    enqueue(Q, s)
    while not isEmpty(Q):
        v = dequeue(Q)
        for u in Adj[v]:
            if not mark[u]:
                mark[u] = True
                prev[u] = v
                d[u] = d[v] + 1
                enqueue(Q, u)


def printpath_1(s, t):
    """
        Dựa theo:
            s -> .. -> prev[prev[t]] -> prev[t] -> t
        Để thiết lập truy tìm theo đệ quy
    """
    if t == s:
        print(name[s], end=" ")
    else:
        if prev[t] == None:
            print("Không tồn tại đường đi", end=" ")
        else:
            printpath_1(s, prev[t])
            print("->", name[t], end=" ")


def printpath_2(s, t):
    q = []
    while t != None:
        q.append(t)
        t = prev[t]
    if s not in q:
        print("Không tồn tại đường đi", end=" ")
    else:
        q = q[::-1]  # reverse q
        for i in range(len(q)):
            print(name[q[i]], end=" ")
            if i < len(q) - 1:
                print("->", end=" ")


if __name__ == '__main__':
    name = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    fname = "data.inp"
    n, V, E, A = BuildGraph(fname)
    Adj = AdjList(A)
    s = 0
    mark = [False] * n
    prev = [None] * n
    d = [INF] * n
    BFS(s)
    print(prev)
    for t in range(0, n):
        print("path", name[s], "to", name[t], d[t], ":", end=" ")
        printpath_2(s, t)
        print()

    print("-----------------------------------")
    BFS_2(s)
    print(prev)
    for t in range(0, n):
        print("path", name[s], "to", name[t], d[t], ":", end=" ")
        printpath_2(s, t)
        print()
