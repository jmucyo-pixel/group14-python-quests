# This function runs the FizzBuzz game between two numbers
# It checks each number and prints Fizz, Buzz, FizzBuzz, or the number itself
def fizzbuzz(start, end):
    # Loop through all numbers from start to end (inclusive)
    for i in range(start, end + 1):
        
        # If the number is divisible by both 3 and 5, print "FizzBuzz"
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        
        # If the number is divisible by 3 only, print "Fizz"
        elif i % 3 == 0:
            print("Fizz")
        
        # If the number is divisible by 5 only, print "Buzz"
        elif i % 5 == 0:
            print("Buzz")
        
        # If none of the conditions match, print the number itself
        else:
            print(i)


# Call the function to run FizzBuzz from 1 to 100
fizzbuzz(1, 100)