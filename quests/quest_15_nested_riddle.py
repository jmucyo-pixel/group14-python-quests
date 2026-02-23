direction = input("Do you go 'left' or 'right'? ")
if direction == "left":
    action = input("Do you 'swim' or 'wait'? ")
    if action == "swim":
        print("You found a treasure!")
    else:
        print("You waited and nothing happened.")
else:
    print("You went right and found a dead end.")
