# how to draw binary triangle
'''
1
01
101
0101
10101
'''

# outer loop for five lines
# inner loop

def binary_traingle(n): # 5
    for i in range(1, n+1):
        if i%2 == 0:       
            start = 0
        else:
            start = 1
        for j in range(i):
            print(start, end="")
            start = 1 - start
        print()
            
binary_traingle(5)
            
    
        
            
        
