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

@db_session
def create_entities(database):
    database.User(username="Josh01", email="josh@gmail.com", password="pass", age=25, location='London')
    database.User(username="Sarah02", email="sarah@gmail.com", password="pass", age=34, location='New York')
    database.User(username="Harris03", email="harris@gmail.com", password="pass", age=45, location='Toronto')

# ex. uncomment the below and run `python part_one.py` in the terminal
trial_db = define_database('postgres', 'postgres://localhost:5432/user-database')
create_entities(trial_db)
