#comparing different numbers or strings in if statements

def max_num(number_1,number_2,number_3):
    if number_1 >= number_2 and number_1>=number_3:
        return number_1
    elif number_2>=number_1 and number_2>=number_3:
        return number_2
    else:
        return number_3

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

print("\n")

print((max_num(float(num1),float(num2),float(num3))))