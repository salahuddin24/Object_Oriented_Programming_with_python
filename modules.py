# a module is a file consisting of Python code. A module can define functions classes and variables
# 1. building module
from math import pow, sqrt
print(pow(2,3))
print(sqrt(55))

# 2. user define module

from  moduleTest import rectangle_area,triangle_area # (*) star diya shobgola import kora jay
triangle_area(4,5)
rectangle_area(2,4)

