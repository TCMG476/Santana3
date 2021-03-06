import os
import platform
import urllib.request
import operator
corrlist = []
errlist = []
if platform.system() == 'Windows':
    errpath = r'C:\vagrant_getting_started\errors.txt'
    corrpath = r'C:\vagrant_getting_started\correct.txt'
    january = r'C:\vagrant_getting_started\01-January.txt'
    february = r'C:\vagrant_getting_started\02-February.txt'
    march = r'C:\vagrant_getting_started\03-March.txt'
    april = r'C:\vagrant_getting_started\04-April.txt'
    may = r'C:\vagrant_getting_started\05-May.txt'
    june = r'C:\vagrant_getting_started\06-June.txt'
    july = r'C:\vagrant_getting_started\07-July.txt'
    august = r'C:\vagrant_getting_started\08-August.txt'
    september = r'C:\vagrant_getting_started\09-September.txt'
    october = r'C:\vagrant_getting_started\10-October.txt'
    november = r'C:\vagrant_getting_started\11-November.txt'
    december = r'C:\vagrant_getting_started\12-December.txt'
else:
    errpath = r'errors.txt'
    corrpath = r'correct.txt'
    january = r'01-January.txt'
    february = r'02-February.txt'
    march = r'03-March.txt'
    april = r'04-April.txt'
    may = r'05-May.txt'
    june = r'06-June.txt'
    july = r'07-July.txt'
    august = r'08-August.txt'
    september = r'09-September.txt'
    october = r'10-October.txt'
    november = r'11-November.txt'
    december = r'12-December.txt'    
    
def main():
    print ("Connecting with https://s3.amazonaws.com/tcmg476/http_access_log...")
    webUrl = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
    print ("Success! Please be patient, your files are being generated.\n")  
    global data
    data = webUrl.read()
    writefile(data)
    error()
    month()
    totalreq()
    dawemo()
    weekav()
    monthnum()
    statuscode()
    numreqs()
    return data

def writefile(lines):
    print("Writing http_access_log to local file...")
    a = open('accesslog.txt', 'w+')
    a.write(lines.decode("UTF-8"))
    a.close()
    print("Done.\nSeparating errors...")
    
def error():
    f = open('accesslog.txt','r')
    for line in f:
        line.split(' ')
        split_up = line.split(' ')
        if len(split_up) != 10:
            errlist.append(split_up)
        else:
            corrlist.append(split_up)
    j= open(corrpath, 'w+')
    j.write(''.join(" ".join(x) for x in corrlist))
    j.close()
    e = open(errpath, 'w+')
    e.write(''.join(" ".join(y) for y in errlist))
    e.close()    
    print("Done.\nSeparating month logs into respective files...")
    return

def month():
    m=open(corrpath, 'r')
    jan = []
    feb = []
    mar = []
    apr = []
    maay = []
    jun = []
    jul = []
    aug = []
    sep = []
    ocp = []
    nov = []
    dec = []
    for line in m:
        split_mon = line.split(' ')
        if len(split_mon) == 10:
            if "Jan" in split_mon[3]:
                jan.append(split_mon)
            elif "Feb" in split_mon[3]:
                feb.append(split_mon)       
            elif "Mar" in split_mon[3]:
                mar.append(split_mon)         
            elif "Apr" in split_mon[3]:
                apr.append(split_mon)         
            elif "May" in split_mon[3]:
                maay.append(split_mon)        
            elif "Jun" in split_mon[3]:
                jun.append(split_mon)        
            elif "Jul" in split_mon[3]:
                jul.append(split_mon)        
            elif "Aug" in split_mon[3]:
                aug.append(split_mon)     
            elif "Sep" in split_mon[3]:
                sep.append(split_mon)
            elif "Oct" in split_mon[3]:
                ocp.append(split_mon)               
            elif "Nov" in split_mon[3]:
                nov.append(split_mon)
            elif "Dec" in split_mon[3]:
                dec.append(split_mon)
        
    j = open(january, 'w+')
    j.write(''.join(" ".join(x) for x in jan))
    j.close
    f = open(february, 'w+')
    f.write(''.join(" ".join(x) for x in feb))
    f.close
    m = open(march, 'w+')
    m.write(''.join(" ".join(x) for x in mar))
    m.close
    a = open(april, 'w+')
    a.write(''.join(" ".join(x) for x in apr))
    a.close
    ma = open(may, 'w+')
    ma.write(''.join(" ".join(x) for x in maay))
    ma.close
    jo = open(june, 'w+')
    jo.write(''.join(" ".join(x) for x in jun))
    jo.close
    ju = open(july, 'w+')
    ju.write(''.join(" ".join(x) for x in jul))
    ju.close
    au = open(august, 'w+')
    au.write(''.join(" ".join(x) for x in aug))
    au.close
    s = open(september, 'w+')
    s.write(''.join(" ".join(x) for x in sep))
    s.close
    o = open(october, 'w+')
    o.write(''.join(" ".join(x) for x in ocp))
    o.close
    n = open(november, 'w+')
    n.write(''.join(" ".join(x) for x in nov))
    n.close
    d = open(december, 'w+')
    d.write(''.join(" ".join(x) for x in dec))
    d.close
        
    return

def totalreq():
    t = open('accesslog.txt', 'r')
    count = 0
    for line in t:
        count +=1
    print('1. There were a total of %d requests.\n' % count)
    return

def dawemo():
    d=open(corrpath, 'r')
    count = 0
    mainlist = []
    day = 0
    mon = 0
    tues = 0
    wed = 0
    thurs = 0
    fri = 0
    sat = 0
    sun = 0
    x = 0
    day = 1
    for line in d:
        split_d = line.split(' ')
        if len(split_d) == 10:
            count += 1
            mainlist.append(split_d)
        today = mainlist[x]
        after = mainlist[x - 1]
        if today[3][1:3] != after[3][1:3]:
            day += 1
        y = day % 8
        if y == 0:
            day = 1
        if day == 1:
            mon += 1
        if day == 2:
            tues += 1
        if day == 3:
            wed += 1
        if day == 4:
            thurs += 1
        if day == 5:
            fri += 1
        if day == 6:
            sat += 1
        if day == 7:
            sun += 1
        x = x + 1            
    monav = mon/52
    tuesav = tues/52
    wedav = wed/52
    thursav = thurs/52
    friav = fri/52
    satav = sat/52
    sunav = sun/52
    print("2. Monday had an average of %d requests." %monav)
    print("   Tuesday had and average of %d requests." %tuesav)
    print("   Wednesday had and average of %d requests." %wedav)
    print("   Thursday had an average of %d requests." %thursav)
    print("   Friday had an average of %d requests." %friav)
    print("   Saturday had an average of %d requests." %satav)
    print("   Sunday had an average of %d requests.\n" %sunav)
    return

def weekav():
    w=open(corrpath, 'r')
    count = 0
    wone = []
    wtwo = []
    wthree = []
    wfour = []
    lastfew = []
    twentynine = []
    thirtieth = []
    thirtyone = []
    for line in w:
        split_w = line.split(' ')
        if '01' in split_w[3][1:3]:
            count += 1
            wone.append(split_w)
        elif '02' in split_w[3][1:3]:
            count += 1
            wone.append(split_w)
        elif '03' in split_w[3][1:3]:
            count += 1
            wone.append(split_w)
        elif '04' in split_w[3][1:3]:
            count += 1
            wone.append(split_w)
        elif '05' in split_w[3][1:3]:
            count += 1
            wone.append(split_w)
        elif '06' in split_w[3][1:3]:
            count += 1
            wone.append(split_w)
        elif '07' in split_w[3][1:3]:
            count += 1
            wone.append(split_w)
        elif '08' in split_w[3][1:3]:
            count += 1
            wtwo.append(split_w)
        elif '09' in split_w[3][1:3]:
            count += 1
            wtwo.append(split_w)
        elif '10' in split_w[3][1:3]:
            count += 1
            wtwo.append(split_w)
        elif '11' in split_w[3][1:3]:
            count += 1
            wtwo.append(split_w)
        elif '12' in split_w[3][1:3]:
            count += 1
            wtwo.append(split_w)
        elif '13' in split_w[3][1:3]:
            count += 1
            wtwo.append(split_w)
        elif '14' in split_w[3][1:3]:
            count += 1
            wtwo.append(split_w)
        elif '15' in split_w[3][1:3]:
            count += 1
            wthree.append(split_w)
        elif '16' in split_w[3][1:3]:
            count += 1
            wthree.append(split_w)
        elif '17' in split_w[3][1:3]:
            count += 1
            wthree.append(split_w)
        elif '18' in split_w[3][1:3]:
            count += 1
            wthree.append(split_w)
        elif '19' in split_w[3][1:3]:
            count += 1
            wthree.append(split_w)
        elif '20' in split_w[3][1:3]:
            count += 1
            wthree.append(split_w)
        elif '21' in split_w[3][1:3]:
            count += 1
            wthree.append(split_w)
        elif '22' in split_w[3][1:3]:
            count += 1
            wfour.append(split_w)
        elif '23' in split_w[3][1:3]:
            count += 1
            wfour.append(split_w)
        elif '24' in split_w[3][1:3]:
            count += 1
            wfour.append(split_w)
        elif '25' in split_w[3][1:3]:
            count += 1
            wfour.append(split_w)
        elif '26' in split_w[3][1:3]:
            count += 1
            wfour.append(split_w)
        elif '27' in split_w[3][1:3]:
            count += 1
            wfour.append(split_w)
        elif '28' in split_w[3][1:3]:
            count += 1
            wfour.append(split_w)
        elif '29' in split_w[3][1:3]:
            count += 1
            lastfew.append(split_w)
            twentynine.append(split_w)
        elif '30' in split_w[3][1:3]:
            count += 1
            lastfew.append(split_w)
            thirtieth.append(split_w)
        elif '31' in split_w[3][1:3]:
            count += 1
            lastfew.append(split_w)
            thirtyone.append(split_w)
    one = len(wone)/12
    two = len(wtwo)/12
    three = len(wthree)/12
    four = len(wfour)/12
    last = len(lastfew)/11
    tn = len(twentynine)/11
    tt = len(thirtieth)/11
    to = len(thirtyone)/7
    print("   The 1st week of every month had an average of %d requests." %one)
    print("   The 2nd week of every month had an average of %d requests." %two)
    print("   The 3rd week of every month had an average of %d requests." %three)
    print("   The 4th week of every month had an average of %d requests.\n" %four)
    print("   The last couple of days of every month had an average of %d "\
          "requests, \n   denoting heavier traffic. The following breaks"\
          " down the last few days \n   of the month (for the months that have"\
          " them):\n" %last)
    print("   The 29th day had an average of %d requests." %tn)
    print("   The 30th day had an average of %d requests." %tt)
    print("   The 31st day had an average of %d requests.\n" %to)

def monthnum():
    j = open(january, 'r')
    f = open(february, 'r')
    mar = open(march, 'r')
    a = open(april, 'r')
    ma = open(may, 'r')
    jun = open(june, 'r')
    jul = open(july, 'r')
    aug = open(august, 'r')
    sep = open(september, 'r')
    o = open(october, 'r')
    n = open(november, 'r')
    d = open(december, 'r')
    jcount = 0
    fcount = 0 
    marcount = 0 
    acount = 0 
    macount = 0 
    juncount = 0 
    julcount = 0 
    augcount = 0 
    sepcount = 0 
    ocount = 0 
    ncount = 0
    dcount = 0 
    for line in j:
        jcount+=1
    for line in f:
        fcount+=1
    for line in mar:
        marcount+=1
    for line in a:
        acount+=1
    for line in ma:
        macount+=1
    for line in jun:
        juncount+=1
    for line in jul:
        julcount+=1
    for line in aug:
        augcount+=1
    for line in sep:
        sepcount+=1
    for line in o:
        ocount+=1
    for line in n:
        ncount+=1
    for line in d:
        dcount+=1   
    print("   January had a total of %d requests." %jcount)
    print("   February had a total of %d requests." %fcount)
    print("   March had a total of %d requests." %marcount)
    print("   April had a total of %d requests." %acount)
    print("   May had a total of %d requests." %macount)
    print("   June had a total of %d requests." %juncount)
    print("   July had a total of %d requests." %julcount)
    print("   August had a total of %d requests." %augcount)
    print("   September had a total of %d requests." %sepcount)
    print("   October had a total of %d requests." %ocount)
    print("   November had a total of %d requests." %ncount)
    print("   December had a total of %d requests.\n" %dcount)
    return

def statuscode():
    f=open(corrpath, 'r')
    count=0
    count1=0
    file = 0
    file1=0
    for line in f:
        split_f = line.split(' ')
        if '4' in split_f[8][0]:
            count+=1
        if '30' in split_f[8]:
            count1+=1
            file1+=1 
            file+=1
        else:
            file+=1
            file1+=1
    percen= (count/file)*100
    redir= (count1/file1)*100
    print("3. A total of %.2f%% of requests were unsuccessful.\n" % percen)
    print("4. A total of %.2f%% of requests were redirected elsewhere.\n" % redir)
    return

def numreqs():
    lc = open(corrpath, 'r')
    sdict = {}
    least = []
    file = 0
    for line in lc:
        split_lc = line.split(' ')
        
        if split_lc[6] in sdict:
            sdict[split_lc[6]]+=1
        else:
            sdict[split_lc[6]]=1
            
    numwords = sorted(sdict, key = sdict.get, reverse = True)
    mostfile = numwords[:1]
    for key, value in sdict.items():
        if value == 1:
            least.append(key)
            file+=1
    print ("5. The most requested file is:")
    for i in mostfile:
        print("  ",i)
    print ("6. Number of files that were only requested once: %d" %file)
    print ("   A couple of examples include:")
    for i in least[6:9]:
        print("  ",i)
    return
main()