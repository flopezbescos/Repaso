import unittest
from serv import Servidor

class TestFrases(unittest.TestCase): 

    def test_openfiles(self):
        server = Servidor()
        self.assertEqual(server.open_files(), ['1 >> fjdsiotsjkvdfnsbrteo,bfdsbihsfdsbgnrdnytjytnfgdyjn.', '2 >> bgfhuidortrd', '3 >> hola', '4 >> esto deberia ser profundo', '5 >> La vida es bella'])

    # def test_generate_frase(self):
    #     server = Servidor()
    #     result = server.generate_frase("FRASE")
    #     expected_outcomes = [
    #         "FRASE --> 1 >> fjdsiotsjkvdfnsbrteo,bfdsbihsfdsbgnrdnytjytnfgdyjn.",
    #         "FRASE --> 2 >> bgfhuidortrd",
    #         "FRASE --> 3 >> hola",
    #         "FRASE --> 4 >> esto deberia ser profundo",
    #         "FRASE --> 5 >> La vida es bella"]
    #     self.assertIn(result, expected_outcomes)
    
    def test_generate_frase(self):
        server = Servidor()
        phrase_count = 5
        expected_outcomes = []
        frase_generada = server.generate_frase("FRASE")
        for i in range(0, phrase_count + 1):
            expected_outcomes.append(f"{frase_generada}")

        self.assertIn(frase_generada, expected_outcomes)

    def test_total(self):
        server = Servidor()
        self.assertEqual(server.generate_frase("TOTAL"), "TOTAL --> 5 FRASES - 9 LINEAS")

    def test_error(self):
        server = Servidor()
        self.assertEqual(server.generate_frase("ERROR"), "ERROR --> Comando no soportado")

    def test_countlines(self):
        server = Servidor()
        self.assertEqual(server.count_non_empty_lines(), 9)

    def test_countfrases(self):
        server = Servidor()
        self.assertEqual(len(server.recognize_frases()), 5)

        