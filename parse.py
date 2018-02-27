import os

newpath = r'C:\vagrant_getting_started\Errors'
mainpath = r'C:\vagrant_getting_started\Main'
errpath = r'C:\vagrant_getting_started\Errors\errors.txt'
corrpath = r'C:\vagrant_getting_started\Main\correct.txt'
janpath = r'C:\vagrant_getting_started\Main\01-January'
january = r'C:\vagrant_getting_started\Main\01-January\January.txt'
febpath = r'C:\vagrant_getting_started\Main\02-February'
february = r'C:\vagrant_getting_started\Main\02-February\February.txt'
marpath = r'C:\vagrant_getting_started\Main\03-March'
march = r'C:\vagrant_getting_started\Main\03-March\March.txt'
aprpath = r'C:\vagrant_getting_started\Main\04-April'
april = r'C:\vagrant_getting_started\Main\04-April\April.txt'
maypath = r'C:\vagrant_getting_started\Main\05-May'
may = r'C:\vagrant_getting_started\Main\05-May\May.txt'
junpath = r'C:\vagrant_getting_started\Main\06-June'
june = r'C:\vagrant_getting_started\Main\06-June\June.txt'
julpath = r'C:\vagrant_getting_started\Main\07-July'
july = r'C:\vagrant_getting_started\Main\07-July\July.txt'
augpath = r'C:\vagrant_getting_started\Main\08-August'
august = r'C:\vagrant_getting_started\Main\08-August\August.txt'
seppath = r'C:\vagrant_getting_started\Main\09-September'
september = r'C:\vagrant_getting_started\Main\09-September\September.txt'
octpath = r'C:\vagrant_getting_started\Main\10-October'
october = r'C:\vagrant_getting_started\Main\10-October\October.txt'
novpath = r'C:\vagrant_getting_started\Main\11-November'
november = r'C:\vagrant_getting_started\Main\11-November\November.txt'
decpath = r'C:\vagrant_getting_started\Main\12-December'
december = r'C:\vagrant_getting_started\Main\12-December\December.txt'
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
            e = open(errpath, 'a+')
            e.write(" ".join(split_up))
            e.close()
        else:
            c = open(corrpath, 'a+')
            c.write(" ".join(split_up))
            c.close()  
    return

def month():
    m = open('main\correct.txt', 'r')
    for line in m:
        split_mon = line.split(' ')
        if "Jan" in split_mon[3]:
            j = open(january, 'a+')
            j.write(" ".join(split_mon))
            j.close()         
        elif "Feb" in split_mon[3]:
            f = open(february, 'a+')
            f.write(" ".join(split_mon))
            f.close()         
        elif "Mar" in split_mon[3]:
            mar = open(march, 'a+')
            mar.write(" ".join(split_mon))
            mar.close()         
        elif "Apr" in split_mon[3]:
            apr = open(april, 'a+')
            apr.write(" ".join(split_mon))
            apr.close()         
        elif "May" in split_mon[3]:
            m = open(may, 'a+')
            m.write(" ".join(split_mon))
            m.close()         
        elif "Jun" in split_mon[3]:
            jun = open(june, 'a+')
            jun.write(" ".join(split_mon))
            jun.close()         
        elif "Jul" in split_mon[3]:
            jul = open(july, 'a+')
            jul.write(" ".join(split_mon))
            jul.close()         
        elif "Aug" in split_mon[3]:
            a = open(august, 'a+')
            a.write(" ".join(split_mon))
            a.close()         
        elif "Sep" in split_mon[3]:
            s = open(september, 'a+')
            s.write(" ".join(split_mon))
            s.close()         
        elif "Oct" in split_mon[3]:
            o = open(october, 'a+')
            o.write(" ".join(split_mon))
            o.close()               
        elif "Nov" in split_mon[3]:
            n = open(november, 'a+')
            n.write(" ".join(split_mon))
            n.close() 
        elif "Dec" in split_mon[3]:
            d = open(december, 'a+')
            d.write(" ".join(split_mon))
            d.close() 
        else:
            e = open(errpath, 'a+')
            e.write(" ".join(split_mon))
            e.close()
    return


def unsuccessful():
    f = open('main\correct.txt', 'r')
    count=0
    file = 0
    
    for line in f:
        split_f = line.split(' ')
        if '400' in split_f[8]:
            count+=1
        if '401' in split_f[8]:
            count+=1
        if '402' in split_f[8]:
            count+=1
        if '403' in split_f[8]:
            count+=1
        if '404' in split_f[8]:
            count+=1
        if '405' in split_f[8]:
            count+=1
        if '406' in split_f[8]:
            count+=1
        if '407' in split_f[8]:
            count+=1
        if '408' in split_f[8]:
            count+=1
        if '409' in split_f[8]:
            count+=1
        if '410' in split_f[8]:
            count+=1
        if '411' in split_f[8]:
            count+=1
        if '412' in split_f[8]:
            count+=1
        if '413' in split_f[8]:
            count+=1
        if '414' in split_f[8]:
            count+=1
        if '415' in split_f[8]:
            count+=1
        if '416' in split_f[8]:
            count+=1
        if '417' in split_f[8]:
            count+=1
        if '418' in split_f[8]:
            count+=1
        if '421' in split_f[8]:
            count+=1
        if '422' in split_f[8]:
            count+=1
        if '423' in split_f[8]:
            count+=1
        if '424' in split_f[8]:
            count+=1
        if '426' in split_f[8]:
            count+=1
        if '428' in split_f[8]:
            count+=1 
        if '429' in split_f[8]:
            count+=1
        if '431' in split_f[8]:
            count+=1
        if '451' in split_f[8]:
            count+=1
        else:
            file+=1

    percen= (count/file)*100
    print(count)
    print(file)
    print("3. A total of %.2f%% of requests were unsuccessful." % percen)
    return


def redirect():
    f = open('main\correct.txt', 'r')
    count=0
    file = 0
    
    for line in f:
        split_f = line.split(' ')
        if '300' in split_f[8]:
            count+=1
        if '301' in split_f[8]:
            count+=1
        if '302' in split_f[8]:
            count+=1
        if '303' in split_f[8]:
            count+=1
        if '304' in split_f[8]:
            count+=1
        if '305' in split_f[8]:
            count+=1
        if '306' in split_f[8]:
            count+=1
        if '307' in split_f[8]:
            count+=1
        if '308' in split_f[8]:
            count+=1
        else:
            file+=1

    percen= (count/file)*100
    
    print(count)
    print(file)
    print("4. A total of %.2f%% of requests were redirected elsewhere." % percen)
    return
main()