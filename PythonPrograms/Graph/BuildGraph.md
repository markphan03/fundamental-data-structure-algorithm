Here we will present different ways to build simple graph

# Đồ thị vô hướng 

# 1. Thiết lập đồ thị vô hướng từ danh sách kề

```
5
0 3
0 4 
1 2
1 3
2 4
```

Khác nhau về cách thiết lập ma trận số A và dãy danh sách cạnh E (Edge)
```
def newMatrix(n):
    A = []
    for i in range(n):
        A.append([0]*n)
    return A
    
def BuildGraph(fname):
    f = open(fname)
    n = int(f.readline())
    A = newMatrix(n)
    V = []
    for i in range(n):
        V.append(i)
    E = []
    for line in f:
        edge = [int(ch) for ch in line.split()]
       i, j = edge[0], edge[1]
       A[i][j] = 1
       A[j][i] = 1
       E.append({i, j})
    f.close()
    return n, V, E, A
```

# 2. Thiết lập đồ thị vô hướng từ ma trận kề

```
AdjMatrix.dat
5
0 0 0 1 1
0 0 1 1 0
0 1 0 0 1
1 1 0 0 0
1 0 1 0 0
```

```
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
        for j in range(i, n): # chỉ duyệt nửa tam giác trên 
            if A[i][j] == 1:
                E.append({i, j})
    f.close()
    return n, V, E, A
```


# Đồ thị có hướng

# 3. Thiết lập đồ thị có hướng từ ma trận kề
```
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
        for j in range(n): # duyệt hết matrix
            if A[i][j] == 1:
                E.append((i, j)) # tuple 
    f.close()
    return n, V, E, A
```

# 4. Thiết lập đồ thị có hướng từ danh sách kề

```
5
0 3
0 4 
1 2
1 3
2 4
```

Khác nhau về cách thiết lập ma trận số A và dãy danh sách cạnh E (Edge)
```
def newMatrix(n):
    A = []
    for i in range(n):
        A.append([0]*n)
    return A
    
def BuildGraph(fname):
    f = open(fname)
    n = int(f.readline())
    A = newMatrix()
    for line in f:
        A.append([int(ch) for ch in line.split()])
    V = []
    for i in range(n):
        V.append(i)
    E = []
    for line in f:
        edge = [int(ch) for ch in line.split()]
       i, j = edge[0], edge[1]
       A[i][j] = 1
       E.append((i, j))  # tuple 
    f.close()
    return n, V, E, A
```
