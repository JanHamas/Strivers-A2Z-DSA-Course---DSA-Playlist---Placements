# how to draw diamond pattern using python

#  diamond
'''
*
**
***
****
***
**
*
'''

# outer loop for n/2 
#
'''
[            stars          ]
            1
            2
            3
            4
            3
            2
            1
'''
def draw_diamond(n):
    print("Diamond")
    n = int(n/2)
    for i in range(1, n+2): 
        print("*" * i)
         
    for i in range(1, n+1):
        print("*" * n, end="")
        n-=1
        print()
        
draw_diamond(8)


