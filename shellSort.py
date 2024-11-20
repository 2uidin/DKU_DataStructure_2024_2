####################
# Chap09_shellSort.py
# 작성일: 2024-11-20
# 소프트웨어학과 32192406 심의진
####################

def shellSort(A):   # A[0...n-1]: 정렬할 리스트
    H = gapSequence(len(A))
    for h in H: # H = [h0, h1, ..., 1]: 갭 수열
        for k in range(h):
            stepInsertSort(A, k, h)

def stepInsertSort(A, k: int, h: int):  # A[k, k+h, K+2h, ...]을 정렬한다
    for i in range(k + h, len(A), h):
        j = i - h
        newItem = A[i]
        # 이 지점에서 A[..., j-2h, j-h, j]는 이미 정렬되어 있는 상태임
        # A[..., j-2h, j-h, j, j + h]의 맞는 곳에 A[j+h]를 삽입한다.
        while 0 <= j and newItem < A[j]:
            A[j + h] = A[j]
            j -= h
        A[j + h] = newItem

def gapSequence(n: int) -> list:    # 갭 수열 만들기. 다양한 선택이 있음
    H = [1]; gap = 1
    while gap < n/5:
        gap = 3 * gap + 1
        H.append(gap)
    H.reverse()
    return H