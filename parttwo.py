from flask import Flask
from flask_testing import TestCase
from pony.orm import Database
from partone import define_entity, create_entities

class TestApp(TestCase):
    PONY_DB_PARAMS = dict(provider='sqlite', filename='/tmp/test.db')

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.db = Database('sqlite', '/tmp/test.db')
        define_entity(self.db)
        self.db.generate_mapping(create_tables=True)
        create_entities(self.db)

    def tearDown(self):
        db.drop_all_tables(with_all_data=True)
