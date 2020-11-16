EXAMPLE_RANDINT_ARGUMENT = 30

# 1
import random
random.randint(EXAMPLE_RANDINT_ARGUMENT)

# 2
from random import randint
randint(EXAMPLE_RANDINT_ARGUMENT)

# 3
from random import *
randint(EXAMPLE_RANDINT_ARGUMENT)
"""
Question Answer:

While using * to import entire variables from the random package,
we're importing EVERYTHING in that package, and not only what we need
The main disatvantage of this solution is that when someone read
your code it cannot know what you've using from random package
Another disatvantage is that if you're importing another package
that having the same variable name as in random, 
one will override the other
"""

# 4
from random import randint
randint = 10
randint(EXAMPLE_RANDINT_ARGUMENT)
"""
Question Answer:

When I called the last line I've got an ERROR because
randint is not a function and I've tried to call it
as a function randint() is a function call
The reason randint is not longer a variable is because the line
randint = 10 replace randint from function to integer
Remember! Python variable can be anything, function, integer, class, etc
When declaring a new integer with same name as already initialized varable
(as in line 18) we're overriding the last variable,
and that's why we're not having function anymore
"""


