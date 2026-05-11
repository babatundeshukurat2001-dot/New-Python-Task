#number = int(input("Enter a number: "))
#numbers = 0

#for count in range(1, number + 1):
    #if number % numbers == 0:
        #numbers += 1

#print("Number of divisors:", number)


n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

print("Number of divisors:", count)
