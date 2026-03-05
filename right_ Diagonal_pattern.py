# how to right diagonal
'''
*
 *
  *
   *
    *
'''
'''
    *
   *
  *
 *
*
'''

def draw_right_diagonal(n):
    print("Right Diagonal")
    for i in range(n):
        print(" " * i, "*")

draw_right_diagonal(5)

def draw_left_diagonal(n):
    print("Left Diagonal")
    for i in range(n):
        print(" " * (n-i), "*")

draw_left_diagonal(5)
