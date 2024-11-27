####################
# Chap08_heap.py
# 작성일: 2024-11-19
# 소프트웨어학과 32192406 심의진
####################

class Heap:
    def __init__(self, *args):
        if len(args) != 0:
            self.__A = args[0]  # 파라미터로 온 리스트
        else:
            self.__A = []
    
    # [알고리즘 8-2] 구현: 힙에 원소 삽입하기(재귀 알고리즘 버전)
    def insert(self, x):
        self.__A.append(x)
        self.__percolateUp(len(self.__A) - 1)
    
    # 스며오르기
    def __percolateUp(self, i: int):
        parent = (i - 1) // 2
        if i > 0 and self.__A[i] > self.__A[parent]:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            self.__percolateUp(parent)
    
    # [알고리즘 8-3] 구현: 힙에서 원소 삭제하기
    def deleteMax(self):
        # heap is in self.__A[0...len(self.__A)-1]
        if (not self.isEmpty()):
            max = self.__A[0]
            self.__A[0] = self.__A.pop()    # *.pop(0): 리스트의 끝원소 삭제 후 원소 리턴
            self.__percolateDown(0)
            return max
        else:
            return None
        
    # def deleteMax(self):
    #     # heap is in self.__A[0...len(self.__A)-1]
    #     if self.isEmpty():
    #         return None  # 힙이 비어있을 때 None을 반환
    #     max_value = self.__A[0]
    #     # 맨 마지막 원소를 루트로 이동
    #     self.__A[0] = self.__A.pop()    
    #     self.__percolateDown(0)
    #     return max_value
        
    # 스며내리기
    def __percolateDown(self, i: int):
        # Percolate down w/ self.__[A] as the root
        child = 2 * i + 1   # left child
        right = 2 * i + 2   # right child
        if (child <= len(self.__A) - 1):
            if (right <= len(self.__A) - 1 and self.__A[child] < self.__A[right]):
                child = right   # index of larger child
            if self.__A[i] < self.__A[child]:
                self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
                self.__percolateDown(child)
    
    def max(self):
        return self.__A[0]
    
    # 힙 만들기
    def buildHeap(self):
        for i in range((len(self.__A) - 2) // 2, -1, -1):
            self.__percolateDown(i)
    
    # 힙이 비었는지 확인하기
    def isEmpty(self) -> bool:
        return len(self.__A) == 0
    
    def clear(self):
        self.__A = []

    def size(self) -> int:
        return len(self.__A)
    
    # 힙의 트리 구조를 시각적으로 출력하는 함수
    def printHeapStructure(self):
        def _printTree(index, level):
            if index < len(self.__A):  # 힙의 원소가 있는 범위 내에서
                _printTree(2 * index + 2, level + 1)  # 오른쪽 자식
                print("   " * level + str(self.__A[index]))  # 현재 노드
                _printTree(2 * index + 1, level + 1)  # 왼쪽 자식

        print("힙 트리 구조:")
        _printTree(0, 0)
        print("----------")