from flask import Flask
from flask_testing import TestCase

class TestApp(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    
