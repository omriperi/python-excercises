"""
Note how the imports done at the top level of the python file,
this convention is "professional" convention" that we should
stick to throughout the course
"""
import random
from string import ascii_letters

NUMBER_OF_DICTS_TO_GENERATE = 10
RANDOM_NUMBER_RANGE = 10
RANDOM_STRING_LENGTH = 5

# This is the list we're going to store the 10 dicts in
# Note that the name of the list is "descriptrive" name, 
# indicating what the list includes
dicts_list = []

for _ in range(NUMBER_OF_DICTS_TO_GENERATE):
    random_number = random.randint(0, RANDOM_NUMBER_RANGE)
    string_list = random.choices(ascii_letters, k=RANDOM_STRING_LENGTH)
    random_string = ''.join(string_list)
    # creating the dict
    random_dict = {}
    random_dict['number'] = random_number
    random_dict[random_string] = random_string
    dicts_list.append(random_dict)

"""
At this stage we're having a list with NUMBER_OF_DICTS_TO_GENERATE in it
Now we shuold sort this dicts according to 'number' key they're having in them
For this purpose, we're going to use the "sort" method of list

----------------
Ths "sort" method
----------------
Lists having "sort" method, used to sort them
In general, when we're having a list of integers, for example:
integer_list = [3, 2, 1]
We can use the sort function in order to sort it
integer_list.sort()
And afterwards the list will be sorted from small to big, 
and the result will be:
integer_list = [1, 2, 3] # TRY IT WITH IPYTHON!!!

But when we're having variabls that is not integer inside a list
we should "tell" the sort method how to sort the items in the list
So we're going to tell the sort method to sort the values found in the 
list (our dicts) according to their 'number' key
"""
dicts_list.sort(key=lambda x: x['number'])