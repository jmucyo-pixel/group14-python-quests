# This function asks the user to enter their age
# It converts the input into a number and returns it
def ask_for_age():
    age = int(input("enter your age: "))
    return age


# This function checks if the person is old enough to vote
# It uses the age provided to make the decision
def can_they_vote(age):
    # If the age is 18 or above, the person is allowed to vote
    if age >= 18:
        print("yes, you can vote!")
    else:
        # If the age is below 18, they are not allowed to vote yet
        print("you cant vote sorry wait for your time.")


# Get the user's age by calling the first function
user_age = ask_for_age()

# Check if the user can vote using the age provided
can_they_vote(user_age)