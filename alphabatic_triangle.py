#
'''
A
AB
ABC
ABCD
ABCDE
'''

# outer loop five time
# make a list from alphabet   abc = [A,B,C,D,E]

def triangle(abc):
    for i in range(len(abc)+1):   # 5
        for j in range(i):   
            print(abc[j], end="")
        print()
    print()

abc = ["A", "B", "C", "D", "E"]
triangle(abc)

# Inverted
'''
A B C D E
A B C D
A B C
A B
A
'''

def inverted_triangle(abc):
    for i in  range(len(abc), 0, -1):   #
        for j in range(i):  
            print(abc[j], end="")
        print()

abc = ["A", "B", "C", "D", "E"]
inverted_triangle(abc)
