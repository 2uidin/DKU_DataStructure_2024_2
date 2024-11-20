####################
# Chap05_circularDoublyLinkedListDemo.py
# 작성일: 2024-11-20
# 소프트웨어학과 32192406 심의진
####################

from Chap05_circularDoublyLinkedList import *

list = CircularDoublyLinkedList()
list.append(30); list.insert(0, 20)
a = [4, 3, 3, 2, 1]
list.extend(a)
list.reverse()
list.pop(0)
print("count(3):", list.count(3))
print("get(2):", list.get(2))
list.printList()