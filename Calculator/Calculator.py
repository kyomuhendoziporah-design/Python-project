print("my calcultor")

#asking for the inputs 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Ask for which operation
operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("error")
    result = None

if result is not None:
    print("Result:", result)
