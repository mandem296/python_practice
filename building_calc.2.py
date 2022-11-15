#more advanced calculator to perform basic operations

number1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
number2 = float(input("Enter second number: "))

if operator == "+":
    print(number1+number2)
elif operator == "-":
    print(number1-number2)
elif operator == "/":
    print(number1/number2)
elif operator == "*":
    print(number1*number2)
else:
    print("Enter a valid operator")