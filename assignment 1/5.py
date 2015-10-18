#5


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
