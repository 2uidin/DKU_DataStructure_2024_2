####################
# Chap09_bucketSort.py
# 작성일: 2024-11-20
# 소프트웨어학과 32192406 심의진
####################

import math
from insertionSort import insertionSort

def bucketSort(A):
    n = len(A)
    B =[[] for _ in range(n)]
    for i in range(n):
        B[math.floor(n*A[i])].append(A[i])
    A.clear()
    for i in range(n):
        insertionSort(B[i])
        A.extend(B[i])