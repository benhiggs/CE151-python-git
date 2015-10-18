#6


def searchforletter(string,lowl,uppl):
    occ=0
    for x in range(0,len(string)):
        if string[x]==lowl or string[x]==uppl:
            occ+=1
    return(occ)

text=str(input('Input a line of text to check for vowels: '))

vowellist=[]

x=searchforletter(text,'a','A')
vowellist.append(('a',x))

x=searchforletter(text,'e','E')
vowellist.append(('e',x))

x=searchforletter(text,'i','I')
vowellist.append(('i',x))

x=searchforletter(text,'o','O')
vowellist.append(('o',x))

x=searchforletter(text,'u','U')
vowellist.append(('u',x))

#sort list, most freq first
vowellist.sort(key=lambda tup:tup[1],reverse=True)

for x in range(0,5):
    occ=0
    tup=vowellist[x]
    if tup[1] !=0:
        print('The vowel ',tup[0],' occurs ',tup[1],' time(s)')
        occ+=1
    elif occ==0:
        print('There were no vowels in the inputted text')
        

