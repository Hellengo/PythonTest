# -*- coding: utf-8 -*-

data = {
    'name' : 'hellen',
    'age'  : 28,
    'job'  : 'CEO'
}
data['salary'] = 50000
data['info'] = 'leader'
data['job'] = 'winer'


#推荐方式
for key in data:
    print key, data[key]


#大字典不适合
#for key, val in data.items():
#    print key, val
#data2 = data.copy()
#print data2

#if data.has_key('info'):
#    print data['info']

keys = data.keys()
keys.sort()
print [data[key] for key in keys]
print map(data.get, keys)

print sorted(data.items(), key=lambda x:x[0])


#print data.get('info')
#print data.get('name')



###
'''
menu = {
    'Beijing':{
        'Chaoyang':{
            'CBD'     : ['CCTV', 'CCAV'],
            'Wangjing': ['Momo', 'Chuizi']
    },
        'Haidian':{
            'Xierqi'  : ['Baidu', 'Youku'],
            'Wudaokou': ['Wangyi', 'Souhu']
}
    },
    'Shanghai': {
        'Pudong' : ['Ctrip', '1 Shop'],
        'Puxi'   : ['China bank', 'America bank']
    }
}
#print menu['Beijing']['Chaoyang']['CBD']
#print menu['Beijing']['Chaoyang']['CBD'][0]

#for key, val in menu.items():
#    print key, val

#for key in menu.keys():
#    print key
exit_flag = False
while  not exit_flag:
    for index, key in enumerate(menu.keys()):
        print index, key
    choice_1 = raw_input("Please choose menu to enter:").strip()
    if choice_1.isdigit():
        choice_1 = int(choice_1)
        key_1 = menu.keys()[choice_1]
        while not exit_flag:
            for index, key in enumerate(menu[key_1]):
                print '-->', index, key
            print '-----------------------------'
            choice_2 = raw_input("Please choose menu to enter").strip()
            if choice_2.isdigit():
                choice_2 = int(choice_2)
                key_2 = menu[key_1].keys()[choice_2]
                while not exit_flag:
                    for index, key in enumerate(menu[key_1][key_2]):
                        print '-->-->', index, key
                    choice_3 = raw_input("Please choose menu to enter").strip()
                    if choice_3.isdigit():
                        choice_3 = int(choice_3)
                        key_3 = menu[key_1][key_2].keys()[choice_3]
                        print menu[key_1][key_2][key_3]
                        print 'this is last level......'
                    elif choice_3 == 'quit':
                         exit_flag = True
                    elif choice_3 == 'back':
                         break

else:
    print 'going to quit...'
'''