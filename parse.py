import re
import os

newpath = r'C:\vagrant_getting_started\Errors'
mainpath = r'C:\vagrant_getting_started\Main'
errpath = r'C:\vagrant_getting_started\Errors\errors.txt'
corrpath = r'C:\vagrant_getting_started\Main\correct.txt'
if not os.path.exists(newpath):
    os.makedirs(newpath)
if not os.path.exists(mainpath):
    os.makedirs(mainpath)
f = open('accesslog.txt','r')
def error():
    for line in f:
        line.split(' ')
        split_up = line.split(' ')
        if len(split_up) != 10:
            print(split_up)
            e = open(errpath, 'a+')
            e.write(" ".join(split_up))
            e.close()
        else:
            c = open(corrpath, 'a+')
            c.write(" ".join(split_up))
            c.close()  
    return
