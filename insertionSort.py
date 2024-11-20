####################
# Chap09_insertionSort.py
# 작성일: 2024-11-19
# 소프트웨어학과 32192406 심의진
####################

def insertionSort(A):
    for i in range(1, len(A)):
        loc = i - 1
        newItem = A[i]
        while loc >= 0 and newItem < A[loc]:
            A[loc + 1] = A[loc]
            loc -= 1
        A[loc + 1] = newItem