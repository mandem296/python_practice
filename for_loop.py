#loop over different collections of items
#for example: arrays, letters in words and sentences
#specify_value used in the for loop
#"Giraffe Academy" collection
#variable value changes after every loop

#for specify_value in "Giraffe Academy"

#creating an array
friends = ["Bobo","Ndela","Dante"]

for letter in "Giraffe Academy":
    print(letter)

for friends in friends:
    print(friends)

#numbers
for index in range(10):
    print(index) #prints numbers from 0 to 9

#numbers
for number in range(3,10):
    print(number) #prints numbers from 3 to 9
    #doesn't print last number in range (3,10) 10 is not printed

print("\n")
friends = ["Bobo","Ndela","Dante"]
for index_ in range(len(friends)): #printing all elements in array

    print(friends[index_])


print("\n")
friends = ["Bobo","Ndela","Kevo"]
for index_1 in range(5): #printing all elements in array
    if index_1==0:
     print("First iteration")
    else:
        print("not first")