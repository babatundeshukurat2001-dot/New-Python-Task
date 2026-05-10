#1. set pass_count = 0
#2. set fail_count = 0
#3. for i from 1 to 15 DO
       #ask user for score of student i
       #if score >= 45 THEN
          # pass_count = pass_count + 1
       #else
          # fail_count = fail_count + 1
#4. print "Students passed:", pass_count
#5. print "Students failed:", fail_count


pass_count = 0
fail_count = 0

for count in range(1, 16):
    score = float(input(f"Enter score for student {count}: "))
    
    if score >= 45:
        pass_count += 1
    else:
        fail_count += 1

print("Students passed:", pass_count)
print("Students failed:", fail_count)
