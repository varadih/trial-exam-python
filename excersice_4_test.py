import unittest
import excercise_4

class TestingGreeter(unittest.TestCase):

    def test_greeter(self):
        self.assertEqual(excercise_4.greeter('Mammut'),('Hello, Mammut!'))

    def test_greeter_empty(self):
        self.assertEqual(excercise_4.greeter(''),('Hello, Mr Nobody!'))

if __name__ == '__main__':
    unittest.main()
