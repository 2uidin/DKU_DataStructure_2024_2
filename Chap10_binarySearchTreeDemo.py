####################
# Chap10_binarySearchTreeDemo.py
# 작성일: 2024-11-20
# 소프트웨어학과 32192406 심의진
####################

from Chap10_binarySearchTree import *

bst1 = BinarySearchTree()
bst1.insert(10)
bst1.insert(20)
bst1.insert(5)
bst1.insert(80)
bst1.insert(90)
bst1.insert(7550)
bst1.insert(30)
bst1.insert(77)
bst1.insert(15)
bst1.insert(40)
bst1.printTreeStructure()
bst1.delete(7550)
bst1.delete(10)
bst1.printTreeStructure()