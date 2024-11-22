####################
# Chap09_insertionSort.py
# 작성일: 2024-11-19
# 소프트웨어학과 32192406 심의진
####################

def insertionSort(A):
    for i in range(1, len(A)):
        loc = i - 1
        newItem = A[i]
        while loc >= 0 and newItem < A[loc]:
            A[loc + 1] = A[loc]
            loc -= 1
        A[loc + 1] = newItem
        if __name__ == "__main__":
            print(f"Step {i}: {A}")  # 단계별 배열 출력

# 예제 실행
if __name__ == "__main__":
    array = [3, 31, 48, 73, 8, 11, 20, 29, 65, 15]
    print("Initial array:", array)
    insertionSort(array)
    print("Sorted array:", array)