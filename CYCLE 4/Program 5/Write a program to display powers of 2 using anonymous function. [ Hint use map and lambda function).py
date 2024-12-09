num_terms=int(input("Enter the number of terms for powers of 2:"))
my_list=[]
print("Enter the terms:")
for i in range(num_terms):
        list_1=int(input())
        my_list.append(list_1)
powers_of_2=list(map(lambda x:2**x,my_list))
print(f"Powers of 2 upto {num_terms} terms:{powers_of_2}")
