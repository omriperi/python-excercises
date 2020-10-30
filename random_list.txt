Difficulty Level: 2
------------
Goals:
------------
- Breaking for loops
- Reversed Lists
- Using random, imports

------------
Material:
------------
1:
Python Random Package:
https://docs.python.org/3.6/library/random.html
1. Note how many options we're having here
2. Please open IPython and play with the random package a little bit

2:
Lists methods
https://docs.python.org/3.6/tutorial/datastructures.html
Try to see what are the methods here,
try to look for appropriate list method for revesing a list

Excercise:
1. 
Please prepare a new list, this list should contain
10 random values, each random value from 1 to 10

Hint #1:
Check material 1 in order to see how to generate a random number

2. 
Sort the list from small to large, that means that if the list 
you got from the first step is:
[5,4,6,1,4,3], after you've sorted it it should be:
[1,3,4,4,5,6]
Note that if there's duplicate number they should reside one next to each other

Hint #1:
Open a new list that should contain the sorted numbers,
run over the original list and look for the smallest number
when you see the smallest number put it inside the new sorted list

Hint #2:
After you run on the first list and find the smallest number,
remove if from the first list

Hint #3:
Removing a list item done by:
- Having the index of the item we want to remove, and than do something like:
original_list.remove(index_of_item_we_want_to_remove)

3. Reverse the sorted list you just got, 
if the list you've sorted looks like:
[1,2,3,4], you need to reverse it to [4,3,2,1]

Hint #1:
List have a special function for reversing it, please look at material #2
and look for the method that reverse the list
