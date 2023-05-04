

"""
1-100 arasında üretilen rastgele sayıyı kullanıcının tahmin etmesini isteyen ve kaçıncı tahmin sonunda sayıyı bulduğunu gösteren program.
"""


from random import randint


number=randint(1,100)
guess_count=0


while True:
    
    guess = int(input("Guess a number between 1 and 100 (exit '0') : "))
    guess_count += 1
    
    if guess == 0:
        print("exit")
        break
    elif guess > number :
        print("You need to guess lower!")
        continue
    elif guess < number :
        print("You need to guess higher!")
        continue
    else:
        print("You guessed the number correctly.Number : {}".format(number))
        print("Number of guesses : {}".format(guess_count))
        break




"""
Output : 

Guess a number between 1 and 100 (exit '0') : 50
You need to guess lower!
Guess a number between 1 and 100 (exit '0') : 25
You need to guess lower!
Guess a number between 1 and 100 (exit '0') : 10
You need to guess higher!
Guess a number between 1 and 100 (exit '0') : 15
You need to guess higher!
Guess a number between 1 and 100 (exit '0') : 20
You need to guess lower!
Guess a number between 1 and 100 (exit '0') : 18
You need to guess lower!
Guess a number between 1 and 100 (exit '0') : 16
You guessed the number correctly.Number : 16
Number of guesses : 7

"""


