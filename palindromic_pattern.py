# how to like palindromic number pattern
'''
  1           1
  12       21
  123   321
 12344321
'''

# outer loop for four lines
# Put spaces and decrease that spaces
# two loop for right and left

def palindromic_pattern(n):
    for i in range(1, n+1):
        # right triangle
        for j in range(1, i+1):
            print(j, end="")
        # spaces
        print(" " * (n-i), end="")  
        # left triangle
        for j in range(1, i+1):  # 
            print(i+1-j, end="")  # 
        print()

palindromic_pattern(8)
            
    
