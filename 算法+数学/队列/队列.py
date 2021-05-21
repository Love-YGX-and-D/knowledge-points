class queue:
    def __init__(self):
        self._box=[]
    def empty(self):
        return self._box==[]
    def queues(self,i):
        self._box.append(i)
    def dequeues(self):
        return self._box.pop(0)

from collections import deque
Queue=deque()
# 插入
Queue.append("A")
# 出队
Queue.popleft()

# 迷宫[栈,队列]
# 冒泡 选择  插入
