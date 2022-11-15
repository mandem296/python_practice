phrase="Ndela is cool"

#print(phrase + " the coolest") --> this is concatenation

print(phrase.upper()) #makes all characters be in uppercase
print(phrase.isupper()) #checking if all characters are in uppercase and returns either true or false


print(phrase.lower()) #makes all characters be in lowercase
print(phrase.lower().islower()) #converting all to lowercase and checking if all characters are in lowercase
print(phrase.islower()) #checking if all characters are in lowercase and returns either true or false

print(len(phrase)) #prints out the number of characters in the phrase

print(phrase[0], phrase[1]) #print character in index 0 and index 1

print(phrase.index("d")) #return index of the character d. this is case sensitive

print(phrase.index("cool")) #return index in which the word "cool" starts. characters before the word "cool"

print(phrase.replace("cool","an agent of mapema ndo best")) #replace "cool" with "an agent of mapema ndo best"