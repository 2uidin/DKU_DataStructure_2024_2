####################
# Chap11_AVLTree.py
# 작성일: 2024-11-20
# 소프트웨어학과 32192406 심의진
####################

class AVLNode:
    def __init__(self, newItem, left, right, h):
        self.item = newItem
        self.left = left
        self.right = right
        self.height = h

class AVLTree:
    def __init__(self):
        self.NIL = AVLNode(None, None, None, 0)
        self.__root = self.NIL
        self.LL = 1; self.LR = 2; self.RR = 3; self.RL = 4
        self.No_NEED = 0
        self.ILLEGAL = -1

    # [알고리즘 10-1] 구현: 탐색
    def search(self, x):
        return self.__searchItem(self.__root, x)
    
    def __searchItem(self, tNode: AVLNode, x) -> AVLNode:
        if (tNode == self.NIL):
            return self.NIL
        elif (x == tNode.item):
            return tNode
        elif (x < tNode.item):
            return self.__searchItem(tNode.left, x)
        else:
            return self.__searchItem(tNode.right, x)
        
    # [알고리즘 10-3] 구현: 삽입
    def insert(self, x):
        self.__root = self.__insertItem(self.__root, x)

    def __insertItem(self, tNode: AVLNode, x) -> AVLNode:
        if (tNode == self.NIL): # insert after a leaf(or into an empty tree)
            tNode = AVLNode(x, self.NIL, self.NIL, 1)
        elif (x < tNode.item):    # branch left
            tNode.left = self.__insertItem(tNode.left, x)
            tNode.height = 1 + max(tNode.right.height, tNode.left.height)
            type = self.__needBalance(tNode)
            if (type != self.No_NEED):
                tNode = self.__balanceAVL(tNode, type)
        else:                           # branch right
            tNode.right = self.__insertItem(tNode.right, x)
            tNode.height = 1+ max(tNode.right.right, tNode.left.height)
            type = self.__needBalance(tNode)
            if (type != self.No_NEED):
                tNode = self.__balanceAVL(tNode, type)
        return tNode
    
    # [알고리즘 10-7] 구현: 삭제
    def delete(self, x):
        self.__root = self.__deleteItem(self.__root, x)

    def __deletItem(self, tNode: AVLNode, x) -> AVLNode:
        if (tNode == self.NIL):
            return self.NIL         # Item not found!
        else:
            if x == tNode.item:     #item found at tNode
                tNode = self.__deleteNode(tNode)
            elif x < tNode.item:
                tNode.left = self.__deleteItem(tNode.left, x)
                tNode.height = 1 + max(tNode.right.height, tNode.left.height)
                type = self.__needBalance(tNode)
                if type != self.No_NEED:
                    tNode = self.__balanceAVL(tNode, type)
            else:
                tNode.right = self.__deleteItem(tNode.right, x)
                tNode.height = 1 + max(tNode.right.height, tNode.left.height)
                type = self.__needBalance(tNode)
                if type != self.No_NEED:
                    tNode = self.__balanceAVL(tNode, type)
            return tNode
    
    def __deleteNode(self, tNode: AVLNode) -> AVLNode:
        # 3가지 case
        #   1. tNode이 리프 노드
        #   2. tNode이 자식이 하나만 있음
        #   3. tNode이 자식이 둘 있음
        if tNode.left == self.NIL and tNode.right == self.NIL:  # case 1(자식이 없음)
            return self.NIL
        elif tNode.left == self.NIL:    # case 2(오른자식뿐)
            return tNode.right
        elif tNode.right == self.NIL:   # case 2(왼자식뿐)
            return tNode.left
        else:   # case 3(두 자식이 다 있음)
            (rtnItem, rtnNode) = self.__deleteMinItem(tNode.right)
            tNode.item = rtnItem
            tNode.right = rtnNode
            tNode.height = 1 + max(tNode.right.height, tNode.left.height)
            type = self.__needBalance(tNode)
            if type != self.No_NEED:
                tNode = self.__balanceAVL(tNode, type)
            return tNode    # tNode survived
        
    def __deleteMinItem(self, tNode: AVLNode) -> tuple:
        if tNode.left == self.NIL:
            # found min at tNode
            return (tNode.item, tNode.right)
        else:   # keep branching left, then backtrack
            (rtnItem, rtnNode) = self.__deleteMinItem(tNode.left)
            tNode.left = rtnNode
            tNode.height = 1 + max(tNode.right.height, tNode.left.height)
            type = self.__needBalance(tNode)
            if type != self.No_NEED:
                tNode = self.__balanceAVL(tNode, type)
            return (rtnItem, tNode)
    
    # 균형 잡기
    def __balanceAVL(self, tNode: AVLNode, type: int) -> AVLNode:
        returnNode = self.NIL
        if type == self.LL:
            returnNode = self.__rightRotate(tNode)
        elif type == self.LR:
            tNode.left = self.__leftRotate(tNode.left)
            returnNode = self.__rightRotate(tNode)
        elif type == self.RR:
            returnNode = self.__leftRotate(tNode.right)
        elif type == self.RL:
            tNode.right = self.__rightRotate(tNode.right)
            returnNode = self.__leftRotate(tNode)
        else:
            print("Impossible type! Should be one of LL, LR, RR, RL")
        return returnNode

    # [알고리즘 11-1] 구현 : 좌회전
    def __leftRotate(self, t: AVLNode) -> AVLNode:
        RChild = t.right
        if RChild == self.NIL:
            print(t.item, "'s RChild should't be NIL!")
        RLChild = RChild.left
        RChild.left = t
        t.right = RLChild
        t.height = 1 + max(t.left.height, t.right.height)
        RChild.height = 1 + max(RChild.left.height, RChild.right.height)
        return RChild

    # [알고리즘 11-2] 구현 : 우회전
    def __rightRotate(self, t: AVLNode) -> AVLNode:
        LChild = t.left
        if LChild == self.NIL:
            print(t.item, "'s LChild should't be NIL!")
        LRChild = LChild.right
        LChild.left = t
        t.left = LRChild
        t.height = 1 + max(t.left.height, t.right.height)
        LChild.height = 1 + max(LChild.left.height, LChild.right.height)
        return LChild

    def __needBalance(self, t: AVLNode) -> int:
        type = self.ILLEGAL
        if (t.left.height + 2) <= t.right.height:    # R 유형
            if (t.right.left.height <= t.right.right.height):
                type = self.RR
            else:
                type = self.RL
        elif t.left.height >= (t.right.height + 2):    # L 유형
            if (t.left.left.height >= t.left.right.height):
                type = self.LL
            else:
                type = self.LR
        else:
            type = self.No_NEED
        return type
    
    # 기타
    def isEmpty(self) -> bool:
        return self.__root == self.NIL
    
    def clear(self):
        self.__root = self.NIL