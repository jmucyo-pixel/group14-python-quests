def add (a, b):#function for adding two variable which is a and b 
    return a + b 
num1 = float(input("Enter first number: "))#when you run it this will display first
num2 = float(input("Enter second number: "))
operation = input("Choose operation (add, subtract, multiply, divide): ")
if operation == "add": #here its to say that if it's to add it will add the variables that u put in
    print(add(num1, num2))
elif operation == "subtract":#same goes for subtraction if u input subtraction it will subtract the inputs
    print(num1 - num2)
elif operation == "divide":
    if num2 == 0:#this is to avoid error because every number divided by zero is error
        print("Cannot divide by zero")
    else:
        print(num1 / num2)
elif operation == "multiply":
    print(num1 * num2)
else:
    print("Invalid operation")#if you dont input any of the above operation it will display this 