

def fibonacci(number):
    if number==0:    # ilk fibonacci sayısı 0'dır.
        return 0
    
    if number==1:    # ikinci fibonacci sayısı 1'dir.
        return 1
    
    return fibonacci(number-1) + fibonacci(number-2)


number=int(input("Enter number : "))
print(fibonacci(number))



"""
Output:

Enter number : 6
8
"""