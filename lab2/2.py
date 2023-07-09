import math
def f(x):
    if math.fabs(x) <= 3:
        f = math.fabs(math.floor(x/3+1))
    elif 3 < math.fabs(x) <= 7:
        f = math.log2(math.e + math.pi* math.fabs(x/3))
    elif math.fabs(x) > 7:
        if x == 7.5:
            return None
        f = math.atan(x/5)+1/(2*x-15)
    else:
        return None 
    return f

def g(x,y):
    if -4 <= x <= 6 and -6 <= y <=2:
        if (x-3)**2+(y-4)**2 == 36 or (x-3)**2+(y-4)**2 == 144:
            return True
        else:
            return False
    else:
        return False
        
    return 

def h(a,b,c):
    if b == 0 and not(abs(a)==5):
        result=0
    elif b == 0 and abs(a)==5:
        result='continuum'
    else:
        result=2
    if c!=0 and not(result == 'continuum'):
        if result == 2:
            if a!= 0 and ( round(-6/c,14) == round(-a/b+5/b,14) or round(-6/c,14) == round(-a/b-5/b,14)):
                return str(result)
            else:
                return str(result+1)
        result = result + 1
    return str(result)
