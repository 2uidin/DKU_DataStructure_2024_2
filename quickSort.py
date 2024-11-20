####################
# Chap09_quickSort.py
# 작성일: 2024-11-19
# 소프트웨어학과 32192406 심의진
####################

def quickSort(A, p: int, r: int):
    if p < r:
        q = partition(A, p, r)  # 분할
        quickSort(A, p, q-1)    # 왼쪽 부분 리스트 정렬
        quickSort(A, q+1, r)    # 오른쪽 부분 리스트 정렬

def partition(A, p: int, r: int) -> int:
    x = A[r]                # x: 기준 원소
    i = p - 1               # i: 1구역의 끝 지점
    for j in range(p, r):   # j: 3구역의 시작 지점
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i] # 교환
    A[i+1], A[r] = A[r], A[i+1]     # 기준 원소와 2구역 첫 원소 교환
    return i+1