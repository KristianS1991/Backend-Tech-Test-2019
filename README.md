# Backend-Technical-Test

## Technologies Used
* Python
* SQL, PostgreSQL, SQLite
* PonyORM
* unittest
* PIP
* GitHub

## Installation
1. Clone or download the repository.
2. Run `pip install pony psycopg2-binary` in the terminal, within the repository folder.
#### For Part One
2. In the terminal, run the Bash command `createdb user-database` to create the SQL database.
3. Run `python part_one.py` within the repository folder in the terminal, this will seed the database with the set of user data.
#### For Part Two
4. Run `python part_two.py` within the repository folder in the terminal, this will run the unit test on the function from `part_one.py`.

## Part One
### Write a function to take a fixed set of data and insert it into a database.
To complete this task, I decided to write the script in Python, using the object relational mapping library PonyORM, to execute the necessary SQL statements to write to an SQL database. I used the PIP package manager to install the required modules. The steps below summarize the process I took to write the first draft of this script.

#### First Draft Process
1. Import the necessary functions from the PonyORM library.
2. Create the database object `db`, and bind this object to the `user-database`.
3. Create a `User` class to model the user data to be stored in the database.
4. Generate mapping on the database object, this shows the database the format to expect for the entities.
5. Define a function, `create_entities` which implements the `User` model to store a set of user data into the `user-database`.
6. Apply the decorator function, `db_session`, to the `create_entities` function to open a session with the user-database before the function logic is executed, and then close that session.
7. Invoke the `create_entities` function.

#### First Draft
![First Draft Part One](https://i.imgur.com/g5PdQg0.png)

#### Refactoring
When I ran `part_one.py` in the terminal, it successfully seeded the database (checked this manually using `psql`). However, I came to realize later on that the way I wrote this script made it difficult when it came to testing in part two. Since the database being seeded was hardcoded, there was no way to unit test the `create_entities` function against a temporary database. Therefore, I had to refactor part one to be more versatile and allow any database object to be defined. This database object was then passed in as an argument to the `create_entities` function to be seeded.

#### Final Draft
![Final Draft Part One](https://i.imgur.com/WvOGkHQ.png)

## Part Two
### Write a unit test to verify the function works.
For part two, I needed to do some research on the best ways to unit test a function that writes to a database. I discovered a couple different ways of doing this, all revolving around the idea of generating a temporary, or "mock" database, then using the function of interest to seed that database. Tests could then be written to get data from the temporary database and determine if that data is equal to the expected value.

#### Choosing a Testing Framework
At first, I tried using the `testing.postgresql` package to set up the unit test for a `postgresql` instance. It follows similar methodology to most packages for unit testing, but it appeared to be a bit more complex for this application, as it required setting up a `PostgreSQL` server and it was meant to be used with plain `SQL` statements rather than `PonyORM`. I decided against this and continued searching for a more straightforward package. I then stumbled across `flask-testing`, the testing extension for the `Flask` framework. This package seemed to be more flexible and worked in conjunction with `PonyORM`. I wrote most of what ended up being the final draft of part two with this until I realized that I didn't need a `Flask` application and I could just use the `unittest` framework.

#### Part Two Process
1. Import the the `unittest` framework, the necessary functions from the `PonyORM` library, and the relevant functions from `part_one.py`.
2. Create a `TestFunc` class as a subclass of the `unittest.TestCase` base class.
3. Define a `setUp` method to set up the temporary database (using sqlite, storing in memory) and call the `create_entities` function, passing the temporary database as an argument.
4. Define a `tearDown` method to delete the temporary database after testing.
5. Define a `test_create_entities` method to get data from the temporary database and use the `assertEqual` method to check if this data matches the expected value.
6. Add the conditional statement at the end of script to run unit tests when the script is ran.

#### Part Two
![Part Two](https://i.imgur.com/a1SzNjP.png)

#### Success!
![Part Two in Terminal](https://i.imgur.com/LQJkuex.png)

## Part Three
###  Create a client/server application to allow discovery on a network.
####  a. A simple server that broadcasts it's existence with a set of data (i.e. ID, MAC or IP)
####  b. A client that searches for the server and displays in a terminal the data received.
