import unittest

from src import XOSymbol
from src import Person


class TestPerson(unittest.TestCase):
    person: Person

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_person_x(self):
        self.person = Person(symbol=XOSymbol.X, nickname="")
        self.assertEqual(XOSymbol.X, self.person.symbol)

    def test_person_o(self):
        self.person = Person(symbol=XOSymbol.O, nickname="")
        self.assertEqual(XOSymbol.O, self.person.symbol)

    def test_increment_person_score(self):
        self.person = Person(symbol=XOSymbol.O, nickname="")
        self.person.increment_score()
        self.assertEqual(1, self.person.score)
