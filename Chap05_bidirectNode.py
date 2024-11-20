####################
# Chap05_bidirectNode.py
# 작성일: 2024-11-11
# 소프트웨어학과 32192406 심의진
####################

class BidirectNode:
    def __init__(self, x, prevNode: 'BidirectNode', nextNode: 'BidirectNode'):
        self.item = x
        self.prev = prevNode
        self.next = nextNode