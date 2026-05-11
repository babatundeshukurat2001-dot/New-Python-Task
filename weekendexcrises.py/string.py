#1. ask user for string 
#2. set reversed_string = ""
#3. for each character  in string 
      # reversed_string = character + reversed_string
#4. print reversed_string


string = input("Enter a string: ")
reversed_string = ""

for character in string:
    reversed_string = character + reversed_string

print(reversed_string)
