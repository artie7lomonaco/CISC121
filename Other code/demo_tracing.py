"""This module demonstrates how we can use execution tracing
to debug a Python program.

Author: Ting Hu
"""

def letter_frequency(s):
    """This function takes a string of charaters s and returns a dictionary
    where the keys are the unique characters (case sensitive) from s
    and the values are the number of times that character appears in s."""
    char_list = s.split()
    
    for item in char_list:

        dict_letter_freq = 0;
        if item not in dict_letter_freq:
            dict_letter_freq[item] = 1
        else:
            dict_letter_freq[item] =+ 1

    return dict_letter_freq
    

if __name__ == "__main__":    
    # Module testing
    a_string = "Welcome to Python"
    print("In '"+a_string+"',the letter frequencies are:") 
    print(letter_frequency(a_string))

    a_string = " "
    print("In '"+a_string+"',the letter frequencies are:") 
    print(letter_frequency(a_string))

    a_string = "AaAa Aa"
    print("In '"+a_string+"',the letter frequencies are:") 
    print(letter_frequency(a_string))
