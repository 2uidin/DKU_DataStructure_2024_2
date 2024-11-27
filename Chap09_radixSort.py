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
        print(f"Sorting by 10^{i} place:")
        for x in A:
            y = (x // 10**i) % 10
            bucket[y].append(x)
        A.clear()
        for j in range(10):
            A.extend(bucket[j])
            # print(f"Bucket {j}: {bucket[j]}")
            bucket[j].clear()
        print(f"Array after sorting by {i + 1} digit: {A}\n")

# 예제 실행
array = [123, 2154, 222, 4, 283, 1560, 1061, 2150]
print("Initial array:", array)
radixSort(array)
print("Sorted array:", array)