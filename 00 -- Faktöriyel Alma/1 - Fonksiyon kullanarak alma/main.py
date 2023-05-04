
# Fonksiyon kullanarak faktöriyel alma programı


def factorial(number):
    if number==0:
        return 1
    elif number<0:
        return "number is negative"
    else:
        fact=1
        for x in range(1,number+1):
            fact=fact*x
        return fact


num=int(input("Enter the number to get the factorial : "))
print(factorial(num))


""" Output :

Enter the number to get the factorial : 4
24

"""