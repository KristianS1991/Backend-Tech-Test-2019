import unittest
import testing.postrgresql
# from partone import create_entity

class TestCase(unittest.TestCase):
    def setUp(self):
        self.postrgresql = testing.postgresql.Postgresql()

    def tearDown(self):
        self.postrgresql.stop()
