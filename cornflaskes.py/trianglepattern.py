#1. ask user for a number and store it as n
#2. for count from 1 to n DO
       #print count number of "*"
#3. end







n = int(input("Enter a number: "))

for count in range(1, n + 1):
    print("*" * count)
