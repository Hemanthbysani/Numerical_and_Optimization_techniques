from sympy import *
x = symbols('x')
f = x**3 - 5*x - 9
fderivative = f.diff(x)
#taking sympy as diff is easier and need not define another function
#install using ‘pip install sympy’
x0 = float(input('Enter Guess: '))
e = float(input('TOL: '))
N = int(input('Maximum Step: '))

def newtonRaphson(x0,e,N):
    print('\nNEWTON-RAPHSON METHOD')
    step = 1
    flag = 1
    condition = True
    while condition:
        if fderivative.evalf(subs= {x:x0}) == 0.0:
            print('Divide by zero error')
            break
        
        x1 = x0 - (f.evalf(subs= {x:x0}))/(fderivative.evalf(subs= {x:x0}))
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f.evalf(subs= {x:x0})))
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f.evalf(subs= {x:x0})) > e
    
    if flag==1:
        print('\nRequired root: %0.7f' % x1)
    else:
        print('\nNot Convergent.')

newtonRaphson(x0,e,N)