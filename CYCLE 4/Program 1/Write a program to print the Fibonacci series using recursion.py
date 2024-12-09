def fibonacci(n):
        if n<=1:
                return n
        else:
                return fibonacci(n-1) + fibonacci(n-2)
num_terms=int(input("Enter the number of terms:"))
if num_terms<=0:
        print("Please enter a positive integer")
else:
        print("Fibonacci Sequence:")
        for i in range(num_terms):
                print(fibonacci(i))
