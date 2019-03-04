
/*fibonacci dizisi */

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
    return a

-----------------------------------------------

/* recursive ile fibonnaci dizisi hesaplama da işlem çok daha uzun sürede bitiyor.*/

def fibonacci_recursive (n):
    if (n<2):
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
        
-----------------------------------------------

/*faktöriyel hesaplama*/

def factorial(n):
    s = 1
    for i in range (1,n+1):
        s = s*i
    return s

-----------------------------------------------

/*recursive ile faktöriyel hesaplama da birbirine yakın süreler de işlem bitiyor.

def factorial_recursive(n) :
    if (n==1):
        return n
    else:
        return n* factorial_recursive(n-1)

-----------------------------------------------
def power (m,n):
    s = m
    for i in range (1,n+1):
        s = s*m
    return s

-----------------------------------------------

/* recursive ile üssünü alırken çok daha kısa sürede işlem bitiyor.*/

def power_recursive (m,n) :
    if (n==0): 
        return 1
    elif (n==1) :
        return m
    elif n//2 ==0 :
        return power_recursive(m*m, n/2)
    elif n//2 != 0:
        return power_recursive(m*m,n/2)*m
        
-----------------------------------------------

 /*
 for i in range(40) :
    r_1 = fibonacci_loop(i)
    r_2 = fibonacci_recursive (i)
    print (r_1, r_2)
 */    
    
 /*   
 for i in range(10,100):
    f1 , f2 = factorial(i), factorial_recursive(i)
    print('factorial loop =',f1,' factorial_recursive=',f2)
 */
 
 /*    
 for i in range (1,3):
    print(power(var,2), end=' ')
    print(power_recursive(var,2))
 */    
        
