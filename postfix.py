####################
# Chap06_postfix.py
# 작성일: 2024-11-12
# 소프트웨어학과 32192406 심의진
####################

from listStack import *

def evaluate(p):
    s = ListStack()
    digitPreviously = False
    for i in range(len(p)):
        ch = p[i]   # i번 문자. 번호는 0번부터
        if ch.isdigit():    # ch가 숫자
            if digitPreviously:
                tmp = s.pop()
                tmp = 10 * tmp + (ord(ch) - ord('0'))
                s.push(tmp)
            else:
                s.push(ord(ch) - ord('0'))
                digitPreviously = True
        elif isOperator(ch):    # ch가 연산자
            s.push(operation(s.pop(), s.pop(), ch))
            digitPreviously = False
        else:   # ch가 공백
            digitPreviously = False
    return s.pop()

def isOperator(ch) -> bool:    # 연산자인가?
    return (ch == '+' or ch == '-' or ch == '*' or ch == '/')

def operation(opr2: int, opr1: int, ch) -> int: # 연산하기
    return {'+': opr1 + opr2, '-': opr1 - opr2, '*': opr1 * opr2, '/': opr1 // opr2}[ch]

def main():
    postfix = "700 3 47 + 6 * - 4 /"    # 테스트 샘플 입력(후위 표현식)
    print("Input string: ", postfix)
    answer = evaluate(postfix)
    print("Answer: ", answer)
    # print(ord('0'), ord('9'))
    
if __name__ == "__main__":
    main()