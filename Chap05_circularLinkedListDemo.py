####################
# Chap05_circularLinkedListDemo.py
# 작성일: 2024-11-11
# 소프트웨어학과 32192406 심의진
####################

from Chap05_circularLinkedList import *

list = CircularLinkedList()
list.append(30); list.insert(0, 20)
a = [4, 3, 3, 2, 1]
list.extend(a)
list.reverse()
list.pop(0)
print("count(3):", list.count(3))
print("get(2):", list.get(2))
list.printList()