

# Girilen sayı uzunluğunda fibonacci dizisini ekrana yazdırır ve hesaplar.


a=0
b=1
c=0

n=int(input("Enter number : "))
print("Fibonacci series :", a, b,end=" ")
c=a+b
n=n-2

while n>0:
    print(c,end=" ")
    a=b
    b=c
    c=a+b
    n=n-1

print("\nTotal : {}".format(c))



"""
Output: 

Enter number : 6
Fibonacci series : 0 1 1 2 3 5
Total : 8
"""