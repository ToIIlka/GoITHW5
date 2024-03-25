def caching_fibonacci():
    chache = {}
    def fibonacci(n):
        if n <=0:
            return 0
        elif n == 1:
            return 1
        elif n in chache:
            return chache[n]
        else:
            chache[n] = fibonacci(n-1) + fibonacci(n-2)
            return chache[n]
        
    return (fibonacci)

fib = caching_fibonacci()
print(fib(10))
print(fib(15))
print(fib(25))
    
    
    