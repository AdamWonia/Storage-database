from config_db import *
import functions as fcn


def main():
    # Creating instance of class:
    my_db = MyDataBase()

    # Create table 'phones' if not exists:
    my_db.create_table_phones()

    # Create table 'watches' if not exists:
    my_db.create_table_watches()

    print("Select table you want to choose: ")
    print("1 - phones")
    print("2 - watches")
    db_option = fcn.select_option(1, 2)
    if db_option == 1:
        my_db.get_table_name("phones")
    elif db_option == 2:
        my_db.get_table_name("watches")

    print("What do you want to do? Select proper option: ")
    print("1 - show store content")
    print("2 - find product in a store")
    print("3 - find product by key word")
    print("4 - add new product")
    print("5 - delete product from database")
    print("6 - edit product information")

    start_option = fcn.select_option(1, 6)
    if start_option == 1:
        my_db.show_all_records()
    if start_option == 2:
        my_db.show_record()
    if start_option == 3:
        my_db.find_by_word()
    if start_option == 4:
        my_db.add_new_product()
    if start_option == 5:
        my_db.delete_record()
    if start_option == 6:
        my_db.edit_record()

    # Closing connection with DB:
    my_db.close_connection()


if __name__ == '__main__':
    main()
