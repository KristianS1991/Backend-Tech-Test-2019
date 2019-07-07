# Backend-Technical-Test

## Technologies Used
* Python
* SQL, PostgreSQL, SQLite
* PonyORM
* Unittest
* PIP
* GitHub

## Installation
1. Clone or download the repository.
2. Run `pip install pony psycopg2-binary` in the terminal, within the repository folder.
##### For Part One:
2. In the terminal, run the Bash command `createdb user-database` to create the SQL database.
3. Run `python part_one.py` within the repository folder in the terminal, this will seed the database with the set of user data.
##### For Part Two:
4. Run `python part_two.py` within the repository folder in the terminal, this will run the unit test on the function from `part_one.py`.

## Part One
### Write a function to take a fixed set of data and insert it into a database.
To complete this task, I decided to write the script in Python, using the object relational mapping library PonyORM, to execute the necessary SQL statements to write to an SQL database. I used the PIP package manager to install the required modules. The steps below summarize the process I took to write the first draft of this script.
##### First Draft Process:
1. Import the necessary functions from the PonyORM library.
2. Create the database object `db`, and bind this object to the `user-database`.
3. Create a `User` class to model the user data to be stored in the database.
4. Generate mapping on the database object, this shows the database the format to expect for the entities.
5. Define a function, `create_entities` which implements the `User` model to store a set of user data into the `user-database`.
6. Apply the decorator function, `db_session`, to the `create_entities` function to open a session with the user-database before the function logic is executed, and then close that session.
7. Invoke the `create_entities` function.
##### First Draft
![First Draft Part One](https://i.imgur.com/g5PdQg0.png)
