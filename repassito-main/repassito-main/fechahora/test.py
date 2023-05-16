import unittest
from serv import *
from cli import *

class TestFrases(unittest.TestCase):

    def test_message_low(self):
        server= Servidor()
        self.assertEqual(server.message_to_lower("ANA"), "ana")

    

    

        
