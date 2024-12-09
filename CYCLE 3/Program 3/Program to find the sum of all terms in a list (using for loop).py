int(input("Enter number of terms:"))
list=[int(x) for x in input ("Enter numbers:").split()]
total=0
for i in list:
        total+=i
print("sum of the list:",total)
