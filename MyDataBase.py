import mysql.connector
import control_input as fcn
from getpass import getpass
from mysql.connector.locales.eng import client_error


class MyDataBase:
    def __init__(self):
        self.db = None
        self.table_name = None

    def __str__(self):
        return "Database"

    def __del__(self):
        self.close_connection()

    def set_table_name(self, table_name):
        """
        Indicates the table in the database that will be used.
        param table_name: The name of the table in the database.
        """
        self.table_name = table_name

    def connect_db(self):
        """
        Establishes a connection to the selected database. The user must provide correct
        database information such as host, user name, password
        and the name of the database.

        Return: Returns a MySQLConnection object.
        """
        try:
            self.db = mysql.connector.connect(
                host="localhost",  # input("Enter host name: "),
                user="username",  # input("Enter username: "),
                password="password",  # getpass("Enter password: "),
                database="database"  # input("Enter database name: "),
            )
            print("Connected to the database")
        except Exception as e:
            print(f"Cannot connect to the database: {e}")
        finally:
            return self.db

    def create_table_phones(self):
        """
        Creates a 'phones' table in the database if it does not already exist.
        """
        my_cursor = self.db.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS phones (brand  VARCHAR(50), model VARCHAR(50), 
        color VARCHAR(50), id int PRIMARY KEY AUTO_INCREMENT);
        """
        try:
            my_cursor.execute(query)
        except Exception as e:
            print(f"Something went wrong! {e}")
        finally:
            my_cursor.close()

    def create_table_watches(self):
        """
        Creates a 'watches' table in the database if it does not already exist.
        """
        my_cursor = self.db.cursor()
        query = """
            CREATE TABLE IF NOT EXISTS watches (brand  VARCHAR(50), type VARCHAR(50), color VARCHAR(50), 
            material VARCHAR(50), id int PRIMARY KEY AUTO_INCREMENT);
            """
        try:
            my_cursor.execute(query)
        except Exception as e:
            print(f"Something went wrong! {e}")
        finally:
            my_cursor.close()

    def show_all_records(self):
        """
        Displays all records found in the database.
        """
        show_query = None
        select_query = None
        my_cursor = self.db.cursor()
        try:
            if self.table_name == "phones":
                show_query = "SHOW COLUMNS FROM phones;"
                select_query = "SELECT * FROM phones;"
            elif self.table_name == "watches":
                show_query = "SHOW COLUMNS FROM watches;"
                select_query = "SELECT * FROM watches;"
            # Get column names from the database:
            my_cursor.execute(show_query)
            results = my_cursor.fetchall()
            # Display column names:
            print("\nStore content: (", end='')
            for i in range(0, len(results)):
                print(results[i][0], end=', ')
            print(")")
            # Get results from the database:
            my_cursor.execute(select_query)
            results = my_cursor.fetchall()
            # Display the records found:
            if len(results) > 0:
                for result in results:
                    for element in result:
                        print(element, end=', ')
                    print("")
            else:
                print("Store is empty!")
        except Exception as e:
            print(f"Something went wrong! {e}")
        finally:
            my_cursor.close()

    def show_single_record(self):
        """
        Displays the selected record from the database table.
        """
        select_query = None
        my_cursor = self.db.cursor()
        if self.table_name == "phones":
            print("Insert phone brand and model to find it: ")
            while True:
                brand = input("Insert brand: ").lower().strip()
                model = input("Insert model: ").lower().strip()
                if (brand.isspace() or brand == '') or (model.isspace() or model == ''):
                    print("You put invalid data, please try again")
                else:
                    break
            select_query = f"SELECT * FROM phones WHERE brand = '{brand}' AND model = '{model}';"
        elif self.table_name == "watches":
            print("Insert watch brand to find it: ")
            while True:
                brand = input("Insert brand: ").lower().strip()
                if brand.isspace() or brand == '':
                    print("You put invalid data, please try again")
                else:
                    break
            select_query = f"SELECT * FROM watches WHERE brand = '{brand}';"
        # Select product information from a database table:
        try:
            # Get results from the database:
            my_cursor.execute(select_query)
            results = my_cursor.fetchall()
            # Display the record found:
            if len(results) > 0:
                print("Product found: ")
                for row in results:
                    for element in row:
                        print(element, end=', ')
                    print("")
            else:
                print("No results found")
        except Exception as e:
            print(f"Something went wrong! {e}")
        finally:
            my_cursor.close()

    def find_by_keyword(self):
        """
        Displays the found record by keyword from the database table.
        """
        select_query = None
        my_cursor = self.db.cursor()
        while True:
            word = input("Insert keyword: ").lower().strip()
            if word.isspace() or word == '':
                print("You put invalid data, please try again")
            else:
                break
        # Try to find record by keyword:
        try:
            if self.table_name == "phones":
                select_query = f"SELECT * FROM phones WHERE brand LIKE '%{word}%' OR model LIKE '%{word}%';"
            elif self.table_name == "watches":
                select_query = f"SELECT * FROM watches WHERE brand LIKE '%{word}%' OR type LIKE '%{word}%' " \
                               f"OR material LIKE '%{word}%';"
            # Get results from the database:
            my_cursor.execute(select_query)
            results = my_cursor.fetchall()
            # Display the record found:
            if len(results) > 0:
                print("Product found: ")
                for row in results:
                    for element in row:
                        print(element, end=', ')
                    print("")
            else:
                print("No results found")
        except Exception as e:
            print(f"Something went wrong! {e}")
        finally:
            my_cursor.close()

    def add_new_product(self):
        """
        Adds a new product to the database.
        """
        insert_query = None
        my_cursor = self.db.cursor()
        print("Add needed information about the product: ")
        if self.table_name == "phones":
            while True:
                brand = input("Insert brand: ").lower().strip()
                model = input("Insert model: ").lower().strip()
                color = input("Insert color: ").lower().strip()
                if (brand.isspace() or brand == '') or \
                        (model.isspace() or model == '') or (color.isspace() or color == ''):
                    print("You put invalid data, please try again")
                else:
                    insert_query = "INSERT INTO phones (brand, model, color) VALUES ('%s', '%s', '%s');" \
                                   % (brand, model, color)
                    break
        elif self.table_name == "watches":
            while True:
                brand = input("Insert brand: ").lower().strip()
                w_type = input("Insert type: ").lower().strip()
                color = input("Insert color: ").lower().strip()
                material = input("Insert material: ").lower().strip()
                if (brand.isspace() or brand == '') or (w_type.isspace() or w_type == '') or \
                        (color.isspace() or color == '') or (material.isspace() or material == ''):
                    print("You put invalid data, please try again")
                else:
                    insert_query = "INSERT INTO watches (brand, type, color, material) " \
                                   "VALUES ('%s', '%s', '%s', '%s');" % (brand, w_type, color, material)
                    break
        # Try to add the new product to the database:
        try:
            my_cursor.execute(insert_query)
            self.db.commit()
            print(f"Product added!")
        except Exception as e:
            print(f"Something went wrong! {e}")
        finally:
            my_cursor.close()

    def delete_record(self):
        """
        Deletes the product from the database.
        """
        select_query = None
        delete_query = None
        my_cursor = self.db.cursor()
        given_id = fcn.input_int("Insert product ID: ")
        try:
            if self.table_name == "phones":
                select_query = f"SELECT * FROM phones WHERE id = '{given_id}'"
                delete_query = f"DELETE FROM phones WHERE id = '{given_id}';"
            elif self.table_name == "watches":
                select_query = f"SELECT * FROM watches WHERE id = '{given_id}'"
                delete_query = f"DELETE FROM watches WHERE id = '{given_id}';"
            # Get results from the database:
            my_cursor.execute(select_query)
            results = my_cursor.fetchall()
            # Check if the record is found:
            if len(results) == 0:
                print("There is not product with this ID")
            else:
                print(f"Product with ID = {given_id}: ")
                # Display the record found:
                for row in results:
                    for element in row:
                        print(element, end=', ')
                    print("")
                print("Are you sure you want to delete the product? [Y or N]: ")
                option = fcn.input_str('Y', 'N')
                # Delete record from the database:
                if option == 'Y':
                    my_cursor.execute(delete_query)
                    self.db.commit()
                    print("Product has been deleted!")
                else:
                    print("Nothing has been deleted")
        except Exception as e:
            print(f"Something went wrong! {e}")
        finally:
            my_cursor.close()

    def edit_record(self):
        """
        Edits the selected product information.
        """
        select_query = None
        update_query = None
        my_cursor = self.db.cursor()
        given_id = fcn.input_int("Insert product ID: ")
        if self.table_name == "phones":
            select_query = f"SELECT * FROM phones WHERE id = '{given_id}';"
        elif self.table_name == "watches":
            select_query = f"SELECT * FROM watches WHERE id = '{given_id}';"
        # Get results from the database:
        my_cursor.execute(select_query)
        results = my_cursor.fetchall()
        # Check if the record is found:
        if len(results) == 0:
            print("There is no product with this ID")
        else:
            print(f"Product with ID = {given_id}: ")
            for row in results:
                for element in row:
                    print(element, end=', ')
                print("")
            print("Insert new product details: ")
            if self.table_name == "phones":
                while True:
                    brand = input("Insert brand: ").lower().strip()
                    model = input("Insert model: ").lower().strip()
                    color = input("Insert color: ").lower().strip()
                    if (brand.isspace() or brand == '') or (model.isspace() or model == '') \
                            or (color.isspace() or color == ''):
                        print("You put invalid data, please try again")
                    else:
                        break
                update_query = f"UPDATE phones SET brand = '{brand}', model = '{model}', " \
                               f"color = '{color}' WHERE id = '{given_id}';"
            elif self.table_name == "watches":
                while True:
                    brand = input("Insert brand: ").lower().strip()
                    w_type = input("Insert type: ").lower().strip()
                    color = input("Insert color: ").lower().strip()
                    material = input("Insert material: ").lower().strip()
                    if (brand.isspace() or brand == '') or (w_type.isspace() or w_type == '') or \
                            (color.isspace() or color == '') or (material.isspace() or material == ''):
                        print("You put invalid data, please try again")
                    else:
                        break
                update_query = f"UPDATE watches SET brand = '{brand}', type = '{w_type}', " \
                               f"color = '{color}', material = '{material}' WHERE id = '{given_id}';"
            try:
                my_cursor.execute(update_query)
                self.db.commit()
                print("Product edited!")
            except Exception as e:
                print(f"Something went wrong! {e}")

        my_cursor.close()

    def find_phone_id(self, brand, model, color):
        """
        Finds the product with specified ID.
        :param brand: Phone brand to insert.
        :param model: Phone model to insert.
        :param color: Phone color to insert.
        :return: Record found in the database.
        """
        phone_id = None
        my_cursor = self.db.cursor()
        try:
            my_cursor.execute(f"SELECT id FROM phones WHERE brand = '{brand}' "
                              f"AND model = '{model}' AND color = '{color}';")
            phone_id = my_cursor.fetchone()
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

        return phone_id[0]

    def find_watch_id(self, brand, watch_type, color, material):
        """
        Finds the product with specified ID.
        :param brand: Watch brand to insert.
        :param watch_type: Watch type to insert.
        :param color: Watch color to insert.
        :param material: Watch material to insert.
        :return: Record found in the database.
        """
        watch_id = None
        my_cursor = self.db.cursor()
        try:
            my_cursor.execute(f"SELECT id FROM watches WHERE brand = '{brand}' "
                              f"AND type = '{watch_type}' AND color = '{color}' AND material = '{material}';")
            watch_id = my_cursor.fetchone()
        except Exception as e:
            print(f"Something went wrong! {e}")
        finally:
            my_cursor.close()

        return watch_id[0]

    def close_connection(self):
        """
        Closes the connection with database.
        """
        self.db.close()
