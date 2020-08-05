import math
a="Alibek123"
ttl=0
def strlen(a):
    if len(a)<=12 and len(a)>=6:
        return 1
    else:
        return 0
    
def strnum(a):    
    counter=0

    for i in a:
        if i.isnumeric:
            counter = counter+1
        return counter

