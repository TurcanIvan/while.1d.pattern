# DRAW THIS PATTERN:     # * # * # * # * # * ....
# HW DRAW THIS: # * * # * * # * *
# 10 size

symbol = 1


print("\n")

while symbol <= 10:
    if symbol % 2 == 1:
        print("#",end=" ")
    else:
        print("*",end=" ")
            
    symbol += 1

print("\n")