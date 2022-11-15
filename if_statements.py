#if statements are conditional statements
#using if statements with or
#elif stands for elseif
#not() negates what is inside

is_male = False
is_tall = False

#if is_male or is_tall:
#if is_male or is_tall:
if is_male and is_tall:
    #print("You are a male or tall or both!")
    print("You are a tall male!")

elif is_male and not(is_tall):
    print("You are a short male")

elif not(is_male) and is_tall:
    print("You are not a male but you are tall")


else:
    print("You are neither male nor tall")
