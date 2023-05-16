import unittest
from serv import Servidor

class TestFrases(unittest.TestCase):

    def test_randomfrase(self):
        server = Servidor()
        self.assertEqual(server.palindrome("ana"), True)

    def test_randomfrase2(self):
        server = Servidor()
        self.assertEqual(server.palindrome("anita lava la tina"), True)

    def test_checkok(self):
        server = Servidor()
        self.assertEqual(server.check("anita lava la tina"), "It's a palindrome")

    def test_checkfail(self):
        server = Servidor()
        self.assertEqual(server.check("Más sabe el diablo por viejo que por diablo"), "It's not a palindrome")


    # python3 -m unittest test.py

    

    
