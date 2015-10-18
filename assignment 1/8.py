#8
from datetime import date
datenow=date.today()

def checkval(val,maxx,arguement): #checks if a value is valid by being passed the val, max and an identifier
    if arguement=='day':
        if val>0 and val<=maxx: check=True
        else:print('The day you entered is not in the valid range'); check=False
    elif arguement=='month':
        if val>0 and val<=maxx: check=True
        else:print('The month you entered is not in the valid range'); check=False
    elif arguement=='year':
        if val>=maxx: check=True
        else:print('The year you entered is not in the valid range'); check=False
#    elif arguement=='fulldate':
#        try:#check date is valid(days in the month) and if it has passed or not
#            datefut=datetime.datetime(year=val[2],month=val[1],day=val[0])
#            check=True                       
#        except:print('Please enter a valid date in the future');check=False    
            
    else:print('There was a problem with your input')
    return check

"""if val[2]==datenow.year:
                if val[1]==datenow.month:
                    if val[0]>datenow.day: check=True
                    else:print('Date has to be in the future');check=False
                elif val[1]>datenow.month: check=True
                else:print('Date has to be in the future'); check=False
            elif val[2]>datenow.year: check=True
            else:print('There was a problem with your input'); check=False"""


def getdate():
    checkfull=False
    while checkfull==False:
        check=False
        while check==False:
            day=int(input('Please input a day: (numerical) '))
            check=checkval(day,31,'day')
        check=False
        while check==False:
            month=int(input('Please input a month: (numerical) '))
            check=checkval(month,12,'month')
        check=False
        while check==False: 
            year=int(input('Please input a year: (_ _ _ _) '))
            check=checkval(year,datenow.year,'year')
        datefut=[day,month,year]
        checkfull=checkval(datefut,'','fulldate')
    return datefut


datefut=getdate()
#using date module(which handles leap years), minus the two dates and convert and output in only days.
dif=date(datefut[2],datefut[1],datefut[0])-datenow
print('There are ',dif.days,' between these now and the date entered')
