import numpy as np
import math as m

# target function
f = lambda x: x/30 - np.cos(x)

# bisectional method
def bisect(a, b):
    result = f(a)*f(b)
    
    if result == 0:
        if f(a) == 0:
            return a, 1
        else:
            return b, 1
        
    else:
        if result > 0:
            return 0, 0
        else:
            n = (a+b)/2
            if round(n, 5) == round(a, 5) or round(n, 5) == round(b, 5):
                return round(n, 5), 1
            else:
                if f(a)*f(n) < 0:
                    return bisect(a, n)
                elif f(a)*f(n) > 0:
                    return bisect(n, b)

if __name__ == '__main__':
    min = -30
    max = 30
    x = []
        
    i=0
    while i <= max:
        n, check = bisect(i, i + m.pi)            
        if check == 1:
            x.append(n)
        i+=m.pi
        
    i=0
    while i >= min:
        n, check = bisect(i - m.pi, i)            
        if check == 1:
            x.append(n)
        i-=m.pi
    
    x.sort()
    print('X')
    for i in range(len(x)):
        print('%.4f' % (x[i]))