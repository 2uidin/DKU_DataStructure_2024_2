####################
# Chap07_listQueue.py
# 작성일: 2024-11-19
# 소프트웨어학과 32192406 심의진
####################

class ListQueue:
    def __init__(self):
        self.__queue = []
    
    def enqueue(self, x):
        self.__queue.append(x)
    
    def dequeue(self):
        return self.__queue.pop(0)  #.pop(0): 리스트의 첫 원소를 삭제한 후 원소 리턴
    
    def front(self):
        if self.isEmpty():
            return None
        else:
            return self.__queue[0]
        
    def isEmpty(self) -> bool:
        return (len(self.__queue) == 0)
    
    def dequeueAll(self):
        self.__queue.clear()

    def printQueue(self):
        print("Queue from front:", end= ' ')
        for i in range(len(self.__queue)):
            print(self.__queue[i], end = ' ')
        print()