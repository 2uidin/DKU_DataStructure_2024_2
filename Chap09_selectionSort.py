####################
# Chap09_selectionSort.py
# 작성일: 2024-11-19
# 소프트웨어학과 32192406 심의진
####################

def selectionSort(A):
    for last in range(len(A) - 1, 0, -1):
        k = theLargest(A, last) # A[0...last] 중 가장 큰 수 A[k] 찾기
        A[k], A[last] = A[last], A[k]
        print(f"Step {len(A) - last}: {A}")  # 단계별 배열 출력

def theLargest(A, last: int) -> int:    # A[0...last]에서 가장 큰 수의 인덱스를 리턴한다
    largest = 0
    for i in range(last + 1):
        if A[i] > A[largest]:
            largest = i
    return largest

# 예제 실행
array = [8, 31, 48, 73, 65, 20, 29, 11, 15]
print("Initial array:", array)
selectionSort(array)
print("Sorted array:", array)