

my_list=[]

while True:                                # listeye eleman ekledik.
    value=int(input("enter value : "))
    my_list.append(value)
    if len(my_list)>=5:
        break

my_list.sort()
print()
print(my_list)    # liste içindeki elemanları sıralayıp yazdık.


def multiply_list(my_list):    # listedeki elemanları çarptık.
    result=1
    for i in my_list:
        result*=i
    return result 


print()
print("result : {}".format(multiply_list(my_list)))



"""
Output: 

enter value : 4
enter value : 9
enter value : 3
enter value : 8
enter value : 6

[3, 4, 6, 8, 9]

result : 5184

"""


