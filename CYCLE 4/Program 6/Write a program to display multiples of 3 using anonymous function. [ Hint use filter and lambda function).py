number=list(map(int,input("Enter the numbers:").split(",")))
multiples=list(filter(lambda x:x%3==0,number))
print(f"The multiples of 3 from the list:{multiples}")
