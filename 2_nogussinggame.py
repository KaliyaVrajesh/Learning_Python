import random

c = int(input("Enter the heighest number:"))

a = random.randint(1,c)
b = 0



while(True):
    b= int(input("Enter the number you guessed:"))

    if (b == a):
        print("Congratulations! You Guessed right!")
        break
    elif(b > a):
        print("Guess Lower!!")
    elif(b < a):
        print("Guess Higher!!")
    else:
        print("Enter valid output")