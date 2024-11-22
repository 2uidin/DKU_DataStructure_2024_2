####################
# Chap09_bucketSort.py
# 작성일: 2024-11-20
# 소프트웨어학과 32192406 심의진
####################

import math
from Chap09_insertionSort import insertionSort

def bucketSort(A):
    n = len(A)
    B =[[] for _ in range(n)]
    for i in range(n):
        B[math.floor(n*A[i])].append(A[i])
    A.clear()
    for i in range(n):
        insertionSort(B[i])
        print(f"Bucket {i}: {B[i]}")
        A.extend(B[i])
        
# 예제 실행
array = [.38, .94, .48, .73, .99, .43, .55, .15, .85, .84, .81, .71, .17, .10, .02]
print("Initial array:", array)
bucketSort(array)
print("Sorted array:", array)