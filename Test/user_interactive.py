#-*- coding: utf-8 -*-
from selenium.webdriver.support.expected_conditions import NoSuchElementException
import sys
import os

'''
name = raw_input("Please input your name:")
age = raw_input("Please input your age:")
salary = raw_input("Please input your salary:")


print "Your name is", name
print "Your name is", age
print "Your name is", salary

###
information = raw_input("Please input your information:")

name, age, salary = information.split(',')

print "information of as blow: %s, %s, %s" %(name,age,salary)

if name == "hellengo":
    print "He is handsome!"
else:
    print "He is a go!"

###
retry_count = 0
real_num = 43
#while True:
#while retry_count < 3:
for i in range(3):

    guess_num = int(raw_input("Please guess the real num:"))

    if guess_num > real_num:

        print "Wrong! you need try smaller!"

        retry_count += 1

    elif guess_num < real_num:

        print "Wrong! you nedd try bigger!"

        retry_count += 1

    else:

        print "You are right!"

        break

###
passwd = 'test'
logout_flag = False
for i in range(3):
    user_input = raw_input("请输入密码:").strip()
    if len(user_input) == 0:
        continue #跳出本次循环,进入下一循环
    if user_input == passwd:
        print "welcome login!"
        while True:
#            user_choice = raw_input(
             1. run a cmd
             2. send a file
             3. exit this level
             4. exit the whole system
             ).strip()
            user_choice = int(user_choice)
            if user_choice == 1:
                print "going to run a cmd"
            if user_choice == 2:
                print "going to send a file"
            if user_choice == 3:
                print "going to exit this level"
                break
            if user_choice == 4:
                logout_flag = True
                break
        if logout_flag:
            print "going to logout"
            break
    else:
        print "密码错误,请重试!"

####
name_list = ['tom', 'jack', 'lucy']
name_list.insert(2, 'lily',)
name_list.append('lilei')
name_list2 = ['rain', 'joy']
#name_list.remove('lilei')

#print name_list.index('tom')
#print name_list
name_list.extend(name_list2)
print name_list

name_list.sort()
print type(name_list.reverse())
print name_list
#print name_list.count('lilei')
#print name_list, name_list[1:3], name_list[-1], name_list[-2], name_list[-3:], name_list[:3]

for i in range(name_list.count('rain'))
    name_list.remove('rain')

####
'''

target = sys.argv[1]
list = range(100)
low = 0
high = len(list) - 1

def BinarySearch(list, target):

    while low <= high:

        mid = (low + high) // 2

        if list[mid] < target:
            low = mid + 1
        elif list[mid] > target:
            high = mid - 1
        else:
            #return mid
            print target, list[mid]
    return -1

if __name__ == '__main__':
	main()