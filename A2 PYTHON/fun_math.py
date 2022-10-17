'''Here we have the factorial Calculator function:
'''


def cal_factorial(x):
    y = 1                       #Starts at 1 so we do not start multipllying by 0
    for i in range(1,x+1,1):    #For loop that multiplies i * y every time increased by 1
        y *= i;
    return y


"""Here we have the list multpiples function"""
def list_multiples(number,length):
    multiples_list = list()                     #Empty list
    for i in range(1,(number*length)+1,1):      #loops until reaches number*length since the last number in list is equivelant to number*length
        if (i % number == 0):
            multiples_list.append(i);           #Adds multiples to list

    return multiples_list


'''Here we have the find max in a list function'''
def find_max(a_list):
    x = a_list[0]                               #starts by setting the first element as the baseline
    for i in a_list:
        if (x <= i):                            #if element is greater than x value, x gets replaced by that value.
            x = i;
    return x

'''Module testing'''
if __name__ == "__main__":

#--------------------------------------------------Testing cal_factorial----------------------------------------------

    print("Testing cal_factorial with 0, 1, and 9:")

    #case 1 (if x is zero)
    x = 0
    print("Factorial of",x,"is",cal_factorial(x))

    #case 2 (if x is 1)
    x = 1
    print("Factorial of",x,"is",cal_factorial(x))

    #Case 3 (any positive number)
    x = 9
    print("Factorial of",x,"is",cal_factorial(x))

    #Case 4 (any positive number)
    x = 10
    print("Factorial of",x,"is",cal_factorial(x))

    #Case 5 (any positive number)
    x = 20
    print("Factorial of",x,"is",cal_factorial(x))

    print("\n")

#-------------------------------------Testing list_multiples-----------------------------------------------------

    print("Testing list_multiples with (0,5), (5,0), (0,0),(5,5), (7,11):")

    #case 1 (how many multiples 0 has)
    x = 0
    y = 5
    print("Factors of",x,",",y,"times is",list_multiples(x,y))

    #case 2 (zero multiples for a number)
    x = 5
    y = 0
    print("Factors of",x,",",y,"times is",list_multiples(x,y))

    #case 3 (zero multiples of 0)
    x = 0
    y = 0
    print("Factors of",x,",",y,"times is",list_multiples(x,y))

    #Case 4  (5 multiples of 5)
    x = 5
    y = 5
    print("Factors of",x,",",y,"times is",list_multiples(x,y))

    #Case 5  (different number of multiples for a number)
    x = 7
    y = 11
    print("Factors of",x,",",y,"times is",list_multiples(x,y))

    print("\n")

#--------------------------------------------------Testing find_max---------------------------------------------------

    #Case 1 (all elements are equal)
    list = [7,7,7,7,7,7]
    print("Max in this list is",find_max(list))

    #Case 2 (all elements are negative)
    list = [-99,-45,-7,-24,-1000,-69]
    print("Max in this list is",find_max(list))

    #Case 3 (all elements are postive)
    list = [1,7,2,3,77,9]
    print("Max in this list is",find_max(list))\

    #Case 4 (elements are from negative to postitive)
    list = [-111,7,-343,55,0,9000]
    print("Max in this list is",find_max(list))

    #Case 5 (Alternating positive and negative)
    list = [1,-2,3,-4,5,-6,7]
    print("Max in this list is",find_max(list))


#-----------------------------------------------------------------------------------------------------------------------