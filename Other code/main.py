def is_in_str(a_string,a_char):
    result = False
    for c in a_string:
        if c == a_char:
            result = True

    return result

def odd_or_even(x):
    remainder = x%2
    if remainder == 0:
        return "even"

    else:
        return "odd"

def less_sublist(a_list,a_value):
    sublist = []

    for num in a_list:

        if num < a_value:

            sublist.append(num)

    return sublist


def reverse_words(s):
    s_list = s.split()
    print(s_list)
    reversed = []
    for word in s_list:
        reversed.insert(-1,word)

    print(reversed)

    return " ".join(reversed)


def is_palindrome(w):
    w_reversed = ""
    for i in range(len(w)):

        w_reversed = w_reversed + w[len(w)-1-i]

    return w == w_reversed


def search_value(a_dict,a_value):
    for k,v in a_dict.items():
        if v == a_value:
            return k

x = {"John":90, "Joe":85, "Jane":93}




