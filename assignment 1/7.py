#7


li=[]; ex=False
while ex == False:
    app=int(input('Input a positive integer to add to the list or e to end list: '))
    if app>=0: li.append(app)
    else: ex=True

def checks(s,sort,li):
    if s==0: sort=True
    else: sort=False
    return s,sort
    
sort=False ;l=0;s=0
while sort==False:
    for i in range(1,len(li)):
        #try: s,sort=checks(s,sort,len(li))
        #except: s=0
        for x in range(0,len(li)-1):
            l+=1
            if li[x]>li[x+1]: li[x],li[x+1]=li[x+1],li[x];s+=1
            if s==0:
                sort=True
            
    sort=True   
            
print((len(li)**2),' possible checks (algorithm has worst case performance of O(n^2) )')
print(s,'swaps')
print(l,'checks')
print('The sorted list is:')
print(li)
