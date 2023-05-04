

# Girilen sayının asal sayı olup olmadığını kontrol eder. 


counter=0
number=int(input("Enter number : "))


for i in range(2,number):
    if number %i==0:
        counter +=1
        break

if counter !=0:
    print(f"The number {number} entered is not prime number.")
else:
    print(f"The number {number} entered is a prime number.")




"""
Enter number : 5
The number 5 entered is a prime number.


Enter number : 9
The number 9 entered is not prime number.

"""
