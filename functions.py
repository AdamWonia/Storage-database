def select_option(lb, ub):
    while True:
        option = input("Insert option: ")
        if option.isnumeric() and int(option) in range(lb, ub + 1):
            break
        else:
            print("You put invalid option, insert number between {} and {}".format(lb, ub))

    return int(option)


def input_int(msg=None):
    while True:
        try:
            input_data = int(input(msg))
            break
        except:
            print("You put invalid data, please enter an integer")

    return input_data
