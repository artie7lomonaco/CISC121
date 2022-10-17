"""This program determines a number the user has in mind based on a input range.
The user will be asked if the number in mind is larger than middle of the range,
and based on their answer the program will narrow down what the number they have in mind is
until the middle number of the range is the number they have in mind.

Author:  Artie LoMonaco
Section:  001
Student number:  20216334
"""
def main():
    """This function runs the code of the program A3_1."""
    lower_bound = int(input("Please enter lower bound: "))
    upper_bound = int(input("Please enter upper bound: "))
    mid = int((lower_bound + upper_bound)/2)
    number_found= False
    user_number=0
    count=0
    while(number_found == False):
        if (upper_bound != lower_bound):
            print("Is the number greater than", mid)
            num_question = input("Enter y for yes and n for no: ")
            if (num_question == "y" or num_question == "Y"):
                lower_bound = mid + 1
                mid = int((lower_bound + upper_bound)/2)
            elif (num_question == "n" or num_question == "N"):
                upper_bound = mid
                mid = int((lower_bound + upper_bound) / 2)
            count+=1
        elif (upper_bound == lower_bound):
            user_number = mid
            number_found = True
    print("The number you had in mind is",user_number)
main()