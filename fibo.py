def fibonacci(n):

    a = 0
    b = 1

    if n<=1:
        return n
    
    for i in range(n-1):
        temp = a + b
        a = b
        b = temp
        print(a, b)
    return b