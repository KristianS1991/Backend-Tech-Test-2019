from flask import Flask
from flask_testing import TestCase
from pony.orm import Database, db_session
from partone import define_entity, create_entities

class TestApp(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.db = Database('sqlite', 'sqlite://tmp/test.db', create_db=True)
        define_entity(self.db)
        self.db.generate_mapping(create_tables=True)
        create_entities(self.db)

    def tearDown(self):
        db.drop_all_tables(with_all_data=True)

    @db_session
    def test_create_entities(self):
        #logic to test function - get something from database and compare w/ known values
        #self.assertEqual(value from db, known value)
