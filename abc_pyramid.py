# Outer loop number of =n
# spaces both   =  n-i
# chars increments by 2 but and should be increase and decrease.
#Example in lines 2 we have three chars but we need to print ab and a like aba, so char increase & decrease 1 time from a aba
# lines 3 have 5 characters but we need to print abcba   increase & decrease 2 time and for all like that

def draw_pyramid(n):
    for i in range(1, n+1):
        print(" " * (n-i), end="")

        char_ascii = ord('a')
        break_point = i

        for j in range(1, i*2):
            print(chr(char_ascii), end="")
            if j < break_point:
                char_ascii += 1
            else:
                char_ascii -= 1

        print()
draw_pyramid(5)
            
            
            
            
            
