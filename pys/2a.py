def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input("Enter the value for n: "))
if n <= 0:
    print("Enter a positive value")
else:
    print("Fibonacci series is:")
    for i in range(n):
        print(fib(i))
