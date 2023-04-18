
# Girilen iki sayı arasındaki sayıların toplamını bulur.

num_1=int(input("Enter  number : "))
num_2=int(input("Enter  number : "))

total=0

for x in range(num_1+1,num_2):
    total+=x

print(total)


