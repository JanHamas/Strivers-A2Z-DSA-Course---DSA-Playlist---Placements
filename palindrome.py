# Check palindrome number
# palindrome is number which is equal to write from both left and right side like    121
# this is easy in python convert number to string and then reverse again using slice and check


n = 66666866
string_n = str(n)[::-1]

if (n == int(string_n)):
    print("Yes palindrome :", n)
else:
    print("Not palindrome : ", n)
    
# Method 2
# Using digit extractions and compare with original one.


def check_palindrome(n):
    num = n # only for last compare n are decreasing
    extracted_digits = ''
    while n > 0:
        ld = n % 10  # get last digit
        extracted_digits = extracted_digits + str(ld)
        n = n // 10
    if str(num) == extracted_digits:
        print("Yes palindrome")
    else:
        print("Not palindrome")

check_palindrome(890)

    



