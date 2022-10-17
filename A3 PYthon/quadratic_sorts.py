"""This module contains three functions that will sort the lists produced
in list_generator in main().  The functions are for the sorting methods of insertion
sort, selection sort, and bubble sort.

Author:  Artie LoMonaco
Section:  001
Student number:  20216334
"""
def insertion(list_a):
    """This function takes a list as input sorts it in ascending order using insertion sort."""
    outer_a=0
    inner_a=0
    swap_a=0
    for key in range(1,len(list_a)):
        i = key
        while(i>0 and list_a[i-1] > list_a[i]):
            list_a[i-1],list_a[i] = list_a[i], list_a[i-1]
            inner_a += 1
            swap_a += 1
            i = i -1
        outer_a +=1
    return outer_a,inner_a,swap_a


def selection(list_a):
    """This function sorts a list by a value in ascending order using selection sort."""
    outer_b = 0
    inner_b = 0
    swap_b = 0
    n = len(list_a)
    for i in range(n-1):
        current_min = i
        for j in range(i+1,n):
            if list_a[j] < list_a[current_min]:
                current_min = j
            inner_b += 1
        if current_min != i:
            list_a[i], list_a[current_min] = list_a[current_min], list_a[i]
            swap_b += 1
        outer_b += 1
    return outer_b,inner_b,swap_b


def bubble(list_a):
    """This function sorts a list in ascending order using bubble sort."""
    outer_c = 0
    inner_c = 0
    swap_c = 0
    swap_flag = True
    n = len(list_a)
    while swap_flag:
        swap_flag = False
        for i in range(1,n):
            if list_a[i-1] > list_a[i]:
                list_a[i-1],list_a[i]=list_a[i],list_a[i-1]
                swap_flag = True
                swap_c += 1
            inner_c += 1
        n -= 1
        outer_c += 1
    return outer_c,inner_c,swap_c