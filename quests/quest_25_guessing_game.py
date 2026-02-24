import random #Import random module to generate a random number
secret_number = random.randint(1,20)#it will generate a random number between 1 and 20
while True:#keep asking till they get it correct
    guess = int(input("Guess the number (1-20): "))

    if guess == secret_number:#if they guess the secret number right it displays this 
        print("Lets goooooo, you got it right!!!!!!.Are u sure u didnt cheat?")
        break

    elif guess < secret_number:#if the number is low it will print this
        print("damn that's too low")

    else:
        print("Aiming for the sky i see, I meant that it's too high")

