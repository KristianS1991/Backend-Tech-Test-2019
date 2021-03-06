import unittest
from pony.orm import Database, db_session
from part_one import define_entity, create_entities, user_data

class TestFunc(unittest.TestCase):
    def setUp(self):
        self.db = Database(provider='sqlite', filename=':memory:')
        define_entity(self.db)
        self.db.generate_mapping(create_tables=True)
        create_entities(self.db, user_data)

    def tearDown(self):
        self.db.drop_all_tables(with_all_data=True)

    @db_session
    def test_create_entities(self):
        # pylint: disable=E1101
        user = self.db.User.get(username="Josh01")
        self.assertEqual(user.location, 'London')

if __name__ == '__main__':
    unittest.main()

# to run test, run `python part_two.py` in the terminal
