# how to draw square pattern
'''
*****
*****
*****
*****
*****
'''
# outer loop for five lines
# inner loop again for five start

def draw_square(n): # 5
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()
        
draw_square(6)

'''
*****
*****
*****
*****
*****
*****
'''
def draw_square(n): # 6
    for i in range(n):
        for j in range(n-1):
            print("*", end="")
        print()
    
print(f"five stars with 6 lines.  \n ")
draw_square(6)

