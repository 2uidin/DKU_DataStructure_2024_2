####################
# Chap05_linkedListBasic.py
# 작성일: 2024-11-08
# 소프트웨어학과 32192406 심의진
####################

from Chap05_listNode import ListNode

class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__numItems = 0

    # [알고리즘 5-2] 구현: 연결리스트에 원소 삽입하기(더미 헤드를 두는 대표 버전)
    def insert(self, i: int, newItem):
        if i >= 0 and i <= self.__numItems:
            prev = self.__getNode(i - 1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems += 1
        else:
            print("index", i, ": out of bound in insert()") # 필요 시 에러 처리
            
    def append(self, newItem):
        prev = self.__getNode(self.__numItems - 1)
        newNode = ListNode(newItem, prev.next)
        prev.next = newNode
        self.__numItems += 1
        
    # [알고리즘 5-3] 구현: 연결 리스트의 원소 삭제하기
    def pop(self, i: int):  # i번 노드 삭제. 고정 파라미터
        if(i >= 0 and i <= self.__numItems - 1):
            prev = self.__getNode(i - 1)
            curr = prev.next
            prev.next = curr.next
            retItem = curr.item
            self.__numItems -= 1
            return retItem
        else:
            return None
        
    # [알고리즘 5-4] 구현: 연결리스트의 원소 x 삭제하기 (더미 헤드를 두는 대표 버전)
    def remove(self, x):
        (prev, curr) = self.__findNode(x)
        if curr != None:
            prev.next = curr.next
            self.__numItems -= 1
            return x
        else:
            return None
        
    # [알고리즘 5-5] 구현: 연결 리스트의 i번 원소 알려주기
    def get(self, i: int):
        if self.isEmpty():
            return None
        if(i >= 0 and i <= self.__numItems - 1):
            return self.__getNode(i).item
        else:
            return None
        
    # [알고리즘 5-7] 구현: x가 연결 리스트의 몇 번 원소인지 알려주기
    def index(self, x) -> int:
        curr = self.__head.next
        for index in range(self.__numItems):
            if curr.item == x:
                return index
            else:
                curr = curr.next
        return -12345   # 안 쓰는 인덱스

    # [알고리즘 5-8] 구현: 기타 작업들
    def isEmpty(self) -> bool:
        return self.__numItems == 0

    def size(self) -> int:
        return self.__numItems

    def clear(self):
        self.__head = ListNode("dummy", None)
        self.__numItems = 0
        
    def count(self, x) -> int:
        cnt = 0
        curr = self.__head.next # 0번 노드
        while curr != None:
            if curr.item == x:
                cnt += 1
            curr = curr.next
        return cnt

    def extend(self, a):    # 여기서 a는 self와 같은 타입의 리스트
        for index in range(a.size()):
            self.append(a.get(index))
            
    def copy(self):
        a = LinkedListBasic()
        for index in range(self.__numItems):
            a.append(self.get(index))
        return a

    def reverse(self):
        a = LinkedListBasic()
        for index in range(self.__numItems):
            a.insert(0, self.get(index))
        self.clear()
        for index in range(a.size()):
            self.append(a.get(index))
            
    def sort(self) -> None:
        a = []
        for index in range(self.__numItems):
            a.append(self.get(index))
        a.sort()
        self.clear()
        for index in range(len(a)):
            self.append(a[index])
            
    def __findNode(self, x) -> (ListNode, ListNode):    # type: ignore
        prev = self.__head  # 더미 헤드
        curr = prev.next    # 0번 노드
        while curr != None:
            if curr.item == x:
                return (prev, curr)
            else:
                prev = curr; curr = curr.next
        return (None, None)

    # [알고리즘 5-6] 구현: 연결 리스트의 i번 노드 알려주기
    def __getNode(self, i: int) -> ListNode:
        curr = self.__head  # 더미 헤드, index: -1
        for index in range(i + 1):
            curr = curr.next
        return curr

    def printList(self):
        curr = self.__head.next # 0번 노드: 더미 헤드 다음 노드
        while curr != None:
            print(curr.item, end = ' ')
            curr = curr.next
        print()