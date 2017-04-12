# -*- coding: utf-8 -*-
import os
import sys
import xlrd
import logging
import string
import fileinput

#reload(sys)
#sys.setdefaultencoding('utf-8')

#res = commands.getoutput('fir')
#print res

#os.system('fir')
'''
print sys.argv
print sys.path
#print sys.path.append('')
sum = 0
list = range(100)
for i in range(len(list)):
    sum += list[i]
print sum

###
#for index, i in enumerate(range(1,10)):
    #print index, i

#read
f = file("test.txt", "r")
for line in f.readlines():
    print line,
f.close()

#write
f = file("test.txt", "w")
f.write("this is first line\n")
f.write("this is second line\n")
f.write("this is third line\n")
f.close()

#append
f = file("test.txt", "a")
f.write("this is appending part\n")
f.close()

#read & write: r+ w+
a = []
f = file("test.txt", "r+")
f.readline()
f.readline()
f.write("this is change line\n")
f.flush()

#for line in f.xreadlines():
#    print line
#for i in string.uppercase:a.append('%s\n' %i)
#f.writelines(a)
f.close()
'''
####自动修改文件

if '-r' in sys.argv:
    rep_argv_pos = sys.argv.index('-r')
    find_str = sys.argv[rep_argv_pos + 1]
    new_str = sys.argv[rep_argv_pos + 2]
#find_str = 'Debug:False'
#new_str = 'Debug:True'
f = file('test.txt', 'r+')
while True:
    line = f.readline()
    #print "===>", f.tell()
    if find_str in line:
        #print "--->cur pos:", f.tell(), len(line)
        last_line_pos = f.tell() - len(line)
        f.seek(last_line_pos)
        #print "--->new pos:", f.tell()
        new_line = line.replace(find_str, new_str)
        f.write(new_line)
        break
    else:
        break
f.close()
###库方法
#for line in fileinput.input("test.txt", inplace=1, backup='.bak'):
#    print line.replace('SECOND', 'GOttfdfl')
