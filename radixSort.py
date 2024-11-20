####################
# Chap09_radixSort.py
# 작성일: 2024-11-20
# 소프트웨어학과 32192406 심의진
####################

import math

def radixSort(A):
    maxValue = max(A)
    numDigits = math.ceil(math.log10(maxValue)) # 자릿수 계산
    bucket =[[] for _ in range(10)] # 0, 1, ..., 9에 대한 10개의 리스트
    for i in range(numDigits):
        for x in A:
            y = (x // 10**i) % 10
            bucket[y].append(x)
        A.clear()
        for j in range(10):
            A.extend(bucket[j])
            bucket[j].clear()