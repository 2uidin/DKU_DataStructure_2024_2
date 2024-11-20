####################
# Chap06_listStackDemo.py
# 작성일: 2024-11-11
# 소프트웨어학과 32192406 심의진
####################

from Chap06_listStack import *

st1 = ListStack()
print(st1.top())    # No effect
st1.push(100)
st1.push(200)
print("Top is", st1.top())
st1.pop()
st1.push('Monday')
st1.printStack()
print('isEmpty?', st1.isEmpty())