"""This module runs the main() function for A3_2. The user inputs an integer
which will be used to create three lists in the module list_generator
Then the lists created will go through the functions created in the module
quardatic sorting, which will return the number of outer loops, inner loops,
and swaps that it takes to sort each list to ascending order.

Author:  Artie LoMonaco
Section:  001
Student number:  20216334
"""
import list_generator
import quadratic_sorts
def output_chart(a,b,c,d,e,f,g,h,i):
    """This function prints a chart containing the data of the three types of sorting."""
    print("\t\t\t# of outer loops  # of inner loops  # of swaps")
    print("Best-case\t\t",a,4*"\t",b,4*"\t",c)
    print("Worst-case\t\t",d,4*"\t",e,4*"\t",f)
    print("Randomized-case\t",g,4*"\t",h,4*"\t",i)


def main():
    """This is the main function that executes the program A3_2, prints the charts of data."""
    list_length = int(input("Please enter the length of input lists: "))
    print("Best-case example:",list_generator.list_ascending(list_length))
    print("Worse-case example:",list_generator.list_descending(list_length))
    print("Randomized example:",list_generator.list_randomized(list_length))
    a,b,c=quadratic_sorts.insertion(list_generator.list_ascending(list_length))
    d,e,f=quadratic_sorts.insertion(list_generator.list_descending(list_length))
    g,h,i=quadratic_sorts.insertion(list_generator.list_randomized(list_length))
    print("\nUsing insertion sort:")
    output_chart(a,b,c,d,e,f,g,h,i)
    a, b, c = quadratic_sorts.selection(list_generator.list_ascending(list_length))
    d, e, f = quadratic_sorts.selection(list_generator.list_descending(list_length))
    g, h, i = quadratic_sorts.selection(list_generator.list_randomized(list_length))
    print("\nUsing Selection sort:")
    output_chart(a,b,c,d,e,f,g,h,i)
    a, b, c = quadratic_sorts.bubble(list_generator.list_ascending(list_length))
    d, e, f = quadratic_sorts.bubble(list_generator.list_descending(list_length))
    g, h, i = quadratic_sorts.bubble(list_generator.list_randomized(list_length))
    print("\nUsing Bubble sort:")
    output_chart(a, b, c, d, e, f, g, h, i)
main()