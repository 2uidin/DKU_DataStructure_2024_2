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
        print(f"Step {len(A) - numElements + 1}: {A}")  # 단계별 배열 출력

# 예제 실행
array = [3, 31, 48, 73, 8, 11, 20, 29, 65, 15]
print("Initial array:", array)
bubbleSort(array)
print("Sorted array:", array)