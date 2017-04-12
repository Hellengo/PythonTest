# -*- coding: utf-8 -*-

from operator import itemgetter, attrgetter
'''
my_name = 1
myName =2
print "请输入姓名、工资"
succuess = False
if succuess:
    print "it is success"

age = "10"
print type(age)
age = int(age)
print type(age)

a = 60
b = 13
c = a & b
print c
c = a | b
print c


print "test"
print 'test'

name = 'Alex'
age = '18'
print ''Welcome!
I am %s
I am %s years old!
''% (name, age)


str = raw_input("Please input:").strip()
list = []
for i in xrange(len(str)):
    list.append(str[i])
    count = list.count(str[i])
    if count > len(str)/2:
        print "找到的元素为:",str[i], "出现次数:", count




#先序遍历

class BinNode():
    def __init__( self, val ):
        self.lchild = None
        self.rchild = None
        self.val = val

def preOrder(self, root):
    if root == None:
        return
    print root.val
    self.preOrder(root.lchild)
    self.preOrder(root.rchild)


def preOrder(self, root):
    if root == None:
        return
    myStack = []
    node = root
    while node or myStack:
        while node:
            # 从根节点开始，一直找它的左子树
            print node.val
            myStack.append(node)
            node = node.lchild
        # while结束表示当前节点node为空，即前一个节点没有左子树了
        node = myStack.pop()
        # 开始查看它的右子树
        node = node.rchild


ipaddr = raw_input("input ipaddress:").strip()

addr = ipaddr.strip().split('.')
#print addr
if len(addr) != 4:
    print "ip 缺少"
for i in range(len(addr)):
    try:
        addr[i] = int(addr[i])
    except:
        print "ip 包含字母"
    if addr[i] <= 255 and addr[i] >= 0:
        pass
    else:
        print "ip 范围错误"

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
for i in list1:
    if i in list2:
        print i
#print [l for l in list1 if l in list2]


List = [1, 2, 2, 3, 2]

def unique_index(List):
    if len(List) != len(set(List)):
        for i in range(len(List)):
            if List.count(i) > 1:
                a = List[i]
        print [i for i, j in enumerate(List) if j==a]
    else:
        return -1

def main():
    unique_index(List)

if __name__ == '__main__':
    main()
'''

List = [1, 3, 5, 2, 4]
list1 = []
list2 = []

a = List[len(List)/2]

for i in List[:len(List)/2]:
    list1.append(i)
for i in List[len(List)/2+1:]:
    list2.append(i)

for i in list2:
    list1.extend(list2)

print  list1


