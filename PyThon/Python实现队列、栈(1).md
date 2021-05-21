# 队列

```python
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
```

# 栈

```python
def match(strs):
    arr=stack()
    con="(){}[]"
    for i in strs:
        if con.find(i)==-1:
            continue
        if i=="(" or i=="{" or i=="[":
            arr.push(i)
            continue
        if arr.length()==0:
            return False
        p=arr.pop()
        if (p=="(" and i==")") or (p=="[" and i=="]") or (p=="{" and i=="}"):
            continue
        else:
            return False
    if arr.length()>0:
        return False
    return True
```

# 单项列表

```python
# 自定义异常
class error(Exception):
    def __init__(self,message):
        super(error,self).__init__()
        self.message=message
    def __str__(self):
        return "Out of range"
# 节点类
class mynode():
    def __init__(self,ele=None):
        self.ele=ele
        self.next=None

# 列表类
class mylist():
    def __init__(self,ele=None):
        self._head=ele
        self.pos=0
    # 判断列表是否为空
    def empty(self):
        return self._head==None
    # 从前添加元素
    def add(self,item):
        node1=mynode(item)
        node1.next=self._head
        self._head=node1
    # 列表的长度
    def length(self):
        num=1
        cursor=self._head
        while cursor.next != None:
            cursor=cursor.next
            num+=1
        return num
    # 队尾追加元素
    def append(self,item):
        node = mynode(item)
        if self._head==None:
            self._head=node
        else:
            cursor=self._head
            while cursor.next != None:
                cursor=cursor.next
            cursor.next=node
    # 获取元素
    def get(self,index):
        if index==0:
            return self._head.ele
        elif index>self.length()-1:
            return error("超出索引范围")
        else:
            cursor=self._head
            num=0
            while num<index:
                cursor=cursor.next
                num+=1
            return cursor.ele
    # 在任意部位插入
    def insert(self,index,item):
        if index==0:
            self.add(item)
        elif index==self.length()-1:
            self.append(item)
        else:
            node=mynode(item)
            num=0
            cursor=self._head
            pre=""
            while num<index:
                pre=cursor
                cursor=cursor.next
                num+=1
            pre.next=node
            node.next=cursor
    # 在队尾删除元素
    def pop(self):
        if self.empty():
            return None
        elif self.length()==1:
            return self._head.ele
        else:
            cursor=self._head
            pre=""
            while cursor.next!=None:
                pre=cursor
                cursor=cursor.next
            pre.next=None
            return cursor.ele
    # 根据内容删除remove
    def remove(self,item):
        if self.empty():
            return None
        elif self.length()==1:
            return None
        else:
            cursor=self._head
            if cursor.ele==item:
                self._head=cursor.next
            else:
                while cursor.next!=None:
                    current=cursor
                    cursor=cursor.next
                    if cursor.ele==item:
                        current.next=cursor.next

    # 根据下标删除delete
    def delete(self,index):
        if index==0:
            cursor=self._head
            self._head=cursor.next
        elif index==self.length()-1:
            self.pop()
        elif index<0 or index>self.length()-1:
            return error("索引超界")
        else:
            num=0
            cursor=self._head
            while num<index:
                current=cursor
                cursor=current.next
                num+=1
            current.next=cursor.next
    # 迭代器/迭代对象
    def __iter__(self):
        return self
    def __next__(self):
        if self.pos<self.length():
            self.pos+=1
            cursor=self._head
            num=0
            while cursor!=None:
                current=cursor
                cursor=cursor.next
                num+=1
                if num==self.pos:
                    return current.ele
        else:
            raise StopIteration


lii=mylist()
lii.add("4")
lii.add("5")
lii.add("6")
lii.append("7")
lii.append("8")
# print(lii.empty())
# lii.remove("7")
# lii.remove("6")
# lii.insert(3,2)
# print(lii.get(4))
# print(lii.pop())
lii.delete(1)
for i in lii:
    print(i)
```

# 单项循环列表

```python
# 自定义异常
class error(Exception):
    def __init__(self,message):
        super(error,self).__init__()
        self.message=message
    def __str__(self):
        return "Out of range"

# 节点
class mynode():
    def __init__(self,ele=None):
        self.ele=ele
        self.next=None
# empty,add,length,append,get,insert,pop,remove,delete
# 列表
class mylist():
    def __init__(self,ele=None):
        self._head=ele
    # empty
    def empty(self):
        return self._head==None
    # add
    def add(self,item):
        node1=mynode(item)
        if self.empty():
            node1.next=self._head
            self._head= node1
        else:
            cursor=self._head
            node1.next=cursor.next
            self._head=node1
    #length
    def length(self):
        num=1
        cursor=self._head
        if cursor.next==self._head:
            num=1
            return num
        while cursor.next!=self._head:
            cursor=cursor.next
            num+=1
        return num





    def __iter__(self):
        return self
    def __next__(self):
        if self.pos<self.length():
            self.pos+=1
            cursor=self._head
            num=0
            while cursor!=None:
                current=cursor
                cursor=cursor.next
                num+=1
                if num==self.pos:
                    return current.ele
        else:
            return StopIteration


lists=mylist()
lists.add("1")
lists.add("2")
print(lists.length())
```

