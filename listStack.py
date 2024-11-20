####################
# Chap06_listStack.py
# 작성일: 2024-11-11
# 소프트웨어학과 32192406 심의진
####################

class ListStack:
    def __init__(self):
        self.__stack = []
        
    def push(self, x):
        self.__stack.append(x)
        
    def pop(self):
        return self.__stack.pop()
    
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.__stack[-1]
    
    def isEmpty(self) -> bool:
        return not bool(self.__stack)
    
    def popALl(self):
        self.__stack.clear()
    
    def printStack(self):
        print("Stack from top:", end = ' ')
        for i in range(len(self.__stack) - 1, -1, -1):
            print(self.__stack[i], end = ' ')
        print()