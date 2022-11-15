#creating a function in python to say hi
#indents in functions are important
#we add params inside the () such as name. when calling the function we then input the parameter required such as "Mandela"
#when using integers with strings in printing you must include the integer in the str() function for it to be printed

def say_hi(name,age):
    print("Hello "+name)
    print("you are "+str(age)+" years old!")
    print("\n")


#calling the function
say_hi("Mandela",10)
say_hi("Joan",20)

