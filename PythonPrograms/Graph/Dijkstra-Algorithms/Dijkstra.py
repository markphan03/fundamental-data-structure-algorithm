fdata = "graph.dat"
fweight = "weight.dat"
INF = float("inf")
name = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from minPriorityQueue import *


def BuildGraph(fdata, fwdata):
    f = open(fdata)
    n = int(f.readline())
    # create graph matrix
    A = []
    for i in range(n):
        line = f.readline()
        line = line.split()
        for k in range(len(line)):
            line[k] = int(line[k])
        A.append(line)
    f.close()
    # create weight matrix
    f = open(fwdata)
    W = []
    for i in range(n):
        line = f.readline()
        line = line.split()
        for k in range(len(line)):
            line[k] = int(line[k])
        W.append(line)
    f.close()
    # create vertices
    V = []
    for i in range(n):
        V.append(i)
    # create edges
    E = []
    for i in range(n):
        for j in range(n):
            if A[i][j] == 1:
                E.append((i, j))

    return n, V, E, A, W


def AdjList(A):
    n = len(A)
    Adj = []
    for i in range(n):
        adj_vertices = []
        for j in range(n):
            if A[i][j] == 1:
                adj_vertices.append(j)
        Adj.append(adj_vertices)
    return Adj


def Relax(u, v):
    """
    Hàm này có chức năng là update dist tử s -> v và update đỉnh trước (previous's vertex) của v là u.
    """
    if d[v] > d[u] + W[u][v]:
        d[v] = d[u] + W[u][v]
        prev[v] = u


def Dijkstra_traditional(s):  # O((V + E)logV)
    d[s] = 0
    q = []
    for v in V:
        q.append([v, d[v]])
    Q = BuildQueue(q)
    while len(Q) > 0:
        u, du = ExtractMin(Q)
        mark[u] = True
        for v in Adj[u]:
            if not mark[v]:
                if d[v] > d[u] + W[u][v]:
                    Relax(u, v)
                    i = getvalues(v)
                    DecreaseKey(Q, i, d[v])


def Dijkstra_bfs(s):
    d[s] = 0
    Q = minQueue()
    Insert(Q, [s, 0])
    while len(Q) > 0:
        u, du = ExtractMin(Q)
        mark[u] = True
        for v in Adj[u]:
            if not mark[v]:
                if d[v] > d[u] + W[u][v]:
                    Relax(u, v)
                    i = findIndex(v)
                    if i >= 0:
                        DecreaseKey(Q, i, d[v])
                    else:
                        Insert(Q, [v, d[v]])


def ShowPath(s, v):
    if s == v:
        print(name[s], end=" ")
    else:
        if prev[v] == None:
            print("Path does not exist!")
        else:
            ShowPath(s, prev[v])
            print("-->", name[v], end=" ")


if __name__ == "__main__":
    n, V, E, A, W = BuildGraph(fdata, fweight)
    Adj = AdjList(A)
    mark = [False] * n
    prev = [None] * n
    d = [INF] * n
    s = 0
    Dijkstra_bfs(s)
    for v in V:
        print(d[v], end=" ")
        ShowPath(s, v)
        print()
