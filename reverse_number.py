# Reverse number
# write a program to generate the reverse of a given number N. If number has trailing zeros, then its reverse will not include them. for E.G  Reverse of  10400 will be 401 instead of 00401

# using list comprehension is very easy
# convert n to string and reverse and convert to int

# using digit extraction
# create a var r_num = 0
# get last digit 
# r_num = ( r_num * 10 ) + ld
# get divide and store n = n // 10

# Method 1
'''
n = 10400
# convert to string
n = str(n)
# reverse string using slicing
n = n[::-1]
# remove leading zero and convert to integer
n = int(n)
'''

# 
n = 10400
r_num  = 0
while n > 0:
    ld = n % 10
    r_num = (r_num * 10) + ld
    n = n // 10
    
print(r_num)




