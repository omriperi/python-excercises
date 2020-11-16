# 2

"""
Answers:
#1 + 2 - 
The pyhton import failed because by default, while the python interpreter
looks for packages we want to import (import some_package) it look on
pre-defined location that "python_import" directory folder
isn't part of them
In order to import the "python_import" package we shuold add the directory
location into the python import search paths

One (popular) way to do that is adding the "python_import" directory
into the "sys.path" location, making python search imports in that location
"""

# 3
import sys
sys.path.append("~/python_import")

# 4
import my_first_import

"""
Answers:
#1 - 
At this stage we'll have the text 'Hey I'm importing myself!' to the screen
that's because when python imports a module it runs his code
We have a code printing the string 'Hey I'm importing myself!' inside the module
we've imported and that's the reason we see it on the screen
If the code in the module we've imported will make pythn exit 
(sys.exit(0)) our program can exist just because of import!
"""

# 5
"""
Answers:
#1 - 
"path" is a python LIST found inside the "sys" package
#2 - 
Paths found inside the "path" list are the python import search location
when we're importing some package, python looks at the locations
found inside the "path" list, if it won't find it, and error will 
occur
"""
