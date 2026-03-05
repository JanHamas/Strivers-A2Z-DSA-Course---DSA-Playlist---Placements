# 200 Pattern Programs with Numbered Headers

## Basic Square/Rectangle Patterns (1-15)

```
1. Square of Stars
   *****
   *****
   *****
   *****
   *****
   
 # Solution
 # Outer loop for number of lines   n 
 # Inner loop again for number of row which is n
n = 4
for i in range(n): # 4
    for j in range(n):
        print("*", end="")
    # break lines
    print()
    
    
2. Square of Numbers - Same Row
   11111
   22222
   33333
   44444
   55555
   
   
  # Outer loop number of lines = n
  # Inner loop print i n times
n = 4
for i in range(1, n+1):
    for j in range(n):
        print(i, end="")
    
    # line break
    print()

3. Square of Numbers - Sequential
   12345
   12345
   12345
   12345
   12345
# Outer loop number of lines = n
# Inner loop every time i to n

n = 5
for i in range(1, n+1):
    for j in range(1, n+1):
        print(j, end="")
    # break line
    print()
    

4. Square of Alphabets
   AAAAA
   BBBBB
   CCCCC
   DDDDD
   EEEEE
# Outer loop number of letters
# Inner loop print each letter length of letters
letters = ['A', 'B', 'C', 'E', 'F']

for i in range(len(letters)):
    for j in range(len(letters)):
        print(letters[i], end="")
    
    # break line
    print()
    

        
5. Right Triangle - Increasing Stars
   *
   **
   ***
   ****
   *****

# Outer loop number of lines = n
# * multiplies i

n = 5
for i in range(1, n+1):
    print("*" * i)
    
6. Right Triangle - Increasing Numbers
   1
   12
   123
   1234
   12345
 # Outer loop number of lines = n
 # Inner loop number of i
n = 4
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    # break line
    print()

7. Right Triangle - Increasing Alphabets
   A
   AB
   ABC
   ABCD
   ABCDE
  
 # Outer loop number of letters length
 # Inner loop number of i
 
letters = ['A', 'B', 'C', 'E']
for i in range(len(letters)):
    for j in range(i+1):
        print(letters[j], end="")
    # break line
    print()
    

8. Right Triangle - Repeated Numbers
   1
   22
   333
   4444
   55555
   
  # Outer loop number of lines = n
  # Inner loop print i and i time
n = 5
for i in range(1, n+1):
    for j in range(i):
        print(i, end="")
    # break line
    print()

9. Inverted Right Triangle - Stars
   *****
   ****
   ***
   **
   *
# this can be done with one loop
# number of lines n and "*" * i but should be start from n and decrement 1
n = 5
for i in range(n, 0, -1):
    print("*" * i)
    
10. Inverted Right Triangle - Numbers
    12345
    1234
    123
    12
    1

# Outer loop run iterate number of lines = n
# Inner loop should be start 1 to n but n should decrement by 1

n = 5
for i in range(1, n+1):
    for j in range(1, n+2-i): #  5+2-1=6,   5+2-2=5, 5+2-3=4 ...
        print(j, end="")
    # break line
    print()
    
11. Inverted Right Triangle - Alphabets
    ABCDE
    ABCD
    ABC
    AB
    A

12. Mirror Right Triangle - Stars
        *
       **
      ***
     ****
    *****

13. Mirror Right Triangle - Numbers
        1
       12
      123
     1234
    12345

14. Mirror Right Triangle - Alphabets
        A
       AB
      ABC
     ABCD
    ABCDE

15. Hollow Square
    *****
    *      *
    *      *
    *      *
    *****
```
# Outer loop for number of rows = rows
# If row was first or last then print stars number of rows    if row == 0 or row+1-rows == 0:
# spaces equal 2-rows = 3     
rows = 10
for row in range(rows):
    if row == 0 or row+1-rows == 0:
        print("*" * rows)
    else:
        # star
        print("*", end="")
        # spaces
        print(" " * (rows-2), end="")
        # star
        print("*")
            
        
        
    



## Number Patterns (16-40)

```
16. Floyd's Triangle
    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15

17. Floyd's Triangle - Even Numbers
    2
    4 6
    8 10 12
    14 16 18 20
    22 24 26 28 30

18. Floyd's Triangle - Odd Numbers
    1
    3 5
    7 9 11
    13 15 17 19
    21 23 25 27 29

19. Pascal's Triangle - Basic
       1
      1 1
     1 2 1
    1 3 3 1
   1 4 6 4 1

20. Pascal's Triangle - Alternative
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1

21. Number Pyramid - Ascending
        1
       2 2
      3 3 3
     4 4 4 4
    5 5 5 5 5

22. Number Pyramid - Descending
        5
       4 4
      3 3 3
     2 2 2 2
    1 1 1 1 1

23. Number Pyramid - Center Aligned
        1
       121
      12321
     1234321
    123454321

24. Number Pyramid - Reverse Center
        5
       454
      34543
     2345432
    123454321

25. Diamond Number Pattern
        1
       121
      12321
     1234321
    123454321
     1234321
      12321
       121
        1

26. Number Triangle - Repeated
    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
    4 4 4 4
    3 3 3
    2 2
    1

27. Binary Triangle
    1
    0 1
    1 0 1
    0 1 0 1
    1 0 1 0 1

28. Binary Pyramid
        1
       0 1
      1 0 1
     0 1 0 1
    1 0 1 0 1

29. Number Spiral - 3x3
    7 8 9
    6 1 2
    5 4 3

30. Number Spiral - 4x4
    7 8 9 10
    6 1 2 11
    5 4 3 12
    16 15 14 13

31. Number Spiral - 5x5
    21 22 23 24 25
    20 7 8 9 10
    19 6 1 2 11
    18 5 4 3 12
    17 16 15 14 13

32. Multiplication Table - 5x5
    1 2 3 4 5
    2 4 6 8 10
    3 6 9 12 15
    4 8 12 16 20
    5 10 15 20 25

33. Multiplication Table - Lower Triangle
    1
    2 4
    3 6 9
    4 8 12 16
    5 10 15 20 25

34. Square of Numbers - Diagonal
    1 2 3 4 5
    2 1 2 3 4
    3 2 1 2 3
    4 3 2 1 2
    5 4 3 2 1

35. Square of Numbers - Border
    1 1 1 1 1
    1 2 2 2 1
    1 2 3 2 1
    1 2 2 2 1
    1 1 1 1 1

36. Number Diamond - Border
        1
       2 2
      3   3
     4     4
    5       5
     4     4
      3   3
       2 2
        1

37. Fibonacci Triangle
    0
    1 1
    2 3 5
    8 13 21 34
    55 89 144 233 377

38. Prime Number Triangle
    2
    3 5
    7 11 13
    17 19 23 29
    31 37 41 43 47

39. Perfect Number Pyramid
       6
      28 496
    8128 33550336

40. Armstrong Number Pattern
    1
    153 370
    371 407 1634
    8208 9474 54748
```

## Star Patterns (41-80)

```
41. Pyramid of Stars
        *
       ***
      *****
     *******
    *********

42. Inverted Pyramid
    *********
     *******
      *****
       ***
        *

43. Diamond Pattern
        *
       ***
      *****
     *******
    *********
     *******
      *****
       ***
        *

44. Hollow Pyramid
        *
       * *
      *   *
     *     *
    *********

45. Hollow Inverted Pyramid
    *********
     *     *
      *   *
       * *
        *

46. Hollow Diamond
        *
       * *
      *   *
     *     *
    *       *
     *     *
      *   *
       * *
        *

47. Right Arrow Pattern
    *****
      ****
        ***
          **
            *
          **
        ***
      ****
    *****

48. Left Arrow Pattern
    *****
    ****
    ***
    **
    *
    **
    ***
    ****
    *****

49. Butterfly Pattern - Small
    *    *
    **  **
    ******
    ******
    **  **
    *    *

50. Butterfly Pattern - Large
    *        *
    **      **
    ***    ***
    ****  ****
    **********
    **********
    ****  ****
    ***    ***
    **      **
    *        *

51. Heart Pattern
     **   **
    **** ****
    *********
     *******
      *****
       ***
        *

52. Cross Pattern
    *     *
     *   *
      * *
       *
      * *
     *   *
    *     *

53. X Pattern
    *       *
     *     *
      *   *
       * *
        *
       * *
      *   *
     *     *
    *       *

54. Plus Sign
        *
        *
        *
    *********
        *
        *
        *

55. Square with X Inside
    *********
    **     **
    * *   * *
    *  * *  *
    *   *   *
    *  * *  *
    * *   * *
    **     **
    *********

56. Hourglass Pattern
    *********
     *******
      *****
       ***
        *
       ***
      *****
     *******
    *********

57. Sandglass Pattern
    *********
     *     *
      *   *
       * *
        *
       * *
      *   *
     *     *
    *********

58. Christmas Tree
        *
       ***
      *****
     *******
    *********
        *
       ***
      *****
     *******
        *
       ***
      *****
        *
       ***
        *

59. Star Burst
        *
       ***
      *****
     *******
    *********
      *****
       ***
        *
         *

60. Sun Pattern
        *
       ***
      *****
    *********
      *****
       ***
        *
    *********
      *****
       ***
        *

61. Diamond in Square
    *********
    **** ****
    ***   ***
    **     **
    *       *
    **     **
    ***   ***
    **** ****
    *********

62. Zigzag Pattern
    *       *
     *     *
      *   *
       * *
        *
       * *
      *   *
     *     *
    *       *

63. Wave Pattern - 3 Waves
    *   *   *   *
     * * * * * *
      *   *   *

64. Wave Pattern - 4 Waves
    *     *     *
     *   * *   *
      * *   * *
       *     *

65. Spiral Star - Small
    ****
    *  *
    *  *
    ****

66. Spiral Star - Medium
    *******
    *     *
    * *** *
    * * * *
    * *** *
    *     *
    *******

67. Spiral Star - Large
    *********
    *       *
    * ***** *
    * *   * *
    * * * * *
    * *   * *
    * ***** *
    *       *
    *********

68. Double Pyramid
    *     *
    **   **
    *** ***
    *******
    *** ***
    **   **
    *     *

69. Star Ladder
    *
    **
    * *
    *  *
    *   *
    *    *
    *******

70. Staggered Stars
    *
     *
      *
       *
        *
       *
      *
     *
    *

71. Diagonal Line
    *
     *
      *
       *
        *

72. Reverse Diagonal
            *
           *
          *
         *
        *

73. Both Diagonals
    *       *
     *     *
      *   *
       * *
        *
       * *
      *   *
     *     *
    *       *

74. Chess Board Pattern
    * * * * *
     * * * * *
    * * * * *
     * * * * *
    * * * * *

75. Diamond of Stars
        *
       * *
      * * *
     * * * *
    * * * * *
     * * * *
      * * *
       * *
        *

76. Hollow Diamond of Stars
        *
       * *
      *   *
     *     *
    *       *
     *     *
      *   *
       * *
        *

77. Star Box
    *********
    *       *
    *       *
    *       *
    *********

78. Star Frame
    *********
    * ***** *
    * *   * *
    * *   * *
    * ***** *
    *********

79. Star Window
    *********
    * *   * *
    *  * *  *
    *   *   *
    *  * *  *
    * *   * *
    *********

80. Star Flower
        *
       ***
      *****
    * * * * *
      *****
       ***
        *
```

## Character/Alphabet Patterns (81-110)

```
81. Alphabet Triangle - A
    A
    B B
    C C C
    D D D D
    E E E E E

82. Alphabet Pyramid
        A
       A B
      A B C
     A B C D
    A B C D E

83. Alphabet Diamond
        A
       A B
      A B C
     A B C D
    A B C D E
     A B C D
      A B C
       A B
        A

84. Alphabet Square
    A B C D E
    A B C D E
    A B C D E
    A B C D E
    A B C D E

85. Reverse Alphabet Triangle
    E D C B A
    E D C B
    E D C
    E D
    E

86. Alphabet Staircase
    A
    B C
    D E F
    G H I J
    K L M N O

87. Vowel Triangle
    A
    E I
    O U A
    E I O U
    A E I O U

88. Consonant Pyramid
        B
       C D
      F G H
     J K L M
    N P Q R S

89. Alphabet Spiral
    A B C D E
    T U V W F
    S X Y Z G
    R Q P O H
    Q P O N I

90. Word Pattern - HELLO
    H
    H E
    H E L
    H E L L
    H E L L O

91. Word Pattern - PYRAMID
    P
    P Y
    P Y R
    P Y R A
    P Y R A M
    P Y R A M I
    P Y R A M I D

92. Initial Pattern - A
        *
       * *
      * * *
     * * * *
    *       *
    *       *
    *********
    *       *
    *       *

93. Initial Pattern - B
    *****
    *   *
    *   *
    *****
    *   *
    *   *
    *****

94. Initial Pattern - C
    *****
    *
    *
    *
    *
    *
    *****

95. Initial Pattern - D
    ****
    *   *
    *   *
    *   *
    *   *
    *   *
    ****

96. Initial Pattern - E
    *****
    *
    *
    ****
    *
    *
    *****

97. Initial Pattern - F
    *****
    *
    *
    ****
    *
    *
    *

98. Initial Pattern - G
    *****
    *
    *
    *  **
    *   *
    *   *
    *****

99. Initial Pattern - H
    *   *
    *   *
    *   *
    *****
    *   *
    *   *
    *   *

100. Initial Pattern - I
     *****
       *
       *
       *
       *
       *
     *****

101. Initial Pattern - J
     *****
        *
        *
        *
        *
     *  *
     ****

102. Initial Pattern - K
     *   *
     *  *
     * *
     **
     * *
     *  *
     *   *

103. Initial Pattern - L
     *
     *
     *
     *
     *
     *
     *****

104. Initial Pattern - M
     *   *
     ** **
     * * *
     *   *
     *   *
     *   *
     *   *

105. Initial Pattern - N
     *   *
     **  *
     * * *
     *  **
     *   *
     *   *
     *   *

106. Initial Pattern - O
     *****
     *   *
     *   *
     *   *
     *   *
     *   *
     *****

107. Initial Pattern - P
     *****
     *   *
     *   *
     *****
     *
     *
     *

108. Initial Pattern - Q
     *****
     *   *
     *   *
     *   *
     * * *
     *  **
     **** *

109. Initial Pattern - R
     *****
     *   *
     *   *
     *****
     *  *
     *   *
     *    *

110. Initial Pattern - S
     *****
     *
     *
     *****
        *
        *
     *****
```

## Mathematical Patterns (111-140)

```
111. Power of 2 Triangle
    2^0 = 1
    2^1 = 2
    2^2 = 4
    2^3 = 8
    2^4 = 16
    2^5 = 32

112. Power of 3 Pyramid
        3^0 = 1
       3^1 = 3
      3^2 = 9
     3^3 = 27
    3^4 = 81
   3^5 = 243

113. Square Numbers Pattern
    1^2 = 1
    2^2 = 4
    3^2 = 9
    4^2 = 16
    5^2 = 25
    6^2 = 36
    7^2 = 49
    8^2 = 64
    9^2 = 81
    10^2 = 100

114. Cube Numbers Pattern
    1^3 = 1
    2^3 = 8
    3^3 = 27
    4^3 = 64
    5^3 = 125
    6^3 = 216
    7^3 = 343
    8^3 = 512
    9^3 = 729
    10^3 = 1000

115. Factorial Triangle
    0! = 1
    1! = 1
    2! = 2
    3! = 6
    4! = 24
    5! = 120
    6! = 720
    7! = 5040
    8! = 40320
    9! = 362880
    10! = 3628800

116. Fibonacci Spiral
    0
    1 1
    2 3 5
    8 13 21 34
    55 89 144 233 377

117. Prime Number Spiral
        2
       3 5
      7 11 13
     17 19 23 29
    31 37 41 43 47

118. Multiplication Pyramid
        1
       2 4
      3 6 9
     4 8 12 16
    5 10 15 20 25

119. Addition Pyramid
        1
       2 3
      4 5 6
     7 8 9 10
    11 12 13 14 15

120. Subtraction Pyramid
        5
       4 3
      3 2 1
     2 1 0 -1
    1 0 -1 -2 -3

121. Division Pyramid
        1
       2 1
      3 1 0
     4 2 1 0
    5 2 1 1 0

122. Modulo Pyramid
        0
       1 0
      2 1 0
     3 2 1 0
    4 3 2 1 0

123. Binary Pyramid
        1
       1 0
      1 0 1
     1 0 1 0
    1 0 1 0 1

124. Hexadecimal Pyramid
        1
       2 3
      4 5 6
     7 8 9 A
    B C D E F

125. Octal Pyramid
        1
       2 3
      4 5 6
     7 10 11 12
    13 14 15 16 17

126. Roman Numerals Pattern
    I
    II III
    IV V VI
    VII VIII IX X
    XI XII XIII XIV XV

127. Pascal's Triangle - Mod 2
        1
       1 1
      1 0 1
     1 1 1 1
    1 0 0 0 1

128. Pascal's Triangle - Mod 3
        1
       1 1
      1 2 1
     1 0 0 1
    1 1 1 1 1

129. Sine Wave Pattern
       *     *     *
      * *   * *   * *
     *   * *   * *   *
    *     *     *     *

130. Cosine Wave Pattern
    *     *     *     *
     *   * *   * *   *
      * *   * *   * *
       *     *     *

131. Exponential Growth
    2^0 = 1
    2^1 = 2
    2^2 = 4
    2^3 = 8
    2^4 = 16
    2^5 = 32
    2^6 = 64
    2^7 = 128

132. Logarithmic Pattern
    log1 = 0
    log2 = 0.3
    log3 = 0.48
    log4 = 0.6
    log5 = 0.7
    log6 = 0.78
    log7 = 0.85
    log8 = 0.9
    log9 = 0.95
    log10 = 1

133. Trigonometric Values
    sin0 = 0
    sin30 = 0.5
    sin45 = 0.707
    sin60 = 0.866
    sin90 = 1

134. Mathematical Constants
    π = 3.14
    e = 2.718
    √2 = 1.414
    √3 = 1.732
    φ = 1.618

135. Fraction Pyramid
    1/2
    1/3 2/3
    1/4 2/4 3/4
    1/5 2/5 3/5 4/5
    1/6 2/6 3/6 4/6 5/6

136. Decimal to Binary
    1 = 1
    2 = 10
    3 = 11
    4 = 100
    5 = 101
    6 = 110
    7 = 111
    8 = 1000
    9 = 1001
    10 = 1010

137. Decimal to Octal
    1 = 1
    2 = 2
    3 = 3
    4 = 4
    5 = 5
    6 = 6
    7 = 7
    8 = 10
    9 = 11
    10 = 12

138. Decimal to Hexadecimal
    1 = 1
    2 = 2
    3 = 3
    4 = 4
    5 = 5
    6 = 6
    7 = 7
    8 = 8
    9 = 9
    10 = A
    11 = B
    12 = C
    13 = D
    14 = E
    15 = F

139. ASCII Table Pattern
    65 = A
    66 = B
    67 = C
    68 = D
    69 = E
    70 = F
    71 = G
    72 = H
    73 = I
    74 = J
    75 = K
    76 = L
    77 = M
    78 = N
    79 = O
    80 = P
    81 = Q
    82 = R
    83 = S
    84 = T
    85 = U
    86 = V
    87 = W
    88 = X
    89 = Y
    90 = Z

140. Unicode Pattern
    ☀ ☁ ☂ ☃
    ★ ☆ ☯ ☮
    ♠ ♣ ♥ ♦
    ♪ ♫ ♩ ♬
    ☎ ☏ ☑ ☒
```

## Complex & Combined Patterns (141-170)

```
141. Number-Star Hybrid
    1 * 2 * 3
    * 4 * 5 *
    6 * 7 * 8
    * 9 * 10 *
    11 * 12 * 13

142. Star-Number Pyramid
        *
       1*
       *2*
       3*4*
       *5*6*
       7*8*9*

143. Calculator Display
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
    | 0 | . | = |
    +---+---+---+

144. Digital Clock Display
     --        --    --        --
    |  |    |    |    |    |  |  |
     --        --    --        --
    |  |    |    |    |    |  |  |
     --        --    --        --

145. Chess Board with Numbers
    1♜ 2♞ 3♝ 4♛ 5♚ 6♝ 7♞ 8♜
    9♟ 10♟ 11♟ 12♟ 13♟ 14♟ 15♟ 16♟
    17♙ 18♙ 19♙ 20♙ 21♙ 22♙ 23♙ 24♙
    25♖ 26♘ 27♗ 28♕ 29♔ 30♗ 31♘ 32♖

146. Sudoku Grid
    +-------+-------+-------+
    | 1 2 3 | 4 5 6 | 7 8 9 |
    | 4 5 6 | 7 8 9 | 1 2 3 |
    | 7 8 9 | 1 2 3 | 4 5 6 |
    +-------+-------+-------+
    | 2 3 4 | 5 6 7 | 8 9 1 |
    | 5 6 7 | 8 9 1 | 2 3 4 |
    | 8 9 1 | 2 3 4 | 5 6 7 |
    +-------+-------+-------+
    | 3 4 5 | 6 7 8 | 9 1 2 |
    | 6 7 8 | 9 1 2 | 3 4 5 |
    | 9 1 2 | 3 4 5 | 6 7 8 |
    +-------+-------+-------+

147. Magic Square - 3x3
    8 1 6
    3 5 7
    4 9 2

148. Magic Square - 4x4
    16 2 3 13
    5 11 10 8
    9 7 6 12
    4 14 15 1

149. Magic Square - 5x5
    17 24 1 8 15
    23 5 7 14 16
    4 6 13 20 22
    10 12 19 21 3
    11 18 25 2 9

150. Latin Square - 4x4
    1 2 3 4
    2 3 4 1
    3 4 1 2
    4 1 2 3

151. Graeco-Latin Square
    1A 2B 3C 4D
    2C 1D 4A 3B
    3D 4C 1B 2A
    4B 3A 2D 1C

152. Number Cross
        1
       2 2
      3   3
     4     4
    5       5
     4     4
      3   3
       2 2
        1

153. Star Cross
        *
       * *
      *   *
     *     *
    *       *
     *     *
      *   *
       * *
        *

154. Diamond inside Square
    *********
    **** ****
    ***   ***
    **     **
    *       *
    **     **
    ***   ***
    **** ****
    *********

155. Square Spiral
    *********
    *       *
    * ***** *
    * *   * *
    * * * * *
    * *   * *
    * ***** *
    *       *
    *********

156. Concentric Squares
    555555555
    544444445
    543333345
    543222345
    543212345
    543222345
    543333345
    544444445
    555555555

distance = min(
    row,            # top
    col,            # left
    n - 1 - row,    # bottom
    n - 1 - col     # right
)

157. Concentric Circles
    33333333333
    32222222223
    32111111123
    32100000123
    32100000123
    32100000123
    32111111123
    32222222223
    33333333333

158. Target Pattern
        1
       212
      32123
     4321234
    543212345
     4321234
      32123
       212
        1

159. Bullseye
    55555
    54445
    54345
    54445
    55555

160. Spider Web
    * | * | *
    --+---+--
    * | * | *
    --+---+--
    * | * | *

161. Maze Pattern
    *********
    *       *
    * *** ***
    * * *   *
    * * *** *
    *   *   *
    *** * ***
    *       *
    *********

162. Labyrinth
    *********
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    *********

163. Checkerboard
    X O X O X
    O X O X O
    X O X O X
    O X O X O
    X O X O X

164. Diamond Checkerboard
        X
       O O
      X X X
     O O O O
    X X X X X
     O O O O
      X X X
       O O
        X

165. Zigzag Line
    *       *       *
     *     * *     *
      *   *   *   *
       * *     * *
        *       *

166. Wave Line
    *******       *******
           *     *
            *   *
             * *

167. Mountain Range
           /\      /\
          /  \    /  \
         /    \  /    \
        /      \/      \

168. Valley Pattern
    \      /      \      /
     \    /        \    /
      \  /          \  /
       \/            \/

169. Staircase Pattern
    *
     *
      *
       *
        *
         *
          *
           *

170. Pyramid Stairs
        *
       **
      ***
     ****
      ***
       **
        *
```

## Special & Fun Patterns (171-200)

```
171. Christmas Tree with Decorations
        *
       *@*
      *@*@*
     *@*@*@*
    *********
        ||
        ||
        ||

172. Snowflake Pattern
        *
       * *
        *
     * * * * *
        *
       * *
        *

173. Flower Pattern
        *
       ***
      *****
     *** ***
      *****
       ***
        *

174. Sun with Rays
        *
       ***
      *****
    *********
      *****
       ***
        *
    *********
      *****
       ***
        *

175. Rainbow Pattern
    RRRRRRRRR
     OOOOOOO
      YYYYY
       GGG
        B
       III
      VVVVV
     IIIIIII
    RRRRRRRRR

176. Flag Pattern - India
    🟧🟧🟧🟧🟧🟧
    🟧🟧🟧🟧🟧🟧
    ⚪⚪⚪⏺⚪⚪
    ⚪⚪⚪⏺⚪⚪
    🟩🟩🟩🟩🟩🟩
    🟩🟩🟩🟩🟩🟩

177. Flag Pattern - USA
    ★★★★★★★★
    ⬜⬜⬜⬜⬜⬜
    🟥🟥🟥🟥🟥🟥
    ⬜⬜⬜⬜⬜⬜
    🟥🟥🟥🟥🟥🟥
    ⬜⬜⬜⬜⬜⬜
    🟥🟥🟥🟥🟥🟥

178. Flag Pattern - Japan
    ⬜⬜⬜⬜⬜⬜
    ⬜⬜🔴🔴⬜⬜
    ⬜🔴🔴🔴🔴⬜
    ⬜🔴🔴🔴🔴⬜
    ⬜⬜🔴🔴⬜⬜
    ⬜⬜⬜⬜⬜⬜

179. Flag Pattern - UK
    ++++++++
    ++++++++
    ++++++++
    ++++++++
    ++++++++
    ++++++++

180. Dice Pattern - 1
    +-------+
    |       |
    |   O   |
    |       |
    +-------+

181. Dice Pattern - 2
    +-------+
    | O     |
    |       |
    |     O |
    +-------+

182. Dice Pattern - 3
    +-------+
    | O     |
    |   O   |
    |     O |
    +-------+

183. Dice Pattern - 4
    +-------+
    | O   O |
    |       |
    | O   O |
    +-------+

184. Dice Pattern - 5
    +-------+
    | O   O |
    |   O   |
    | O   O |
    +-------+

185. Dice Pattern - 6
    +-------+
    | O   O |
    | O   O |
    | O   O |
    +-------+

186. Playing Cards - Heart
        **
      *    *
     *      *
     *      *
      *    *
        **
         *

187. Playing Cards - Spade
        **
       *  *
      *    *
       *  *
        **
       *  *
      ******

188. Playing Cards - Club
        **
       *  *
      *    *
       *  *
        **
       ****
      *    *

189. Playing Cards - Diamond
        *
       * *
      *   *
     *     *
      *   *
       * *
        *

190. Clock Face - 12 Hours
        12
     11    1
   10        2
   9          3
    8        4
     7    5
        6

191. Clock Face - Digital
     ---
    |   |
    |   |
     ---
    |   |
    |   |
     ---

192. Smiley Face
     *******
    *       *
    *  O O  *
    *   ^   *
    *  ---  *
    *       *
     *******

193. Sad Face
     *******
    *       *
    *  O O  *
    *   v   *
    *  ---  *
    *       *
     *******

194. Surprised Face
     *******
    *       *
    *  O O  *
    *   o   *
    *  O O  *
    *       *
     *******

195. Animal Face - Cat
      /\_/\
     ( o o )
     (  ^  )
      (___)
     (     )
      (___)

196. Animal Face - Dog
       __
      / _)
     /  /
    /  /
   (__/

197. Animal Face - Rabbit
     (\\_/)
     (o o)
     ( V )
     (   )
      ( )

198. Animal Face - Bear
      ___
     / _ \
    | ( ) |
    (  ^  )
     (___)

199. Animal Face - Owl
      ___  
     (o o) 
    (  V  )
     (___)
      | |
      | |

200. Complete Pattern Collection
    ╔═══════════════════════╗
    ║    200 PATTERNS       ║
    ║  COMPLETE COLLECTION  ║
    ║    PROGRAMMING        ║
    ║     PRACTICE          ║
    ╚═══════════════════════╝
```

## Bonus: Pattern Categories Summary

```
201. Summary Grid
    ┌─────────────────────────────────┐
    │ Basic Patterns    : 1-15        │
    │ Number Patterns   : 16-40       │
    │ Star Patterns     : 41-80       │
    │ Alphabet Patterns : 81-110      │
    │ Math Patterns     : 111-140     │
    │ Complex Patterns  : 141-170     │
    │ Fun Patterns      : 171-200     │
    │ Bonus             : 201         │
    └─────────────────────────────────┘
```

## Quick Reference Guide

| Category | Pattern Numbers | Difficulty |
|----------|----------------|------------|
| Basic Square/Rectangle | 1-15 | ⭐ |
| Number Patterns | 16-40 | ⭐⭐ |
| Star Patterns | 41-80 | ⭐⭐ |
| Alphabet Patterns | 81-110 | ⭐⭐ |
| Mathematical Patterns | 111-140 | ⭐⭐⭐ |
| Complex/Combined | 141-170 | ⭐⭐⭐⭐ |
| Special/Fun | 171-200 | ⭐⭐⭐ |

**Happy Coding!** Remember to:
- Start with basic patterns
- Understand the logic before coding
- Practice regularly
- Try to create your own variations
- Optimize your solutions

These patterns will help you master loops, conditionals, and algorithmic thinking! 🚀
