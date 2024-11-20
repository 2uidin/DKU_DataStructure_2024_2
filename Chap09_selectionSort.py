####################
# Chap09_selectionSort.py
# 작성일: 2024-11-19
# 소프트웨어학과 32192406 심의진
####################

def selectionSort(A):
    for last in range(len(A) - 1, 0, -1):
        k = theLargest(A, last) # A[0...last] 중 가장 큰 수 A[k] 찾기
        A[k], A[last] = A[last], A[k]

def theLargest(A, last: int) -> int:    # A[0...last]에서 가장 큰 수의 인덱스를 리턴한다
    largest = 0
    for i in range(last + 1):
        if A[i] > A[largest]:
            largest = 1
    return largest