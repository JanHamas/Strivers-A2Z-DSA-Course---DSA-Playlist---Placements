# In python they easy to convert into str and then iterate but can be also happen with by devision 10

# method one convert into string and iterate 
n = 900
digits = [ i for i in str(n) ]
print(digits)

# method two using devision
n = 10
digits = []
while n > 0:
    digits.append(n % 10)  # 10 % 10 = 0,   1 % 10 = 1   
    n = n // 10 # divide and round whole nereast integer   10 // 10 = 1
    #print(n / 10) # divide normal 5.0

digits.reverse() # for correct order
print(digits)




