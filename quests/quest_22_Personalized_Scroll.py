def personalized_greeting(name, quest):
    print(f"Greetings, {name}!")
    print(f"Good luck on your quest to {quest}!")

# Ask the user for input
user_name = input("What is your name? ")
user_quest = input("What is your quest? ")

# Call the function with the user's answers
personalized_greeting(user_name, user_quest)