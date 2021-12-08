<<<<<<< HEAD
import mysql.connector
import functions as fcn
from getpass import getpass


class MyDataBase:
    def __init__(self):
        self.db = self.connect_db()
        self.table_name = None

    def __del__(self):
        self.close_connection()

    def get_table_name(self, table_name):
        self.table_name = table_name

    @staticmethod
    def connect_db():
        # Connecting to database:
        db = None
        try:
            db = mysql.connector.connect(
                host="localhost",
                user=input("Enter username: "),
                password=getpass("Enter password: "),
                database="testdatabase"
            )
            print("Connected to the database")
        except Exception as e:
            print("Cannot connect to the database")
            print(e)
        finally:
            return db

    def create_table_phones(self):
        # Create table phones with columns: brand, model, color, id:
        my_cursor = self.db.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS phones (brand  VARCHAR(50), model VARCHAR(50), 
        color VARCHAR(50), id int PRIMARY KEY AUTO_INCREMENT);
        """
        try:
            my_cursor.execute(query)
            print("Table 'phones' created!")
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

    def create_table_watches(self):
        # Create table watches with colums: brand, type, color, material, id:
        my_cursor = self.db.cursor()
        query = """
            CREATE TABLE IF NOT EXISTS watches (brand  VARCHAR(50), type VARCHAR(50), color VARCHAR(50), 
            material VARCHAR(50), id int PRIMARY KEY AUTO_INCREMENT);
            """
        try:
            my_cursor.execute(query)
            print("Table 'watches' created!")
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

    def show_all_records(self):
        # Show all record in table:
        show_query = None
        select_query = None
        my_cursor = self.db.cursor()
        try:
            if self.table_name == "phones":
                show_query = "SHOW COLUMNS FROM phones;"
            elif self.table_name == "watches":
                show_query = "SHOW COLUMNS FROM watches;"
            my_cursor.execute(show_query)
            results = my_cursor.fetchall()
            print("Store content: (", end='')
            for i in range(0, len(results)):
                print(results[i][0], end=', ')
            print(")")
            if self.table_name == "phones":
                select_query = "SELECT * FROM phones;"
            elif self.table_name == "watches":
                select_query = "SELECT * FROM watches;"
            my_cursor.execute(select_query)
            results = my_cursor.fetchall()
            if len(results) > 0:
                for row in results:
                    for element in row:
                        print(element, end=', ')
                    print("")
            else:
                print("Store is empty!")
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

    def show_record(self):
        # Show given product:
        select_query = None
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
        my_cursor = self.db.cursor()
        try:
            my_cursor.execute(select_query)
            results = my_cursor.fetchall()
            if len(results) > 0:
                print("Product found: ")
                for row in results:
                    for element in row:
                        print(element, end=', ')
                    print("")
            else:
                print("No results found")
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

    def find_by_word(self):
        # Find product by key word in brand or model:
        select_query = None
        while True:
            word = input("Insert key word: ").lower().strip()
            if word.isspace() or word == '':
                print("You put invalid data, please try again")
            else:
                break
        my_cursor = self.db.cursor()
        try:
            if self.table_name == "phones":
                select_query = f"SELECT * FROM phones WHERE brand LIKE '%{word}%' OR model LIKE '%{word}%';"
            elif self.table_name == "watches":
                select_query = f"SELECT * FROM watches WHERE brand LIKE '%{word}%' OR type LIKE '%{word}%' " \
                               f"OR material LIKE '%{word}%';"
            my_cursor.execute(select_query)
            results = my_cursor.fetchall()
            if len(results) > 0:
                print("Product found: ")
                for row in results:
                    for element in row:
                        print(element, end=', ')
                    print("")
            else:
                print("No results found")
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

    def add_new_product(self):
        # Add new product into database:
        insert_query = None
        print("Add needed information about product: ")
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
        my_cursor = self.db.cursor()
        try:
            my_cursor.execute(insert_query)
            self.db.commit()
            print(f"Product added!")
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

    def delete_record(self):
        # Delete product from database:
        select_query = None
        delete_query = None
        given_id = fcn.input_int("Insert product ID: ")
        my_cursor = self.db.cursor()
        try:
            if self.table_name == "phones":
                select_query = f"SELECT * FROM phones WHERE id = '{given_id}'"
                delete_query = f"DELETE FROM phones WHERE id = '{given_id}';"
            elif self.table_name == "watches":
                select_query = f"SELECT * FROM watches WHERE id = '{given_id}'"
                delete_query = f"DELETE FROM watches WHERE id = '{given_id}';"
            my_cursor.execute(select_query)
            results = my_cursor.fetchall()
            if len(results) == 0:
                print("There is not product with this ID")
            else:
                print(f"Product with ID = {given_id}: ")
                for row in results:
                    for element in row:
                        print(element, end=', ')
                    print("")
                print("Are you sure you want to delete the product? [Y or N]: ")
                option = fcn.input_str('Y', 'N')
                if option == 'Y':
                    my_cursor.execute(delete_query)
                    self.db.commit()
                    print("Product has been deleted!")
                else:
                    print("Nothing has been deleted")
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

    def edit_record(self):  # try catch
        # Edit product information:
        select_query = None
        update_query = None
        given_id = fcn.input_int("Insert product ID: ")
        my_cursor = self.db.cursor()
        if self.table_name == "phones":
            select_query = f"SELECT * FROM phones WHERE id = '{given_id}';"
        elif self.table_name == "watches":
            select_query = f"SELECT * FROM watches WHERE id = '{given_id}';"
        my_cursor.execute(select_query)
        results = my_cursor.fetchall()
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
                print("Something went wrong!")
                print(e)

        my_cursor.close()

    def find_phone_id(self, brand, model, color):
        # Find and return product ID:
        my_cursor = self.db.cursor()
        phone_id = None
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

    def find_watch_id(self, brand, w_type, color, material):
        # Find and return product ID:
        my_cursor = self.db.cursor()
        watch_id = None
        try:
            my_cursor.execute(f"SELECT id FROM watches WHERE brand = '{brand}' "
                              f"AND type = '{w_type}' AND color = '{color}' AND material = '{material}';")
            watch_id = my_cursor.fetchone()
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

        return watch_id[0]

    def close_connection(self):
        self.db.close()
=======
import mysql.connector
import functions as fcn
from getpass import getpass


class MyDataBase:
    def __init__(self):
        self.db = self.connect_db()
        self.table_name = None

    def __del__(self):
        self.close_connection()

    def get_table_name(self, table_name):
        self.table_name = table_name

    @staticmethod
    def connect_db():
        # Connecting to database:
        db = None
        try:
            db = mysql.connector.connect(
                host="localhost",
                user=input("Enter username: "),
                password=getpass("Enter password: "),
                database="your-database-name"
            )
            print("Connected to the database")
        except Exception as e:
            print("Cannot connect to the database")
            print(e)
        finally:
            return db

    def create_table_phones(self):
        # Create table phones with columns: brand, model, color, id:
        my_cursor = self.db.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS phones (brand  VARCHAR(50), model VARCHAR(50), 
        color VARCHAR(50), id int PRIMARY KEY AUTO_INCREMENT);
        """
        try:
            my_cursor.execute(query)
            print("Table 'phones' created!")
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

    def create_table_watches(self):
        # Create table watches with colums: brand, type, color, material, id:
        my_cursor = self.db.cursor()
        query = """
            CREATE TABLE IF NOT EXISTS watches (brand  VARCHAR(50), type VARCHAR(50), color VARCHAR(50), 
            material VARCHAR(50), id int PRIMARY KEY AUTO_INCREMENT);
            """
        try:
            my_cursor.execute(query)
            print("Table 'watches' created!")
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

    def show_all_records(self):
        # Show all record in table:
        show_query = None
        select_query = None
        my_cursor = self.db.cursor()
        try:
            if self.table_name == "phones":
                show_query = "SHOW COLUMNS FROM phones;"
            elif self.table_name == "watches":
                show_query = "SHOW COLUMNS FROM watches;"
            my_cursor.execute(show_query)
            results = my_cursor.fetchall()
            print("Store content: (", end='')
            for i in range(0, len(results)):
                print(results[i][0], end=', ')
            print(")")
            if self.table_name == "phones":
                select_query = "SELECT * FROM phones;"
            elif self.table_name == "watches":
                select_query = "SELECT * FROM watches;"
            my_cursor.execute(select_query)
            results = my_cursor.fetchall()
            if len(results) > 0:
                for row in results:
                    for element in row:
                        print(element, end=', ')
                    print("")
            else:
                print("Store is empty!")
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

    def show_record(self):
        # Show given product:
        select_query = None
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
        my_cursor = self.db.cursor()
        try:
            my_cursor.execute(select_query)
            results = my_cursor.fetchall()
            if len(results) > 0:
                print("Product found: ")
                for row in results:
                    for element in row:
                        print(element, end=', ')
                    print("")
            else:
                print("No results found")
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

    def find_by_word(self):
        # Find product by key word in brand or model:
        select_query = None
        while True:
            word = input("Insert key word: ").lower().strip()
            if word.isspace() or word == '':
                print("You put invalid data, please try again")
            else:
                break
        my_cursor = self.db.cursor()
        try:
            if self.table_name == "phones":
                select_query = f"SELECT * FROM phones WHERE brand LIKE '%{word}%' OR model LIKE '%{word}%';"
            elif self.table_name == "watches":
                select_query = f"SELECT * FROM watches WHERE brand LIKE '%{word}%' OR type LIKE '%{word}%' " \
                               f"OR material LIKE '%{word}%';"
            my_cursor.execute(select_query)
            results = my_cursor.fetchall()
            if len(results) > 0:
                print("Product found: ")
                for row in results:
                    for element in row:
                        print(element, end=', ')
                    print("")
            else:
                print("No results found")
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

    def add_new_product(self):
        # Add new product into database:
        insert_query = None
        print("Add needed information about product: ")
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
        my_cursor = self.db.cursor()
        try:
            my_cursor.execute(insert_query)
            self.db.commit()
            print(f"Product added!")
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

    def delete_record(self):
        # Delete product from database:
        select_query = None
        delete_query = None
        given_id = fcn.input_int("Insert product ID: ")
        my_cursor = self.db.cursor()
        try:
            if self.table_name == "phones":
                select_query = f"SELECT * FROM phones WHERE id = '{given_id}'"
                delete_query = f"DELETE FROM phones WHERE id = '{given_id}';"
            elif self.table_name == "watches":
                select_query = f"SELECT * FROM watches WHERE id = '{given_id}'"
                delete_query = f"DELETE FROM watches WHERE id = '{given_id}';"
            my_cursor.execute(select_query)
            results = my_cursor.fetchall()
            if len(results) == 0:
                print("There is not product with this ID")
            else:
                print(f"Product with ID = {given_id}: ")
                for row in results:
                    for element in row:
                        print(element, end=', ')
                    print("")
                print("Are you sure you want to delete the product? [Y or N]: ")
                option = fcn.input_str('Y', 'N')
                if option == 'Y':
                    my_cursor.execute(delete_query)
                    self.db.commit()
                    print("Product has been deleted!")
                else:
                    print("Nothing has been deleted")
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

    def edit_record(self):  # try catch
        # Edit product information:
        select_query = None
        update_query = None
        given_id = fcn.input_int("Insert product ID: ")
        my_cursor = self.db.cursor()
        if self.table_name == "phones":
            select_query = f"SELECT * FROM phones WHERE id = '{given_id}';"
        elif self.table_name == "watches":
            select_query = f"SELECT * FROM watches WHERE id = '{given_id}';"
        my_cursor.execute(select_query)
        results = my_cursor.fetchall()
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
                print("Something went wrong!")
                print(e)

        my_cursor.close()

    def find_phone_id(self, brand, model, color):
        # Find and return product ID:
        my_cursor = self.db.cursor()
        phone_id = None
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

    def find_watch_id(self, brand, w_type, color, material):
        # Find and return product ID:
        my_cursor = self.db.cursor()
        watch_id = None
        try:
            my_cursor.execute(f"SELECT id FROM watches WHERE brand = '{brand}' "
                              f"AND type = '{w_type}' AND color = '{color}' AND material = '{material}';")
            watch_id = my_cursor.fetchone()
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

        return watch_id[0]

    def close_connection(self):
        self.db.close()
>>>>>>> bdb13ef0b0d3e6b365a3e5e8c92be3189d928514
