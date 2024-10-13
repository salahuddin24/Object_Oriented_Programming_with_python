
"""
* what is regular expression?
    => regular expression are tools for manipulating string.
* Why do we need regular expression?
    => verifying that strings match a pattern
    => performing substitutions in a string
* Regular expressions can be accessed using the re module
    - match() : matches at the beginning of a string.
    - search() : finds a match of a pattern anywhere in the string.
    - findall() : returns a list of all substrings that match a pattern.
"""

import  re
from itertools import count
from traceback import print_tb
#
# pattern = r"color"
# if re.match(pattern, "Red is a color, I love red color") :
#     print("Match")
# else:
#     print("Not Matched ")
#
# if re.search(pattern, "Red is a color, I love red color") :
#     print("Match")
# else:
#     print("Not Matched ")
#
#
# print(re.findall(pattern, "Red is a color, I love red color"))
#
#
# pattern2 = r"colour"
# text = "My favourite colour is Red"
# match = re.search(pattern2, text)
# if match:
#     print(match.start()) # je word match hobe tar first index print korbe
#     print(match.end()) # je word match hobe tar end index print korbe
#     print(match.span()) # je word match hobe tar first+end duitar index print korbe
#
#

# pattern = r"colour"
# text1 = "My favourite colour is Red. I love blue colour as well."
# text2 = re.sub(pattern, "color", text1)
# text3 = re.sub(pattern, "color", text1, count=1)
# print(text2)
# print(text3)

#meta charecter
"""
.(dot) ( any character )
^$ 
* ( o or more )
+ ( 1 or more ) 
? ( o or 1) 
{and}
"""
# pattern2 = r"colo.r" # . ar jaygay jekono charecter thakte pare
#
# if re.match(pattern2, "colour"):
#     print("matched")

# pattern3 = r"^colo..r$" # . ar jaygay jekono charecter thakte pare
#
# if re.match(pattern3, "colouar"):
#     print("matched")

# pattern3 = r"a*" # * o/j kono shokkhok a thakte parbe
#
# if re.match(pattern3, "colour"):
#     print("matched")


# pattern3 = r"a+" # * 1/more shokkhok a thakte parbe
#
# if re.match(pattern3, "colour"):
#     print("matched")


# pattern3 = r"ice(-)?cream" # * o/1 shokkhok - thakte parbe
#
# if re.match(pattern3, "ice-cream"):
#     print("matched")


# pattern3 = r"a{1,3}$" # * 1 theke 3 shokkhok a thakte parbe
#
# if re.match(pattern3, "aaa"):
#     print("matched")


# character class # set of character niya kaj kore
#
# pattern3 = r"[A-Z]"
#
# if re.match(pattern3, "SaaaSa"):
#     print("matched")

pattern3 = r"[0-9]" # * 1 theke 3 shokkhok a thakte parbe

if re.match(pattern3, "3AaKka"):
    print("matched")

















