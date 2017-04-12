#from Selenium2Library import Selenium2Library
#se = Selenium2Library()
#se.open_browser('http://www.baidu.com', 'safari')
import os
import sys
#se.close_browser()
'''


data = {}
for i in range(10):data[i] = i
print data

list1 = [1,4,6,3,8,6,1]
list1 = set(list1)
list2 = set([2,1,4,9,7])

print list1 & list2
print list1 | list2
print list1 - list2
print list2 - list1
print list1 ^ list2
'''

currentPath = os.getcwd()
buildPath = os.chdir('')

print currentPath + '/' + 'test'