import re
import os

newpath = r'C:\vagrant_getting_started\Errors'
mainpath = r'C:\vagrant_getting_started\Main'
errpath = r'C:\vagrant_getting_started\Errors\errors.txt'
corrpath = r'C:\vagrant_getting_started\Main\correct.txt'
janpath = r'C:\vagrant_getting_started\Main\01-January'
febpath = r'C:\vagrant_getting_started\Main\02-February'
marpath = r'C:\vagrant_getting_started\Main\03-March'
aprpath = r'C:\vagrant_getting_started\Main\04-April'
maypath = r'C:\vagrant_getting_started\Main\05-May'
junpath = r'C:\vagrant_getting_started\Main\06-June'
julpath = r'C:\vagrant_getting_started\Main\07-July'
augpath = r'C:\vagrant_getting_started\Main\08-August'
seppath = r'C:\vagrant_getting_started\Main\09-September'
octpath = r'C:\vagrant_getting_started\Main\10-October'
novpath = r'C:\vagrant_getting_started\Main\11-November'
decpath = r'C:\vagrant_getting_started\Main\12-December'
def main():
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    if not os.path.exists(mainpath):
        os.makedirs(mainpath)
    if not os.path.exists(janpath):
        os.makedirs(janpath)
    if not os.path.exists(febpath):
        os.makedirs(febpath)
    if not os.path.exists(marpath):
        os.makedirs(marpath)
    if not os.path.exists(aprpath):
        os.makedirs(aprpath)
    if not os.path.exists(maypath):
        os.makedirs(maypath)
    if not os.path.exists(junpath):
        os.makedirs(junpath)
    if not os.path.exists(julpath):
        os.makedirs(julpath)
    if not os.path.exists(augpath):
        os.makedirs(augpath)
    if not os.path.exists(seppath):
        os.makedirs(seppath)
    if not os.path.exists(octpath):
        os.makedirs(octpath)
    if not os.path.exists(novpath):
        os.makedirs(novpath)
    if not os.path.exists(decpath):
        os.makedirs(decpath)    
    
    
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














main()