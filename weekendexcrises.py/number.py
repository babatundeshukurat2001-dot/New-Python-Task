#1. ask user for integer 
#2. set reversed_integer = ""
#3. for each number  in int 
      # reversed_integer = integer + reversed_integer
#4. print reversed_integer


int = input("Enter a integer: ")
reversed_integer = ""

for number in int:
    reversed_integer = number + reversed_integer

print(reversed_integer)
