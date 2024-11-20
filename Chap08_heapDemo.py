####################
# Chap08_heapDemo.py
# 작성일: 2024-11-19
# 소프트웨어학과 32192406 심의진
####################

from Chap08_heap import *

h1 = Heap([1, 11, 9, 2, 3])
h1.buildHeap()
h1.clear()
h1.insert(7)
h1.insert(5)
h1.insert(9)
h1.insert(4)
h1.insert(11)
h1.insert(19)
h1.insert(20)
h1.insert(21)
h1.insert(11)
h1.printHeapStructure()
h1.deleteMax()
h1.printHeapStructure()