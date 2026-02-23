def forest():
    print("You enter a dark forest.")
    choice = input("Do you go left or right? ")

    if choice == "left":
        print("You find treasure! You win!")
    else:
        print("You meet a dragon. Game over.")


def castle():
    print("You approach a mysterious castle.")
    choice = input("Do you enter or run away? ")

    if choice == "enter":
        print("You become king! You win!")
    else:
        print("You fall into a trap. Game over.")


def adventure():
    print("Welcome to the Adventure!")
    start = input("Do you go to the forest or castle? ")

    if start == "forest":
        forest()
    elif start == "castle":
        castle()
    else:
        print("Invalid choice. Game over.")

# Start the game
adventure()