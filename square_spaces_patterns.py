#     
'''
# top side
stars     spaces         stars
5            0                  5
4           2                   4
3           4                   3
2           6                   2
1           8                   1

# bottom side
stars     spaces         stars
1            8                  1
2            6                  2
3           4                   3
4           2                   4
5           0                   5
'''
def draw_square(n):
    for i in range(n):
        # top side
        for j in range(n):
            # stars
            print("*" * (n-j), end="")
            # spaces
            print(" " * (j * 2), end="")
            # stars
            print("*" * (n-j), end="")
            print()
            
        # bottom side
        for j in range(n):5       8 6 4 
                # stars
                print("*" * (j+1), end="")
                # spaces
                print(" " * (n*2), end="")
                # stars
                print("*" * (j+1), end="")
                print()

draw_square(5)
        
