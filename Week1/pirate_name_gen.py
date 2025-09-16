# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 18:57:00 2024

@author: tashr
"""

import random

Name_1 = ["Jolly", "Old", "One-eyed", "Stinky", "Pegleg", "Phlegmatic"]
Name_2 = ["Bud", "Sally", "Davie", "Sam"]
Name_3 = ["blue", "Orange", "pink", "red"]


# get 3 name first last and middle names then prints it out

def get_a_pirate_name():
    """
    Here is the docstring for get_a_pirate_name() function.
    
    there are no input parameters
    """
    first = random.sample(Name_1, 1)
    last = random.sample(Name_2, 1)
    third = random.sample(Name_3, 1)
    outname = first[0]+" " + last[0] + " " + third[0]
    return outname


print(get_a_pirate_name())

# 1.The names are string variables.

# Done!
