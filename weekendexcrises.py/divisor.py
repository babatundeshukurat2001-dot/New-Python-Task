#1. ask user for a number and store it as n
#2. print "Divisors of", n, ":"
#3. for i from 1 to number
       #if n divided by i has no remainder 
           #print i



n = int(input("Enter a number: "))

print("Divisors of", n, ":")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")


