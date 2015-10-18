'''
This program is EX1 from the Introduction to programming assignment 2
Student details
Ben Higgs 02-12-2014
'''

def getdetails(string):#gets details on regno year course, then surname then othernames
    try:
        strpos=0;stfpos=0;dets=['','',''];temp=''
        while stfpos<3:
            if string[strpos]!=' ':
                temp+=string[strpos]
                strpos+=1
            else:
                dets[stfpos]=temp
                temp=''
                stfpos+=1
                strpos+=1
        string=string[strpos:]
        spaces=[]
        for i in range(len(string)):
            if string[i]==' ':
                j=i
                spaces.append(j)
        sname=string[(spaces[-1]+1):]
        onames=string[:spaces[-1]]
        details=(dets[0],dets[1],dets[2],onames,sname)
    except:details=string 
    print(format((details[4]+', '+details[3]),'<32s'),format(details[0],'<7s'),format(details[2],'<6s'),'Year',format(details[1],'<1s'))
    return details

def printheaders():#print headers for the table
    print(format('Student name','<32s'),format('Regno','<7s'),format('Course','<6s'),'Year')
    

def fileops():#file operations
    Filename = input("Specify input file: ")
    if Filename[-4:]!='.txt':
        Filename=Filename+'.txt'
    try :
        filein = open(Filename)
    except IOError as e :
        filein = None
        print("Failed to open", Filename, "- program aborted")

    if filein != None:
        printheaders()
        stdli=[]
        for line in filein:
            line=line.replace('\n', '').replace('\r', '')
            res=getdetails(line)
            stdli.append(res)
        return stdli


def degreesearch(details): #search for degree scheme, orders by students surname
    search=str(input('Input the degree scheme to search for: '))
    res=[]
    for i in range(len(details)):
        if (details[i])[2]==search:
            res.append(details[i])
    res=sorted(res,key=lambda x:x[4])
    if len(res)>0:
        printheaders()
        for i in range(len(res)):
            getdetails(res[i])
    else: print('No students matched your criteria.')
    

def regnosearch(details): #searches by the registration number, outputs the name of student
    search=input('Input the regno to search for: ')
    crit='F'
    for i in range(len(details)):
        if (details[i])[0]==search:
            print('The student searched for is:')
            print((details[i])[3],(details[i])[4])
            crit='T'
    if crit=='F':print('No students matched your criteria.')


def yearsearch(details): #searches the list of tuples by year and orders by students surname
    lower=int(input('Input the lowest year to include in your search: '))
    upper=int(input('Input the upper year to include in your search: '))
    rang=[lower]
    while lower !=upper:
        lower+=1
        rang.append(lower)
    res=[]
    for i in range(len(details)):
        if int((details[i])[1]) in rang:
            res.append(details[i])
    res=sorted(res,key=lambda x:x[4])
    if res>0:
        printheaders()
        for i in range(len(res)):
            getdetails(res[i])
    else: print('No students matched your criteria.')


#main body of program. exits the program loop if file is not found. File can be specified specifally or just by the name

print('This program interprets text files and outputs the list of students')
details=fileops()
bye=False
while bye==False:
    print('''
Please choose a search option:
1 - Degree scheme
2 - Students in specific year
3 - Regno
0 - exit
''')
    opt=int(input('Your choice is '))
    if opt==1:
        degreesearch(details)
    elif opt==2:
        yearsearch(details)
    elif opt==3:
        regnosearch(details)
    elif opt==0:bye=True
    

