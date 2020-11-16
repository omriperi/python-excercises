import random

####
#1
####

# This is called "LIST COMPREHENSION"
# If you don't remember what is it, please read online
first_list = [random.randrange(1, 10) for _ in range(10)]
filtered_list = []
for item in first_list:
    if item not in filtered_list:
        filtered_list.append(item)

####
# 2
####
first_list = [random.randrange(1, 10) for _ in range(10)]
second_list = [random.randrange(1, 5) for _ in range(5)]
third_list = first_list + second_list

####
# 3
####
first_list = [random.randrange(1, 10) for _ in range(10)]
second_list = [random.randrange(1, 5) for _ in range(5)]

# Option 1
third_list = []
third_list.append(first_list)
third_list.append(second_list)

# Option 2 - preferred
third_list = [first_list, second_list]

####
# 4
####
# Look how I've replace the integer came from random
# into a string inside the list comprehension
# This trick is because afterwards when I'll want to build
# a string from those integers, they should be already strings 
# and not integers
string_list = [str(random.randrange(1, 10)) for _ in range(10)]
my_string = ''.join(string_list)

####
# 5
####
list_to_delete = [random.randrange(1, 10) for _ in range(10)]

# Option 1:
list_to_delete.clear()
"""
In this option we're CLEARING the list, that means that if 
there's someone else using this list, it will not 
have it's values any more (since we've CLEARED them)
"""

# Option 2:
list_to_delete = []
"""
In this option we're not CLEARING the list, but creating a new
list instead of the old one
In this situation, if someone else using the original list 
(before we've replaced it to new one), it will still have it's values
That's a BIG difference, that we should keep in mind
"""

