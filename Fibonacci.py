def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Change the value of n to generate a different number of Fibonacci numbers
n = 10
result = fibonacci(n)
print(f"The first {n} Fibonacci numbers are: {result}")
