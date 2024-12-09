def compare(s1,s2,n):
        if s1[:n]==s2[:n]:
                return True
        else:
                return False
s1=input("Enter the first string(s1):")
s2=input("Enter the second string(s2):")
n=int(input("Enter the number of characters to compare:"))
result=compare(s1,s2,n)
if result:
        print("The first",n,"characters of both strings are the same.")
else:
        print("The first",n,"characters of both strings are not the same.")
