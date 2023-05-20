import unittest
from serv import Servidor

class TestFrases(unittest.TestCase):

    def test_frasepalindroma(self):
        server = Servidor()
        self.assertEqual(server.palindrome("Somos"), True)

    def test_frasepalindroma2(self):
        server = Servidor()
        self.assertEqual(server.palindrome("Dabale arroz a la zorra el abad"), True)

    def test_checkok(self):
        server = Servidor()
        self.assertEqual(server.check("Ana lava lana"), "Es palindroma")

    def test_checkfallo(self):
        server = Servidor()
        self.assertEqual(server.check("El coche es rojo"), "No es palindroma")


    # python3 -m unittest test.py

    

    
