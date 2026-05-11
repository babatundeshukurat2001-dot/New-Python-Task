#1. ask user for a string
#2. set count = 0
#3. for each character character in string 
       #if character is an uppercase letter then
           #count = count + 1
#4. print "Uppercase letters:", count





string = input("Enter a string: ")
count = 0

for character in string:
    if character.isupper():
        count = count + 1

print("Number of Uppercase letters:", count)
