def factorial(num):
        if num==0 or num==1:
                return 1
        else:
                result=1
                for i in range(2,num+1):
                        result *= i
        return result
def permutations(n,r):
        return factorial(n)//factorial(n-r)
def combinations(n,r):
        return factorial(n)//(factorial(r)*factorial(n-r))
n=int(input("Enter the value of n (total objects):"))
r=int(input("Enter the value of r (objects taken at a time):"))
if r>n:
        print("Invalid input:r should be less than or equal to n")
else:
        print(f"The number of permutations (p{n},{r})) is:{permutations(n,r)}")
        print(f"The number of combinations (c({n},{r})) is:{combinations(n,r)}")
