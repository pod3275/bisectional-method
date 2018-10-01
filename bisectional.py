import numpy as np
import math as m

# target function
f = lambda x: x/30 - np.cos(x)
MIN = -30
MAX = 30
sign_bit = 5

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
            if round(n, sign_bit) == round(a, sign_bit) or round(n, sign_bit) == round(b, sign_bit):
                return round(n, sign_bit), 1
            else:
                if f(a)*f(n) < 0:
                    return bisect(a, n)
                elif f(a)*f(n) > 0:
                    return bisect(n, b)

if __name__ == '__main__':
    min = MIN
    max = MAX
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