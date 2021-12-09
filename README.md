# Storage database with Python and MySQL

## Description

The programme is used to manage a storage which initially contains two products: 
* phones
* watches

Each product is stored in a separate table with corresponding columns.

To create a tables in the database, the **create_table_phones()** and **create_table_watches()** methods available in the MyDataBase class object are used. 

The following queries were used to create them:

* to create phones table:

```query
CREATE TABLE IF NOT EXISTS phones (brand  VARCHAR(50), model VARCHAR(50), color VARCHAR(50), 
id int PRIMARY KEY AUTO_INCREMENT);
```

* to create watches table:

```query
CREATE TABLE IF NOT EXISTS watches (brand  VARCHAR(50), type VARCHAR(50), color VARCHAR(50), 
material VARCHAR(50), id int PRIMARY KEY AUTO_INCREMENT);
```

## Creating a virtual environment

Open a terminal in your project directory and type the following command:

```bash
python -m venv venv
```
This will create a virtual environment named **venv**. To activate the virtual environment type the following command in your terminal:

```bash
"venv/scripts/activate.bat"
```

Next you have to install all required packages.


## Packages

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all required packages, which are listed in the **requirements.txt** file. You can use the command below.

```bash
pip install -r requirements.txt
```

## Launch

To run the application, use the **main.py** file found in the repository. You can use a terminal by typing the following command or run it from the IDE.

```bash
python main.py
```

When you start the program you will see the menu shown below:

```terminal
Connected to the database
Select the table you want to use:
1 - phones table
2 - watches table
Insert option:

Insert option: 
```
You need to select a product now. After selecting one of the options, a menu will be displayed for further operation of the programme.

```terminal
What do you want to do? Choose the right option:
1 - view storage content
2 - find a product in storage
3 - find a product by keyword
4 - add new product
5 - remove the product from the database
6 - edit product information

Insert option: 
```
Now select one of the available options. As you can see, it is possible to view the contents of the database, add a new product, search for existing products, change information and delete a product from the database.

## Closing words

The **MyDataBase.py** module contains the MyDataBase class, which contains methods to initialise the database connection and product management. In the **connect_db()** method, enter the appropriate database-related data to ensure a valid database connection.

```python
self.db = mysql.connector.connect(
    host="localhost",
    user="username",
    password="your-password",
    database="database-name"
)
```

The **control_input.py** module contains a functions to retrieve the relevant data from the terminal.

The program is a good base for further development, by adding more capabilities such as: adding new products to the database, adding new options related to the operation of the database (e.g. product counter in the database).

I hope you enjoy using it.
