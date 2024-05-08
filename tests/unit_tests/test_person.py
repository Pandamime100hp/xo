import unittest

from src import XOSymbol
from src import Person


class TestPerson(unittest.TestCase):
    person: Person

    def setUp(self):
        """_summary_
        """
        pass

    def tearDown(self):
        """_summary_
        """
        pass

    def test_person_x(self):
        """_summary_
        """
        self.person = Person(symbol=XOSymbol.X, nickname="")
        self.assertEqual(XOSymbol.X, self.person.symbol)

    def test_person_o(self):
        """_summary_
        """
        self.person = Person(symbol=XOSymbol.O, nickname="")
        self.assertEqual(XOSymbol.O, self.person.symbol)

    def test_increment_person_score(self):
        """_summary_
        """
        self.person = Person(symbol=XOSymbol.O, nickname="")
        self.person.increment_score()
        self.assertEqual(1, self.person.score)
