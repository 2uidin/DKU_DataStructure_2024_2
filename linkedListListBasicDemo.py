####################
# Chap05_linkedListListBasicDemo.py
# 작성일: 2024-11-08
# 소프트웨어학과 32192406 심의진
####################

from linkedListBasic import *

list = LinkedListBasic()
list.append(30); list.insert(0,20)
a =LinkedListBasic()
a.append(4); a.append(3); a.append(3); a.append(2); a.append(1)
list.extend(a)
list.reverse()
list.pop(0)
print('count(3):', list.count(3))
print('get(2):', list.get(2))
list.printList()