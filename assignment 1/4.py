#4

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
