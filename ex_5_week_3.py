print("--- Fibonacci Sequence Generator ---")
a = 0
b = 1

quantity = int(input("How many Fibonacci numbers would you like to generate? "))
for sequence in range(quantity):
    print(a, end=" ")
    a, b = b, a + b