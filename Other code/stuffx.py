def linear_search(a, v):
    """This function takes a list a and a value as input, and returns the location of value v in a list a, or None if v is not in a."""
    i = 0
    while i < len(a) and a[i] != v:
        i += 1
    if i < len(a):
        return i

    else:
        return None

# def a_function(x_list, val):
#
#     k = 0
#
#     while k < len(x_list) and x_list[k] != val:
#         k += 1
#         print(k)
#
#
#     return k < len(x_list)


def a_function(s, c):  # s is a string and c is a letter

    l = s.split()

    n = 0

    for item in l:

        if linear_search(item, c) != None:
            n += 1

    return n

def binary_search(a,v):
    start = 0
    end = len(a)-1
    count = 0
    while start <= end:
        count += 1;
        mid = (start + end)//2
        if a[mid] == v:
            return mid
        elif  v < a[mid]:
            end = mid - 1
        else:
            start = mid + 1
        count += 1;

    return None

    print(count)

print(binary_search("abcdefghijklmnop","m"))