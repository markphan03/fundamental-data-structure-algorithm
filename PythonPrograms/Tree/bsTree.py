class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


def RNode_Search(x, K):
    """
    recursive node search.
    :param x: current node
    :param K: key of the search node
    :return: search node
    """
    if x == None:
        return None
    elif x.key == K:
        return x
    elif x.key > K:
        return RNode_Search(x.left, K)
    else:
        return RNode_Search(x.right, K)


def INode_Search(x, K):
    """
    iterative node search.
    :param x: current node
    :param K: key of the search node
    :return: search node
    """
    while x != None and x.key == K:
        if x.key > K:
            x = x.left
        else:
            x = x.right
    return x


class Tree:
    def __init__(self, key=None):
        if key == None:
            self.root = None
        else:
            self.root = Node(key)


def Tree_Search(T, K):
    x = T.root
    return INode_Search(x, K)


def Tree_Search_2(T, K):
    x = T.root
    while x != None and x.key == K:
        if x.key > K:
            x = x.left
        else:
            x = x.right
    return x


def Tree_Insert(T, K):
    """
    Procedure:
    - Keep finding the parent node to insert. By declaring two variables y, x, and let x keep going left or
    right until x is NULL
    - When x is NULL, we know that y is the parent of x
    - create a new Node z for K
    - Some conditions to consider when inserting z:
        + Tree is empty
        + K > y.key
        + K < y.key
    :param T: Tree
    :param K: the key value
    :return: void
    """
    y = None
    x = T.root
    is_node_exist = False
    while x != None:
        y = x
        if K == x.key:
            is_node_exist = True
        elif K < x.key:
            x = x.left
        else:
            x = x.right
    if not is_node_exist:
        node = Node(K)
        node.parent = y
        if y == None:  # Tree is empty
            T.root = node
        else:
            if K < y.key:
                y.left = node
            else:
                y.right = node


def Tree_Insert_Node(T, z):
    """
    Procedure should be somewhat the same as the Tree insert function above
    :param T: Bs Tree
    :param z: a node has value needs to insert
    :return:
    """

    y = None
    x = T.root
    is_node_existed = False
    while x != None:
        y = x
        if x.key == z.key:
            is_node_existed = True
        elif z.key < x.key:
            x = x.left
        else:
            x = x.right
    if not is_node_existed:
        z.p = y
        if y == None:
            T.root = y
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z


def RTree_Insertion(T, K, x, y):
    """
    Recursive tree insertion
    :param T:
    :param K:
    :return:
    """
    if x == None:
        node = Node(K)
        node.p = y
        if y == None:
            T.root = y
        else:
            if K < y.key:
                y.left = node
            else:
                y.right = Node
    else:
        y = x
        if K < x.key:
            RTree_Insertion(T, K, x.left, y)
        else:
            RTree_Insertion(T, K, x.right, y)


def RTree_Insertion_2(T, K, x, y):
    """
    Recursive tree insertion
    :param T:
    :param K:
    :return:
    """
    if x != None:
        y = x
        if K < x.key:
            RTree_Insertion(T, K, x.left, y)
        else:
            RTree_Insertion(T, K, x.right, y)
    else:
        node = Node(K)
        node.p = y
        if y == None:
            T.root = y
        else:
            if K < y.key:
                y.left = node
            else:
                y.right = Node


def node_preorder(x):
    """
    Traverse the root first, then all node in left branch from the current node x, then traverse the
    nodes from right branch.
    :param x:
    :return:
    """
    if x != None:
        print(x.key, end=" ")
        node_preorder(x.left)
        node_preorder(x.right)


def node_postorder(x):
    """
    Thứ tự duyệt từ node lá lên từ nhánh trái qua nhánh phải, và cuối cùng sẽ duyệt gốc (root)
    :param x:
    :return:
    """
    if x != None:
        node_postorder(x.left)
        node_postorder(x.right)
        print(x.key, end=" ")


def node_inorder(x):
    """
    Inorder traversal will traverse all the nodes in increment order of their keys.
    Ex: 1, 2, 3, 4, 5
    :param x:
    :return:
    """
    if x != None:
        node_inorder(x.left)
        print(x.key, end=" ")
        node_inorder(x.right)


def Tree_preorder(T):
    node_preorder(T.root)


def Tree_postorder(T):
    node_postorder(T.root)


def Tree_inorder(T):
    node_inorder(T.root)


def BSTSort(A):
    """
    Sort all element in A in order, and print them out using BSTree properties.
    Time complexity: O(nlogn) - average case, O(n^2) - worst case
    :param A: an array of element
    :return: void
    """
    T = Tree()
    for k in A:
        Tree_Insert(T, k)
    Tree_inorder(T)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Hello World')
