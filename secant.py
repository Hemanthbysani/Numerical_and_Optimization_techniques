from sympy import *
x = symbols('x')
f = x**3 - 5*x - 9
#taking sympy as diff is easier and need not define another function
#install using ‘pip install sympy’
x0 = float(input('First Guess: '))
x1 = float(input('Second Guess: '))
e = float(input('TOL: '))
N = int(input('Maximum Step: '))

def secant(x0,x1,e,N):
    print('\nSECANT METHOD')
    step = 1
    condition = True
    while condition:
        if f.evalf(subs= {x:x0}) == f.evalf(subs= {x:x1}):
            print('Divide by zero error')
            break
        
        x2 = x0 - (x1-x0)*f.evalf(subs= {x:x0})/( f.evalf(subs= {x:x1}) - f.evalf(subs= {x:x0}) ) 
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f.evalf(subs= {x:x2})))
        x0 = x1
        x1 = x2
        step = step + 1
        
        if step > N:
            print('Not Convergent')
            break
        
        condition = abs(f.evalf(subs= {x:x2})) > e
    print('\n Required root is: %0.8f' % x2)

secant(x0,x1,e,N)