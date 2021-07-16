import mysql.connector
import functions as fcn
from getpass import getpass


# nie wiem czy nie zrobić licznika jeszcze w tabeli
# bo mogą być dwa takie same telegfony
# i ktory wtedy usunie? hmm

# nazyw kolumn dynamicznie w 'show content':
# show columns from phones;


class MyDataBase:
    def __init__(self):
        self.db = self.connect_db()

    def __del__(self):
        self.close_connection()

    @staticmethod
    def connect_db():
        # Connecting to database:
        db = None
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",  # input("Enter username: "), only for test in PyCharm
                password="adam_root",  # getpass("Enter password: "),
                database="testdatabase"
            )
            print("Connected to the database")
        except Exception as e:
            print("Cannot connect to the database")
            print(e)
        finally:
            return db

    def show_all_records(self):
        # Show all record in table:
        print("Store content: (Brand, Model, Color, ID)")
        my_cursor = self.db.cursor()
        try:
            my_cursor.execute("SELECT * FROM phones")
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
        print("Insert phone brand and model to find it: ")
        while True:
            brand = input("Insert brand: ").lower().strip()
            model = input("Insert model: ").lower().strip()
            if (brand.isspace() or brand == '') or (model.isspace() or model == ''):
                print("You put invalid data, please try again")
            else:
                break
        my_cursor = self.db.cursor()
        try:
            my_cursor.execute(f"SELECT * FROM phones WHERE brand = '{brand}' AND model = '{model}';")
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
        while True:
            word = input("Insert key word: ").lower().strip()
            if word.isspace() or word == '':
                print("You put invalid data, please try again")
            else:
                break
        my_cursor = self.db.cursor()
        try:
            my_cursor.execute(f"SELECT * FROM phones WHERE brand LIKE '%{word}%' OR model LIKE '%{word}%';")
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
        print("Add needed information about product: ")
        while True:
            brand = input("Insert brand: ").lower().strip()
            model = input("Insert model: ").lower().strip()
            color = input("Insert color: ").lower().strip()
            if (brand.isspace() or brand == '') or \
                    (model.isspace() or model == '') or (color.isspace() or color == ''):
                print("You put invalid data, please try again")
            else:
                break
        my_cursor = self.db.cursor()
        try:
            my_cursor.execute("INSERT INTO phones (brand, model, color) VALUES (%s, %s, %s);", (brand, model, color))
            self.db.commit()
            print(f"Product: {brand}, {model}, {color} added!")
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

    def delete_record(self):
        # Delete product from database:
        given_id = fcn.input_int("Insert product ID: ")
        my_cursor = self.db.cursor()
        try:
            my_cursor.execute(f"SELECT * FROM phones WHERE id = '{given_id}'")
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
                    my_cursor.execute(f"DELETE FROM phones WHERE id = '{given_id}';")
                    self.db.commit()
                    print("Phone has been deleted!")
                else:
                    print("Nothing has been deleted")
        except Exception as e:
            print("Something went wrong!")
            print(e)
        finally:
            my_cursor.close()

    def edit_record(self):  # try catch
        # Edit product information:
        given_id = fcn.input_int("Insert product ID: ")
        my_cursor = self.db.cursor()
        my_cursor.execute(f"SELECT * FROM phones WHERE id = '{given_id}';")
        results = my_cursor.fetchall()
        if len(results) == 0:
            print("There is no product with this ID")
        else:
            print("Insert new product details: ")
            while True:
                brand = input("Insert brand: ").lower().strip()
                model = input("Insert model: ").lower().strip()
                color = input("Insert color: ").lower().strip()
                if (brand.isspace() or brand == '') or (model.isspace() or model == '') \
                        or (color.isspace() or color == ''):
                    print("You put invalid data, please try again")
                else:
                    break
            try:
                my_cursor.execute(f"UPDATE phones SET brand = '{brand}', model = '{model}', "
                                  f"color = '{color}' WHERE id = '{given_id}';")
                self.db.commit()
                print("Product edited!")
            except Exception as e:
                print("Something went wrong!")
                print(e)

        my_cursor.close()

    def find_record_id(self, brand, model, color):
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

    def close_connection(self):
        self.db.close()
