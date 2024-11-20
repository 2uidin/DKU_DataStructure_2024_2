####################
# Chap05_listNode.py
# 작성일: 2024-11-08
# 소프트웨어학과 32192406 심의진
####################

class ListNode:
    def __init__(self, newItem, nextNode: 'ListNode'):
        self.item = newItem
        self.next = nextNode