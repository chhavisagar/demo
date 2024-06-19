
n = int(input("Enter the number of Fibonacci numbers to generate: "))


a, b = 0, 1


fib_sequence = []


for _ in range(n):
    fib_sequence.append(a)
    a, b = b, a + b


print(f"Fibonacci sequence with {n} numbers: {fib_sequence}")