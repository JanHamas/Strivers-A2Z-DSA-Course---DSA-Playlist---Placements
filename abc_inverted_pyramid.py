# Outer loop number of lines  length of letters
# in innner loop we are starting letters length - i - 1 and stop step length characters


'''
E             
DE         
CDE        
BCDE    
ABCDE  
'''

def draw_triangle(letters):
    for i in range(len(letters)):
        for j in range(len(letters) - i - 1, len(letters) ):  
            print(letters[j], end="")
        print()
 
letters = ["A", "B", "C", "D", "E"]
draw_triangle(letters) 



    
