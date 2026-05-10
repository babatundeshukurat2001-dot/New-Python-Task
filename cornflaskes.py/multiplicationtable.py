#1. ask user for a number and store it as num
#2. for count from 1 to 10 DO
       #calculate product = num * count
      # print "num x count = product"
#3. end



num = int(input("Enter a number: "))

for count in range(1, 11):
    print(f"{num} x {count} = {num * count}")
