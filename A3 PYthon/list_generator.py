"""This module list_generator contains three functions that generates three
random lists; one in ascending order, descending order, and randomized. The
length of the three lists depends on the integer the user inputs in main()
in A3_2 module.

Author:  Artie LoMonaco
Section:  001
Student number:  20216334
"""
import random
def list_ascending(a):
    """This function creates a list of random numbers in ascending order."""
    best_list=list()
    for j in range(a):
        x = round(random.uniform(1, 100), 2)
        best_list.append(x)
    for key in range(1,len(best_list)):
        i = key
        while(i>0 and best_list[i-1] > best_list[i]):
            best_list[i-1],best_list[i] = best_list[i], best_list[i-1]
            i = i -1
    return best_list


def list_descending(b):
    """This function creates a list of random numbers in descending order."""
    worse_list=list()
    for k in range(b):
        y = round(random.uniform(1,100),2)
        worse_list.append(y)
    for key in range(1,len(worse_list)):
        i = key
        while(i>0 and worse_list[i-1] < worse_list[i]):
            worse_list[i-1],worse_list[i] = worse_list[i], worse_list[i-1]
            i = i -1
    return worse_list


def list_randomized(c):
    """This function creates a list of random numbers in neither ascending or descending order."""
    rand_list=list()
    for l in range(c):
        z = round(random.uniform(1,100),2)
        rand_list.append(z)
    return rand_list