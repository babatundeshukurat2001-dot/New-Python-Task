#1. for count from 5 down to 1 
      # for i from count down to 1 
          # print i without a new line
      # print a new line
#2. end




for count in range(5, 0, -1):
    for i in range(count, 0, -1):
        print(i, end="")
    print()
