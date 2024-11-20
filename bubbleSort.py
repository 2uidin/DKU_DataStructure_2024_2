####################
# Chap09_bubbleSort.py
# 작성일: 2024-11-19
# 소프트웨어학과 32192406 심의진
####################

def bubbleSort(A):
    for numElements in range(len(A), 0, -1):
        for i in range(numElements - 1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]