####################
# Chap10_binarySearchTree.py
# 작성일: 2024-11-20
# 소프트웨어학과 32192406 심의진
####################

class TreeNode:
    def __init__(self, newItem, left=None, right=None):
        self.item = newItem
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.__root = None

    # [알고리즘 10-1] 구현: 탐색
    def search(self, x) -> TreeNode:
        return self.__searchItem(self.__root, x)

    def __searchItem(self, tNode: TreeNode, x) -> TreeNode:
        if (tNode == None):
            return None
        elif (x == tNode.item):
            return tNode
        elif (x < tNode.item):
            return self.__searchItem(tNode.left, x)
        else:
            return self.__searchItem(tNode.right, x)

    # [알고리즘 10-3] 구현: 삽입
    def insert(self, newItem):
        self.__root = self.__insertItem(self.__root, newItem)

    def __insertItem(self, tNode: TreeNode, newItem) -> TreeNode:
        if (tNode == None):
            tNode = TreeNode(newItem)
        elif (newItem < tNode.item):    # branch left
            tNode.left = self.__insertItem(tNode.left, newItem)
        else:                           # branch right
            tNode.right = self.__insertItem(tNode.right, newItem)
        return tNode

    # [알고리즘 10-7] 구현: 삭제
    def delete(self, x):
        self.__root = self.__deleteItem(self.__root, x)

    def __deleteItem(self, tNode: TreeNode, x) -> TreeNode:
        if (tNode == None):
            return None         # Error! Item not found
        elif (x == tNode.item): # item found!
            tNode = self.__deleteNode(tNode)
        elif (x < tNode.item):
            tNode.left = self.__deleteItem(tNode.left, x)
        else:
            tNode.right = self.__deleteItem(tNode.right, x)
        return tNode

    def __deleteNode(self, tNode: TreeNode) -> TreeNode:
        if tNode.left == None and tNode.right == None:  # case 1 (leaf node)
            return None
        elif tNode.left == None:    # case 2 (only right child)
            return tNode.right
        elif tNode.right == None:   # case 2 (only left child)
            return tNode.left
        else:   # case 3 (two children)
            (rtnItem, rtnNode) = self.__deleteMinItem(tNode.right)
            tNode.item = rtnItem
            tNode.right = rtnNode
            return tNode

    def __deleteMinItem(self, tNode: TreeNode) -> tuple:
        if tNode.left == None:
            return (tNode.item, tNode.right)
        else:   # branch left
            (rtnItem, rtnNode) = self.__deleteMinItem(tNode.left)
            tNode.left = rtnNode
            return (rtnItem, tNode)

    def printTreeStructure(self):
        def _printTree(node, depth=0):
            if node is not None:
                _printTree(node.right, depth + 1)  # 오른쪽 자식 먼저
                print("     " * depth + str(node.item))  # 현재 노드
                _printTree(node.left, depth + 1)  # 왼쪽 자식

        print("\n이진 검색 트리 구조:")
        _printTree(self.__root)
        print("----------")

    # 기타
    def isEmpty(self) -> bool:
        return self.__root == None

    def clear(self):
        self.__root = None
