#      defaultdict
# defaultdict is from collection module which is a bit different form stander one raise key error when key don't have and defaultdict one initialize default value

# Stander one dict
'''
dict = { 
    "name": "Hamas",
    "age": 20
}
print(dict['name'])
print(dict['marks']) # KeyError
'''
# Example 2
'''
dict = {}
dict["a"] +=1
print(dict)
'''

# defaultdict
'''
from collections import defaultdict

dict = defaultdict(int)  #
print(dict["marks"])
'''
from collections import defaultdict
d = defaultdict(int)
d["a"] +=1 # This will create a key if doesn't exist
print(d)

