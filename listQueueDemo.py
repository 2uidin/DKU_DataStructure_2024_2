####################
# Chap07_listQueueDemo.py
# 작성일: 2024-11-19
# 소프트웨어학과 32192406 심의진
####################

from listQueue import *

q1 = ListQueue()
q1.enqueue("Mon")
q1.enqueue("Tue")
q1.enqueue(1234)
q1.enqueue("Wed")
q1.dequeue()
q1.enqueue('aaa')
q1.printQueue()