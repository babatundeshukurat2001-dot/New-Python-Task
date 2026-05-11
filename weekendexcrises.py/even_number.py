# ask user for a number and store it as n
 #set sum_even = 0
 #while n > 0 DO
       #digit = n % 10
      # if digit is even 
           #sum_even = sum_even + digit
      # n = n // 10
#4. print sum_even



n = int(input("Enter a number: "))
sum_even = 0

while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        sum_even += digit
    n //= 10

print("Sum of even digits:", sum_even)
