#defining function
def f(x):
    return(x**2 - 7)

def bisection_method(a, b, tol):
    if f(a)*f(b) > 0:
        #end function
        print("No root found")
    else:
        while (b - a)/2.0 > tol:
            midpoint = (a + b)/2.0
            if f(midpoint) == 0:
                return(midpoint) #The midpoint is the x-intercept/root.
            elif f(a)*f(midpoint) < 0: # if increasing but below 0 
                b = midpoint
            else:
                a = midpoint
            print("Midpoint = ",midpoint)#print values of midpoint after every iteration
        
        return(midpoint)

answer = bisection_method(-1, 5, 0.001)#define parameters for search; a,b,tolerance of error

print("Answer:", round(answer, 3))