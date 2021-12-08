from config_db import *
from control_input import *

if __name__ == '__main__':
    # Create instance of class:
    my_db = MyDataBase()
    # Connect to database
    my_db.connect_db()
    # Create table 'phones' and watches if they do not exists:
    my_db.create_table_phones()
    my_db.create_table_watches()

    # Select table you want to use:
    print("Select the table you want to use: ")
    print("1 - phones table")
    print("2 - watches table")
    db_option = select_option(1, 2)
    if db_option == 1:
        my_db.set_table_name("phones")
    elif db_option == 2:
        my_db.set_table_name("watches")

    print("\nWhat do you want to do? Choose the right option: ")
    print("1 - view storage content")
    print("2 - find a product in storage")
    print("3 - find a product by key word")
    print("4 - add new product")
    print("5 - remove the product from the database")
    print("6 - edit product information", end='\n\n')

    start_option = select_option(1, 6)
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

    # Close connection with DB:
    my_db.close_connection()
