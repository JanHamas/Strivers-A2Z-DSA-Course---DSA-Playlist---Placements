#  Counter, in python from collections module a best efficient tool used for counting frequency hashable objects within an iterable (such as list, tuple, dict) and act like dictionary where key is objects and value is number of count.

# example 1
from collections import Counter

list_of_char = [ 'a', 'b', 'c', 'a', 'j', 'k']
count = Counter(list_of_char)
print(count)

string = "this is hamas wanna master in  DSA"
char_count = Counter(string)
print(char_count)
print(char_count.most_common(2))

