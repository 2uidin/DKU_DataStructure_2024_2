####################
# Chap07_palindrome.py
# 작성일: 2024-11-19
# 소프트웨어학과 32192406 심의진
####################

from Chap06_listStack import *
from Chap07_listQueue import *

def isPalindrome(A) -> bool:
    s = ListStack(); q = ListQueue()
    for i in range(len(A)):
        s.push(A[i]); q.enqueue(A[i])
    while (not q.isEmpty()) and s.pop() == q.dequeue():
        {}
    if q.isEmpty():
        return True
    else:
        return False

def main():
    print("Palindrome Check!")
    str = 'lioninoil'   # 테스트 문자열
    t = isPalindrome(str)
    print(str, " is Palindrome?: ", t)

if __name__ == "__main__":
    main()