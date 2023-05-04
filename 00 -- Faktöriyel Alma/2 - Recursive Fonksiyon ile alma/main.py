
# Recursive Fonksiyon kullanarak faktöriyel alma programı


def factorial(number):
    if number==0:
        return 1
    elif number==1:
        return 1
    return number*factorial(number-1)


num=int(input("Enter the number to get the factorial : "))
print(factorial(num))


""" Output :

Enter the number to get the factorial : 5
120

"""