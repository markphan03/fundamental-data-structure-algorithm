"""
Cho đồ thị G không liên thông, cần tính số các thành phần liên thông và thông tin chi tiết của các thành phần liên thông
của G
    - C[] - thông tin chi tiếp các thành phần liên thông - dạng table [{1, 2, 5}, {3, 6}]
    - count - biến đếm các thành phần liên thông
    - comp[v], v in V, mảng mô tả chỉ số thành phần liên thông của G. comp[v] = k khi và chỉ khi v thuộc thành phần
    liên thông thứ k

Mô tả thuật toán:

* Mô tả theo kiểu của Kỹ thuật lập trình & Nhập môn lập trình, cần cho nó bài bản.

Bước 1: Chọn một v bất kì từ V. Nếu v chưa được duyệt, thì duyệt v bằng DFS, và phân loại v vào nhóm Connected Component
(liên thông) theo thứ tự (ConnectedComponent())

Bước 2: Lần lượt duyệt các nút kề nút v bằng DFS_extend, và phân loại các nút đấy vào nhóm Connected Component
(liên thông) cùng với v. (Các thao tác đều đc xử lý trong DFS_extend())

Bước 3: Chọn các nút còn lại và duyệt chúng theo như bước 1, 2 đến khi hết V.

Note: Có thể thay đổi để biến mỗi vertex là một custom Node. Thử tham khảo bài giảng của Brady và viết lại = Python/ C++.

"""
from DataStructure.Stack import *
from DataStructure.Queue import *

def ConnectedComponent():
    count = -1
    for v in V:
        if not mark[v]:
            count = count + 1
            C.append(set())
            DFS_extend(v, count) # BFS_extend(v, count)
    return count


def DFS_extend(s, count):
    S = Stack()
    C[count] = set()
    Push(S, s)
    while not isEmpty(S):
        v = Pop(S)
        if not mark[v]:
            mark[v] = True
            comp[v] = count
            C[count].add(v)
            for u in Adj[v]:
                Push(S, u)

def BFS_extend(s, count):
    Q = Queue()
    C[count] = set()
    enqueue(Q, s)
    while not isEmpty(Q):
        v = dequeue(Q)
        if not mark[v]:
            mark[v] = True
            comp[v] = count
            C[count].add(v)
            for u in Adj[v]:
                enqueue(Q, u)


if __name__ == '__main__':
    n, V, E, A = BuildGraph(fname)
    Adj = AdjList(A)
    count = 0
    comp = [0]*n
    mark = [False]*n
    C = []
    count = CC()
    print("Graph has", count, "connected components")
    for i in range(count):
        print("Connected component number", i+1, ":", end=" ")
        print(C[i])

