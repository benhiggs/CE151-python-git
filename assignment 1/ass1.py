"""
ass1.py
CE151 assignment 1 template
created by sands 30/10/10
modified by Ben Higgs 27/10/14 - 8
"""
from math import sqrt,atan,degrees

def ex1() :
    """
    exercise 2
    hypotenuse and angles
    done 27/10/14
    """
    width=float(input("\nPlease enter the width of the triangle: "))
    height=float(input("Please enter the height of the triangle: "))
    #work out hypotenuse
    hypot=sqrt(width**2 + height**2)
    print ("The hypotenuse for your triangle, using pythagoras' theorem is ",round(hypot,1))
    #Work out angles
    deg=180-90
    dego=degrees(atan(height/width))
    deg=deg-dego
    print("The angles in the triangle are 90 °,",round(dego,1),"° and",round(deg,1),"°")
    


    
def ex2() :
    """
    exercise 2
    Fibonacci
    done 27/10/14
    """
    #loops of fib seq
    n=int(input("Input a number for n: "))

    li=[]
    #if n is less than 2
    if n <=2:
        l=0
        while l<n:
            li.append(1)
            l+=1        
    else:
    #if n is more than 2
        n=n-2
        l=0
        li=[1,1]
        while l<n:            
            t=li[-1]+li[-2]
            li.append(t)
            l+=1
    #convert list to string and strip [] and remove spaces
    fib=(str(li).strip('[]'))
    fib=fib.replace(' ','')
    print(fib)

    
        
        
def ex3() :
    """
    exercise 3
    prime number checker
    done 27/10/14
    """

    n=int(input("Please input a positive integer to be checked: "))
    prime=False
    
    PrimeL=False

    if n in [1,2,3]:
        PrimeL=True; print('The Number is prime')

    elif n%2==0:
        PrimeL=True; print('The Number is not prime')

    else:
        d=3
        while d<(n//2):
            r=n%d
            if r==0:
                PrimeL=True;d=n//2; print('The Number is not prime')
            else:
                d+=2
                
        if PrimeL==False: #still false, all checks been completed, no number gave r=0, Prime
            PrimeL=True; print('The Number is Prime')



   
def ex4() :
    """
    exercise 4
    Binomial coefficent
    03/11/14
    """

    x=int(input('Input a value for x: '))
    y=int(input('Input a value for y: '))

    if y>x: res=0
    elif y==1: res=x
    elif y==x: res=1
    else:
        top=x
        print(top)
        for i in range(1,(y)):
            top=top*(x-i)
        bot=y
        for i in range(1,(y)):
            bot=bot*(y-i)
        res=top//bot

    print ('The binomial coefficent when x =',x,' and y =',y,' equals ',res)



     
        
def ex5() :
    """
    exercise 5
    word processing
    03/11/14
    """
    text=str(input("Input a line of text e.g. a sentence :"))
    #init vars
    pos1=0
    pos2=0
    l=0
    s=0
    def comparelen(string,l,s):
        leng=len(string)
        if l==0 and s==0:
            l=leng
            s=leng
        else:
            if leng<=s:
                s=leng
            elif leng>=l:
                l=leng
        return l,s
    while pos2 < len(text):
        #while text is not at the end of the inputted string
        if text[pos2]==" ":
            print(text[pos1:pos2])
            l,s=comparelen(text[pos1:pos2],l,s)
            #accounts for the fact slices cut off the string 1 char short.
            pos2+=1; pos1=pos2
        #while text is at the end of its params
        elif pos2==len(text)-1:
            print(text[pos1:])
            l,s=comparelen(text[pos1:],l,s)
        pos2+=1
    print ('shortest string is ',s,' characters long and the longest string is ',l,' characters long')

    

    
def ex6() :
    """
    exercise 6
    search for vowels in a string
    03/11/14
    """
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
    
    occ=0
    for x in range(0,5):       
        tup=vowellist[x]
        if tup[1] !=0:
            print('The vowel ',tup[0],' occurs ',tup[1],' time(s)')
            occ+=1
    if occ==0:
        print('There were no vowels in the inputted text')
        
def ex7() :
    """
    exercise 7
    """
    li=[]; ex=False
    while ex == False:
        app=int(input('Input a positive integer to add to the list or e to end list: '))
        if app>=0: li.append(app)
        else: ex=True

    def checks(s,sort,li):
        if s==0: sort=True
        else: sort=False
        return s,sort
        
    sort=False ;l=0
    while sort==False:
        for i in range(1,len(li)):
            try: s,sort=checks(s,sort,len(li))
            except: s=0
            for x in range(0,len(li)-1):
                l+=1
                if li[x]>li[x+1]: li[x],li[x+1]=li[x+1],li[x];s+=1
                
        sort=True   
                
    print((len(li)**2),' possible checks (algorithm has worst case performance of O(n^2) )')
    print(s,'swaps')
    print(l,'checks')
    print('The sorted list is:')
    print(li)

    
def ex8() :
    """
    exercise 8
    """
    print("Exercise 8 not attempted")


# modify the following line so that your name is displayed instead of Lisa's
print("CE151 assignment 1 - Ben Higgs")

# do not modify anything beneath this line
exlist = [None, ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8]
running = True
while running :
    line = input("Select exercise (0 to quit): ")
    if line == "0" : running = False
    elif len(line)==1 and "1"<=line<="8": exlist[int(line)]()
    else : print("Invalid input - try again")


