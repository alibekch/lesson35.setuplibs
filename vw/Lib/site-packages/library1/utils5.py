
import math
a = "alibek1321423"

def strnum(a):    
    counter=0

    for i in a:
        if i.isnumeric:
            counter = counter+1
        return counter
        print(counter)
