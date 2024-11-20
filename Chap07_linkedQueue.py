####################
# Chap07_linkedQueue.py
# 작성일: 2024-11-19
# 소프트웨어학과 32192406 심의진
####################

from Chap05_circularLinkedList import *

class LinkedQueue:
    def __init__(self):
        self.__queue = CircularLinkedList()

    def enqueue(self, x):
        self.__queue.append(x)
    
    def dequeue(self):
        return self.__queue.pop(0)  # .pop(0): 리스트의 첫 원소를 삭제한 후 원소 리턴
    
    def front(self):
        return self.__queue.get(0)  # .get(0): 리스트의 첫 원소 리턴
    
    def isEmpty(self) -> bool:
        return self.__queue.isEmpty()
    
    def dequeueAll(self):
        self.__queue.clear()

    def printQueue(self):
        print("Queue from front:", end = ' ')
        for i in range(self.__queue.size()):
            print(self.__queue.get(i), end = ' ')
        print()