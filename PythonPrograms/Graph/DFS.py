"""
Thuật toán DFS tổng quát cho đồ thị vô hướng sử dụng mảng đánh dấu và Stack, với input là Ma trận 1/0
"""
from DataStructure.Stack import *

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

    return n, V, E, A


def AdjList(A):
    n = len(A)
    Adj = []
    for i in range(n):
        nodes_adj = []
        for j in range(n):
            if A[i][j] == 1:
                nodes_adj.append(j)
        Adj.append(nodes_adj)
    return Adj


def DFS(s):
    S = Stack()
    Push(S, (None, s))
    while not isEmpty(S):
        p, v = Pop(S)
        if not mark[v]:
            mark[v] = True
            prev[v] = p
            for u in Adj[v]:
                Push(S, (v, u))

def printpath_1(src, dest):
    if (dest == src):
        print(name[src], end=" ")
    else:
        if prev[dest] == None:
            print("Path does not exist")
        else:
            printpath_1(src, prev[dest])
            print("->", name[dest], end=" ")


def printpath_2(src, dest):
    path = []
    while dest != None:
        path.append(dest)
        dest = prev[dest]
    if src not in path:
        print("Path does not exist")
    else:
        path = path[::-1] # reverse path
        for i in range(len(path)):
            print(name[path[i]], end=" ")
            if i < len(path) - 1:
                print("->", end=" ")

if __name__ == '__main__':
    name = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    fname = "data.inp"
    n, V, E, A = BuildGraph(fname)
    Adj = AdjList(A)
    s = 4
    mark = [False]*n
    prev = [None]*n
    DFS(s)
    for t in range(0, n):
        print("path", name[s], name[t], ":", end=" ")
        printpath_2(s, t)
        print()

