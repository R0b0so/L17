import random
playing = True
Number = str(random.randint(10, 20))
print("I will generate a number from 10 - 20 and you have to guess which number it is.")
while playing:
    guess = input("what is your guess? \n")
    if guess == Number:
        print("You win")
        break
    else:
        print("Try again")

  