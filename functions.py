def select_option(lb, ub):
    """Returns the selected integer type option between lb and ub. Otherwise shows an error message.

            Parameters:
                lb (lower bound): Lower limit of the integer type for options.
                ub (upper bound): Upper limit of the integer type for options.
    """
    while True:
        option = input("Insert option: ")
        if option.isnumeric() and (int(option) in range(lb, ub + 1)):
            break
        else:
            print("You put invalid option, insert number between {} and {}".format(lb, ub))

    return int(option)


def input_int():
    """Returns given integer number, otherwise displays an error message."""
    while True:
        try:
            input_data = int(input())
            break
        except:
            print("You put invalid data, please enter an integer")

    return input_data


def input_str(option1=None, option2=None):
    """Returns a string variable taken from the user, otherwise displays an error message.
    If option1 and option2 are specified, the function returns one of those two options,
    otherwise it displays an error message.

            Parameters:
                option1: First option to choose of type string.
                option2: Second option to choose of type string.
    """
    while True:
        input_data = input()
        if option1 is None and option2 is None:
            if ''.join(input_data.split()).isalpha():
                break
            else:
                print("You put invalid data, please try again")

        if option1 is not None or option2 is not None:
            input_data = input_data.upper().strip()
            if input_data.isalpha() and (input_data == option1 or input_data == option2):
                break
            else:
                print("You put invalid data, please try again")

    return input_data
