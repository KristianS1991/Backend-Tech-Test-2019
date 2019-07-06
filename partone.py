from pony.orm import Database, Required

db = Database('postgres', 'postgres://localhost:5432/user-database')

class User(db.Entity):
    username = Required(str)
    password = Required(str)
    age = Required(int)
    location = Required(str)
