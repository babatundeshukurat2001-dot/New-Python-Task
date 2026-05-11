# ask user for a number and store it as n
 #set sum_odd = 0
 #while n > 0 DO
       #digit = n % 10
      # if digit is odd 
           #sum_odd = sum_odd + digit
      # n = n // 10
#4. print sum_odd



n = int(input("Enter a number: "))
sum_odd = 0

while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        sum_odd += digit
    n //= 10

print("Sum of odd digits:", sum_odd)
