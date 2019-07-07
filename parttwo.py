import unittest
from unittest import TestCase
from pony.orm import Database, db_session
from flask import Flask
from partone import define_entity, create_entities

class TestFunc(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.db = Database(provider='sqlite', filename=':memory:')
        define_entity(self.db)
        self.db.generate_mapping(create_tables=True)
        create_entities(self.db)

    def tearDown(self):
        self.db.drop_all_tables(with_all_data=True)

    @db_session
    def test_create_entities(self):
        # pylint: disable=E1101
        user = self.db.User.get(username="Josh01")
        self.assertEqual(user.location, 'London')

if __name__ == '__main__':
    unittest.main()
