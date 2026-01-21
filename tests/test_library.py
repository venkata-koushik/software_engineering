import unittest
from src.library import Library

class TestLibrarySprint1(unittest.TestCase):

    def setUp(self):
        self.lib = Library()

    def test_add_book_success(self):
        self.lib.add_book("B1", "Python", "Guido")
        self.assertIn("B1", self.lib.books)

    def test_add_duplicate_book(self):
        self.lib.add_book("B1", "Python", "Guido")
        with self.assertRaises(ValueError):
            self.lib.add_book("B1", "Java", "James")

if __name__ == "__main__":
    unittest.main()
class TestLibrarySprint2(unittest.TestCase):

    def setUp(self):
        self.lib = Library()
        self.lib.add_book("B1", "Python", "Guido")

    def test_borrow_book(self):
        self.lib.borrow_book("B1")
        self.assertEqual(self.lib.books["B1"]["status"], "Borrowed")

    def test_borrow_unavailable_book(self):
        self.lib.borrow_book("B1")
        with self.assertRaises(ValueError):
            self.lib.borrow_book("B1")

    def test_return_book(self):
        self.lib.borrow_book("B1")
        self.lib.return_book("B1")
        self.assertEqual(self.lib.books["B1"]["status"], "Available")
class TestLibrarySprint3(unittest.TestCase):

    def setUp(self):
        self.lib = Library()
        self.lib.add_book("B1", "Python", "Guido")

    def test_report_has_header(self):
        report = self.lib.generate_report()
        self.assertIn("ID | Title | Author | Status", report)

    def test_report_has_book_entry(self):
        report = self.lib.generate_report()
        self.assertIn("B1", report)

