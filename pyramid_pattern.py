#   

'''
         *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *   
'''

# outer loop for five lines
# first four space then decrease one by one
# frist one start then increase two by two

'''
def print_pyramid(n):
    for i in range(1, n + 1): # 5
         # print spaces
        print(" " * (n - i), end="")
        # print stars
        print("*" * (i * 2 - 1))
        

print_pyramid(4)
'''
    
'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
'''
#  1, [ spaces   stars     spaces ]
            0              9            0
            1               7           1
            2               5           2
            3              3            3
            4               1           4
'''


# first we don't need to print last space if we do or not cannot see their effect.
# we need to outer loop number of lines which 5 for up pyramid

def inverted_pyramid(n): # 5
        for i in range(1, n+1):
             # spaces
             print(" " * (i * 1 - 1), end="" ) # 0, 1, 2, 3 ... n
             # stars
             print("*" * (n * 2 - 1))             # 5*2-1=9,   4*2-1=7
             n-=1

inverted_pyramid(5)
             

             

  
 
