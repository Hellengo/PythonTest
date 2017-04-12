# -*- coding: utf-8 -*-
'''
name =  "健康的abcdef"
print type(name)
print len(name)

str = 'abcdecfgc'
list = []
for i in range(len(str)):
    list.append(str[i])
print list
print list.index('c')
print list.count('c')
'''
shop_list = []
total_cost = 0
salary = raw_input("请输入工资:").strip()
if salary.isdigit():
    salary = int(salary)
Products = [
    ['iPhone', 6000],
    ['Ximi', 2000],
    ['BMW', 300000],
    ['Uyiku', 99],
    ['Coffee', 39]
]

while True:
    for index, product in enumerate(Products):
        print index, product[0], product[1]
    choice = raw_input("选择购买:").strip()
    if choice.isdigit():
        choice = int(choice)
        price = Products[choice][1]
        if price < salary:
            shop_list.append(Products[choice])
            salary -= price
            total_cost += price
            print "\033[31;1m%s\033[0m 添加成功,余额为\033[31;1m%s\033[0m" %(Products[choice][0], salary)
        else:
            print "余额不足,请购买其它物品!"
            continue
    elif choice == '退出':
        break
print "购物清单:", shop_list, "\n总计:%s元" %total_cost, "\n卡上余额为:%s元" %salary

