import fun_math

input_okay = False #variable for checking if input is correct

print("Here are the tasks: \n1 - Calculate Factorial \n2 - Generate a List of Multiples \n3 - Find Max in a List")

task_number = int(input("Please choose a task (Enter corresponding number): "))    #enter task number

#-----------------------------------------First task----------------------------------------------------------------

if (task_number == 1):

    while not input_okay:  #loop that checks if input is integer

        try:

            x = int(input("Enter integer to get factorial: "))

            input_okay = True

        except:

            print("Must enter an integer, please try again!")

    print("The factorial of",x,"is",fun_math.cal_factorial(x))  #prints out factorial of a number

#---------------------------------------Second Task---------------------------------------------------------------------

elif (task_number == 2):

    y = 0                       #initializing variables

    y_multiple_num = 0

    while not input_okay:                   #loop that checks both inputs are correct

        try:

            y = int(input("Enter a non-negative integer: "))

            y_multiple_num = int(input("Enter how many multiples of this integer you would like: "))

            input_okay = True

        except:

            print("Must enter an integer, please try again!")

    print(y_multiple_num,"multiples of",y,"are:")

    print(fun_math.list_multiples(y,y_multiple_num))        #prints list of multiples

#-----------------------------------------Third Task--------------------------------------------------------------------

elif (task_number == 3):

    while not input_okay:                       #loop to check if input is correct

        try:

            z_length = int(input("Enter number list length: "))

            input_okay = True

        except:

            print("Must enter an integer, please try again!")

    z_count = 1;                            #count of how many times loop has passed

    z_list = list()                         #empty list

    while (z_count <= z_length):

        z_element = int(input("Enter a integer to add to list: "))          #not able to use check method to see if input is correct since it would not work for some reason or if I inputed a number all the elements in list would be that number



        if (isinstance(z_element,int)):                                      #only adds int to list

            z_list.append(z_element)                                           #adds int element to list

            print((z_length - z_count),"integers to go")                        #print how mnany more integers need to be inputed

            z_count += 1                                                        #count of loop increases by 1

    print("This is your list:",z_list)

    print("The largest number in the list is",fun_math.find_max(z_list))        #prints largest element in list

#----------------------------------------------------------------------------------------------------------------------