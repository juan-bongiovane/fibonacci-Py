# La función calcula el número de fibonacci en la posicion n

def fibonacci(n):

    a = 0
    b = 1
    
    if n<=1:
        return n
    
    for i in range(n-1):
        temp = a + b
        a = b
        b = temp
    return a