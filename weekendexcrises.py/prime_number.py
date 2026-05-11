# for num from 2 to 100 
       #set is_prime = True
       #for i from 2 to num-1 
          # if num % i == 0 
               #is_prime = False
               #stop inner loop
       #if is_prime 
           #print num



count = 0
for num in range(2, 101):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        count += 1

print("Number of primes between 1 and 100:", count)
