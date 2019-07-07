from flask import Flask
from flask_testing import TestCase
from partone import define_database
from partone import create_entities

class TestApp(TestCase):
    PONY_DB_PARAMS = dict(provider='sqlite', filename='/tmp/test.db')

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.db = define_database(**self.PONY_DB_PARAMS)
        create_entities(self.db)
