# Triangle pattern

'''
*
**
***
****
*****
'''

#  pattern have five lines so for that outer loop should be five time
#  star increase one by one until five.

'''
[       star    ]
        *
        **
        ***
        ****
        *****
'''
def triangle_pattern(n): # 10 or other values
    print(f"Right Triangle \n \n")
    for i in range(n):
        # print stars
        for j in range(i+1):
            print("*", end="")
        print()


triangle_pattern(10)


# Inverted right triangle
'''
*****
****
***
**
*
'''

def triangle_pattern(n): # 10 or other values
    print("Right inverted Triangle")
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()
        n-=1
        


triangle_pattern(10)

