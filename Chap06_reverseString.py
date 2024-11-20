####################
# Chap06_reverseString.py
# 작성일: 2024-11-12
# 소프트웨어학과 32192406 심의진
####################

from Chap06_listStack import *

def reverse(str):
    st = ListStack()
    for i in range(len(str)):
        st.push(str[i])
    out = ''
    while not st.isEmpty():
        out += st.pop()
    return out

def main():
    input = "Test seq 12345"    # 테스트 입력 문자열
    answer = reverse(input)
    print("Input string: ", input)
    print("Reversed string: ", answer)
    
if __name__ == "__main__":
    main()