# The Fortune Teller asks for input.

user_name = input("Fortune Teller: Stranger, what is your name? ")

# Ask a second question for the current quest
user_quest = input(f"Fortune Teller: And what brings you to the cave today, {user_name}? ")

# Print a confirmation message using the stored variables
print(f"\nAh, {user_name}! I foresee that your journey for '{user_quest}' has begun.")
