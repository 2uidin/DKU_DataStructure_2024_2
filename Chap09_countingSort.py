####################
# Chap09_countingSort.py
# 작성일: 2024-11-20
# 소프트웨어학과 32192406 심의진
####################

def countingSort(A):
    k = max(A)  # 리스트 A[...]에서 최댓값
    C = [0 for _ in range(k+1)]
    for j in range(len(A)):
        C[A[j]] += 1
    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]
    B = [0 for _ in range(len(A))]
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return B

# 예제 실행
array = [3, 2, 1, 4, 0, 2, 5, 1, 3, 4, 2, 0, 5, 1, 3]
print("Initial array:", array)
countingSort(array)
print("Sorted array:", array)