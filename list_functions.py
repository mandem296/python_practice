print("\n")
friends = ["Bobo","Joan","Wambui","Jojo","Mojojojo"]
lucky_numbers = [4,8,15,42,16,23]

#copying a list
friends_copy = friends.copy()

print(friends)
print(lucky_numbers)
print(friends_copy)
print("\n")


#sorting lists
friends.sort()
lucky_numbers.sort()
print(lucky_numbers)
print(friends)
print("\n")

#sorting in reverse
lucky_numbers.reverse()
friends.reverse()

print(friends)
print(lucky_numbers)
print("\n")

friends.extend(lucky_numbers) #joining two lists

friends.append("Mandela") #adding another element at the end of list


#inserting at the middle
friends.insert(1,"Ndela") #insert element in index 1
friends.insert(1,"Bobo") #insert element in index 1


print(friends)
print("\n")

friends.pop() #removes last element in list

print(friends)
print("\n")

friends.remove("Ndela") #remove element from list

print(friends)
print("\n")

print(friends.index("Bobo")) #display index of the element
print("\n")

print(friends.count("Bobo"))
print("\n")



























































