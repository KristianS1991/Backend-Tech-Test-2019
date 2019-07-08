from pony.orm import Database, db_session, Required

def define_entity(db):
    # pylint: disable=W0612
    class User(db.Entity):
        username = Required(str)
        email = Required(str)
        password = Required(str)
        age = Required(int)
        location = Required(str)

def define_database(*db_args, **db_kwargs):
    db = Database(*db_args, **db_kwargs)
    define_entity(db)
    db.generate_mapping(create_tables=True)
    return db

user_data = [dict(username="Josh01", email="josh@gmail.com", password="pass", age=25, location='London'),
        dict(username="Sarah02", email="sarah@gmail.com", password="pass", age=34, location='New York'),
        dict(username="Harris03", email="harris@gmail.com", password="pass", age=45, location='Toronto')]

@db_session
def create_entities(database, data):
    for el in data:
        database.User(**el)

# ex. uncomment the below and run `python part_one.py` in the terminal
trial_db = define_database('postgres', 'postgres://localhost:5432/user-database')
create_entities(trial_db, user_data)
