#      some rules for print patterns and almost patters used nested loop.
# 1. for the outer loop, count the number of lines.
# 2. for the inner loop, focus on the columns and connect them somehow to the rows
# 3. print them inside inner loop
# 4. observe summitry (optional) because required for some patterns.


# Patterns 1
'''
*   *   *   *
*   *   *   *
*   *   *   *
*   *   *   *
'''
# for outer loop will be run for four time so rule one apply here
# for inner loop connect somehow to lines apply here in below example
'''

def print_pattern(n):
    for _ in range(n):
        for _ in range(n):
              print("*", end="  ")
        print()
        
n = 10
print_pattern(n)
'''

# Patterns 2
'''
*   
*   *   
*   *   *   
*   *   *   *
'''

'''
def print_pattern(n):
    for i in range(n):
        j = 0
        while j < i :
            print("*", end="  ")
            j+=1
        print()
        
n = 10
print_pattern(n)
'''

# pattern 3
'''
1
12
123
1234
'''
'''
def print_pattern(n):
    for i in range(n):
        j = 1
        while j < i :
            print(j, end="  ")
            j+=1
        print()
        
n = 10
print_pattern(n)
'''

# pattern 4
'''
1
22
333
4444
'''

'''
def print_pattern(n):
    for i in range(n):
        j = 0
        while j < i :
            print(i, end=" ")
            j+=1
        print()
        
n = 10
print_pattern(n)
'''

# pattern 5
'''
*   *   *   *
*   *   *   
*   *   
*   
'''
def print_pattern(n):
    for i in range(n):
        j = 0
        while j < n :
            print('*', end=" ")
            j+=1
        print()
        
n = 10
print_pattern(n)









### ⭐ Row 1

**1. Right Triangle**

```
*
**
***
****
*****
```

**2. Inverted Right**

```
*****
****
***
**
*
```

**3. Solid Square**

```
*****
*****
*****
*****
*****
```

**4. Vertical Line**

```
*
*
*
*
*
```

---

### ⭐ Row 2

**5. Right Diagonal**

```
*
 *
  *
   *
    *
```

**6. Left Diagonal**

```
    *
   *
  *
 *
*
```

**7. Half Diamond**

```
*
**
***
****
***
**
*
```

**8. Small Pyramid**

```
  *
 ***
*****
```

---

### ⭐ Row 3

**9. Inverted Pyramid**

```
*****
 ***
  *
```

**10. Full Diamond**

```
*
**
***
****
*****
****
***
**
*
```

**11. Number Triangle**

```
1
12
123
1234
12345
```

**12. Same Number**

```
1
22
333
4444
55555
```

---

### ⭐ Row 4

**13. Continuous Numbers**

```
1
23
456
78910
```

**14. Inverted Numbers**

```
12345
1234
123
12
1
```

**15. Shifted Numbers**

```
5
45
345
2345
12345
```

**16. Binary Triangle**

```
1
01
101
0101
10101
```

---

### ⭐ Row 5

**17. Floyd Triangle**

```
1
2 3
4 5 6
7 8 9 10
```

**18. Same Number Rows**

```
1
2 2
3 3 3
4 4 4 4
```

**19. Number Diamond**

```
1
12
123
1234
123
12
1
```

**20. Reverse Numbers**

```
5
44
333
2222
11111
```

---

### ⭐ Row 6

**21. Alphabet Triangle**

```
A
AB
ABC
ABCD
ABCDE
```

**22. Same Alphabet**

```
A
BB
CCC
DDDD
```

**23. Inverted Alphabet**

```
ABCDE
ABCD
ABC
AB
A
```

**24. Reverse Alphabet**

```
A
BA
CBA
DCBA
```

---

### ⭐ Row 7

**25. Continuous Alphabet**

```
A
BC
DEF
GHIJ
```

**26. Alphabet Diamond**

```
A
AB
ABC
ABCD
ABC
AB
A
```

**27. Shifted Alphabet**

```
E
DE
CDE
BCDE
ABCDE
```

**28. Alphabet Inverted Space**

```
A B C D E
A B C D
A B C
A B
A
```

---

### ⭐ Row 8

**29. Star Pyramid**

```
    *
   ***
  *****
 *******
```

**30. Inverted Pyramid**

```
*******
 *****
  ***
   *
```

**31. Star Diamond**

```
    *
   ***
  *****
   ***
    *
```

**32. Number Palindrome**

```
1
121
12321
1234321
```

---

### ⭐ Row 9

**33. Centered Numbers**

```
    1
   121
  12321
 1234321
```

**34. Hollow Triangle**

```
*
* *
*   *
*     *
*******
```

**35. Hollow Square**

```
*****
*   *
*   *
*   *
*****
```

**36. Extended Floyd**

```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

---

### ⭐ Row 10

**37. Incremental Rows**

```
1
2 3
3 4 5
4 5 6 7
```

**38. Binary Pattern**

```
1
10
101
1010
10101
```

**39. Spaced Triangle**

```
*
* *
* * *
* * * *
* * * * *
```

**40. Reverse Spaced**

```
        *
      * *
    * * *
  * * * *
* * * * *
```

---

If you want, I can next:

* ✅ give **empty templates** under each
* ✅ add **expected loop counts**
* ✅ give **Python solutions row-wise**

Just say the word 🚀

