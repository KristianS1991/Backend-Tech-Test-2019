from pony.orm import Database, db_session, Required

# db = Database('postgres', 'postgres://localhost:5432/user-database')

def define_entity(db):
    class User(db.Entity):
        username = Required(str)
        email = Required(str)
        password = Required(str)
        age = Required(int)
        location = Required(str)

def define_database(*db_params):
    db = Database(*db_params)
    define_entity(db)
    db.generate_mapping(create_tables=True)
    return db

@db_session
def create_entities(database):
    database.User(username="Josh01", email="josh@gmail.com", password="pass", age=25, location='London')
    database.User(username="Sarah02", email="sarah@gmail.com", password="pass", age=34, location='New York')
    database.User(username="Harris03", email="harris@gmail.com", password="pass", age=45, location='Toronto')

# create_entities(db)
