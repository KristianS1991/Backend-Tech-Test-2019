import unittest
import testing.postgresql
from partone import create_entity

# store data that currently exists in the real database for comparison purposes in test
prev_data = testing.postgresql.Postgresql(copy_data_from='postgres://localhost:5432/user-database')

class TestCase(unittest.TestCase):
    def setUp(self):
        self.postgresql = testing.postgresql.Postgresql()

    def test_create_entity(self):
        # I need to re-write create_entity func to take the database of interest as an argument
        create_entity()

    def tearDown(self):
        self.postgresql.stop()
