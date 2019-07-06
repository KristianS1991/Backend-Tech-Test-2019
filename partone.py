from pony.orm import Database, db_session, Required

db = Database('postgres', 'postgres://localhost:5432/user-database')

class User(db.Entity):
    username = Required(str)
    email = Required(str)
    password = Required(str)
    age = Required(int)
    location = Required(str)

db.generate_mapping(create_tables=True)

@db_session
def create_entity():
    User(username="Josh01", email="josh@gmail.com", password="pass", age=25, location='London')
    User(username="Sarah02", email="sarah@gmail.com", password="pass", age=34, location='New York')
    User(username="Harris03", email="harris@gmail.com", password="pass", age=45, location='Toronto')

create_entity()
