# Storage-database

The program is used to service a store that initially contains two products: phones and watches.
Each product is stored in a separate table with corresponding columns.

The main.py file is the main file that should be run.
The config_db.py file contains the MyDataBase class containing all the methods needed to handle the program and the database.
File functions.py contains additional functions used in the program.

There are functions available in the program to connect to the database, and to create two tables:
- phones: brand varchar(50), model varchar(50), color varchar(50), id int AI PK.
- watches: brand varchar(50), type varchar(50), color varchar(50), material varchar(50), id int AI PK.

It is recommended to run the program from the cmd console.
At the beginning, the user is asked to enter the user name and password to the database. 
Then he has the opportunity to select the table on which he wants to work.

After selecting the table, a list of operations that can be performed is displayed. These are:
- checking the stock content,
- finding a specific product in the database,
- finding a product in the database by keyword,
- adding a new product to the database,
- deleting an existing product,
- editing an existing product.

The program is a good base for further development, by adding more capabilities such as: 
adding new products to the database, adding new options related to the operation of the database (e.g. counter 
products in the database).
