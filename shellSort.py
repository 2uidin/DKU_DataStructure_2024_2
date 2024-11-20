####################
# Chap09_shellSort.py
# 작성일: 2024-11-19
# 소프트웨어학과 32192406 심의진
####################

def shellSort(A):   # A[0...n-1]: 정렬할 리스트
    H = gapSequence(len(A))