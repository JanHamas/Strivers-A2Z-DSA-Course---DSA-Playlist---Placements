#   Sorting list

'''
list_of_string = ["hamas", "jan", "khan", "sultan"]
list_of_integer = [2, 4, 3, 8, 10, 4, 0]
print(f"Before sorting string list: {list_of_string}")
print(f"Before sorting integer list: {list_of_integer}")

list_of_string.sort()
list_of_integer.sort()
print(f"After sorting string list: {list_of_string}")
print(f"After sorting integer list: {list_of_integer}")
# We can also do with sorted method which return new sorted list
'''

# Sorting list of tuples

list_of_products = [
     ("product1", 100),
    ("product2", 500),
     ("product3", 2500),
]
'''
def get_index(item):
      return item[1]
list_of_products.sort(key=get_index, reverse=False)
'''
# With lambda function
list_of_products.sort(key=lambda item: item[1])

print("Products  Prices")
print()
for item in list_of_products:
    print(item[0], item[1])






