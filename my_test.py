import unittest


from palindromos import palindromo


class MyTest(unittest.TestCase):

    def test_uno(self):
        self.assertEqual(palindromo("neuquen"), True)

    def test_dos(self):
        self.assertEqual(palindromo("racecar"), True)

    def test_tres(self):
        self.assertEqual(palindromo("anita lava la tina"), True)

    def test_cuatro(self):
        self.assertEqual(palindromo("se es o no se es"), True)

    def test_cinco(self):
        self.assertEqual(palindromo("somos o no somos"), True)


if __name__ == '__main__':
    unittest.main()