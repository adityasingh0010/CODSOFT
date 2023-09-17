
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


while True:

    print("Operators:")
    print("Type 'add' for addition.")
    print("Type 'subtract' for subtraction.")
    print("Type 'multiply' for multiplication.")
    print("Type 'divide' for division.")
    print("Type 'quit' to end the program.")


    user_input = input(": ")


    if user_input == "quit":
        break


    if user_input not in ["add", "subtract", "multiply", "divide"]:
        print("Invalid input. Please enter a valid operation.")
        continue


    number1 = float(input("Enter your first number: "))
    number2 = float(input("Enter your second number: "))


    if user_input == "add":
        result = add(number1, number2)
    elif user_input == "subtract":
        result = subtract(number1, number2)
    elif user_input == "multiply":
        result = multiply(number1, number2)
    elif user_input == "divide":
        result = divide(number1, number2)

    
    print("Show Result:", result)
