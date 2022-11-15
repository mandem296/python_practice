#return allows returning information from a function
#cannot read code after return keyword
#any datatype can be returned

def user(name):
    return name

def cube(number):
    return number*number*number

digit = input("Enter number: ")

print(user("Mandela your answer is"))

print(cube(float(digit)))

print("\n")

#storing in a variable the printing the value inside the variable
result = cube(4)
print(result)















































