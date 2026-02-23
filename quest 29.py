def code_breaker():
    # This is the secret number the player must guess correctly
    secret_code = 42
    
    # The player is only allowed a limited number of attempts
    attempts = 3

    # Keep asking for guesses as long as the player still has attempts left
    while attempts > 0:
        # Ask the user to enter a guess and convert it to an integer
        guess = int(input("Enter the secret code: "))

        # Check if the guess matches the secret code
        if guess == secret_code:
            # If the guess is correct, the game ends successfully
            print("Access granted!")
            return
        else:
            # If the guess is wrong, reduce the number of attempts
            attempts -= 1
            print("Wrong code! Attempts left:", attempts)

    # This message is shown only if the player runs out of attempts
    print("Access denied. Game over.")

# This line starts the game by calling the function
code_breaker()