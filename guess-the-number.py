#simple number gessing program
import random
secretnmber = random.randint(1,20)
print("please enter your name")
name = input()
print("helo "+name+" i am thinking of number between 1 to 20")

for i in range(1,7):
    print("take guess")
    guess = int(input())
    if guess < secretnmber:
        print("your gess is too low")
    elif guess > secretnmber:
        print("yor guess is too high")
    else:
        break #true condition

if guess == secretnmber:
    print("good you guessed my number in %s guesses"%(i))
else:
    print("nope, you not guessed my number, which is %s in %s guesses"%(secretnmber,i))
    
''' created by Atul'''
