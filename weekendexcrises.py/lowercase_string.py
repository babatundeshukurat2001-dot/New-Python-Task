#1. ask user for a string 
#2. set count = 0
#3. for each character character in string 
       #if character is an lowercase letter then
           #count = count + 1
#4. print "Number of lowercase letters:", count





string = input("Enter a string: ")
count = 0

for character in string:
    if character.islower():
        count = count + 1

print("Number of Lowercase letters:", count)
