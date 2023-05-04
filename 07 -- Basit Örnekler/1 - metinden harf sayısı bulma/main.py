

# Harfin metinde kaç adet bulunduğunu söyler.


text=input("Enter text : ")

letter=input("Enter letter : ")
counter=0

for character in text:
    if character==letter:
        counter+=1

print("There {} of entered letter {} in the text.".format(counter,letter))



"""
Output:

Enter text : Hi! How are you today?
Enter letter : a
There 2 of entered letter a in the text.
"""
