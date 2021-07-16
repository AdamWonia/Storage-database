import mysql.connector
from config_db import *
import functions as fcn

"""
projekt 2 zakres:
- aplikacja CLI - obługa z terminala - pierwsza wersja
- aplikcja z GUI - obsługa z menu - druga wersja (rozszerzenie pierwszej)

- scope: aplikacja do obsługi magazynu:
-- możliwość sprawdzenia stanu całego magazynu lub wybranych produktów +++


-- możliwość dodawania nowych produktów (np 3 typy: telefon, zegarek, laptop)
---> każdy produkt posiada inne pola w tabeli +++
---> pokazywać jakie są kolumny w tabeli +++
---> obługa wyjątków jak pole puste lub domyślnie wypełniaj +++
---> użytkownik wybiera który produkt chce dodać do magazynu
---> w zależności od produktu mają być odpowiednie pola do uzupełnienia
-- możliwość wyszukiwania produktów po ich nazwe lub id lub za pomocą frazy +++
-- możliwość usuwania danego produktu z bazy: +++
---> obsługa wyjątków ++++
---> zatwierdzenie przez użytkownika usuwania produktu
-- możliwość aktualizacji danych produktu lub zmiany wybranego pola +++
---> ew. edycja całego rekordu +++

"""


def main():
    # Creating instance of class:
    my_db = MyDataBase()

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
