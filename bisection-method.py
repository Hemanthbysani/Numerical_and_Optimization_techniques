from sympy import *
x = symbols('x')
f = x**3-5*x-9
#taking sympy as differenciation is easier and need not define another function
#install using ‘pip install sympy’
x0 = float(input('First Guess: '))
x1 = float(input('Second Guess: '))
e = float(input('TOL: '))

def bisection(x0,x1,e):
    Count = 1
    print('\nBISECTION METHOD')
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (Count, x2, f.evalf(subs= {x:x2})))

        if f.evalf(subs= {x:x0}) * f.evalf(subs= {x:x2}) < 0:
            x1 = x2
        else:
            x0 = x2
        
        Count = Count + 1
        condition = abs(f.evalf(subs= {x:x2})) > e

    print('\nRequired Root is : %0.8f' % x2)



if f.evalf(subs= {x:x0}) * f.evalf(subs= {x:x1}) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    bisection(x0,x1,e)