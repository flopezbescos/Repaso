import unittest
from servidor import Servidor


class TestFrases(unittest.TestCase):

    def test_frasepalindroma(self):
        server = Servidor()
        self.assertEqual(server.es_palindroma("Somos"), True)

    def test_frasepalindroma2(self):
        server = Servidor()
        self.assertEqual(server.es_palindroma("Dabale arroz a la zorra el abad"), True)

    def test_fraseNopalindroma2(self):
        server = Servidor()
        self.assertEqual(server.es_palindroma("Dabale arroz a la zorra el abaz"), False)
    def test_checkok(self):
        server = Servidor()
        self.assertEqual(server.check("Ana lava lana"), "Es palindroma")

    def test_checkfallo(self):
        server = Servidor()
        self.assertEqual(server.check("El coche es rojo"), "No es palindroma")


if __name__ == '__main__':
    unittest.main()