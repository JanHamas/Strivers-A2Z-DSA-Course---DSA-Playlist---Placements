'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
'''


# outer loop for 4 lines or row
# inner loop for printing integer

def floyd_triangle(n): # 4
    num = 1
    for i in range(1, n+1):
        for j in range(1,i+1):  
            print(num, "", end="")   # 1\n,    23\n, 456\n, 78910\n,  1112131415\n  don't confuse here? logic are correct
            num+=1
        print()
        
floyd_triangle(5)
        
    
