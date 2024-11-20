####################
# Chap09_heapSort1.py
# 작성일: 2024-11-19
# 소프트웨어학과 32192406 심의진
####################

from heap import *

def heapSort(A):
    B = [x for x in A]  # 리스트 복사
    h = Heap(B)
    h.buildHeap()
    for i in range(len(B)-1, -1, -1):
        A[i] = h.deleteMax()