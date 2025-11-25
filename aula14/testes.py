'''''
import unittest
from aula14 import SobrenomeNaOrdem

class NomeTest(unittest.TestCase):
    def TestSobrenomeNaOrdem(self):
        NomeCompleto = SobrenomeNaOrdem('Joao', 'Madureira', 'Silva')
        self.assertEqual(NomeCompleto, 'Joao Silva Madureira')
'''''
# # unittest.main(argv=[''], exit = False)

# # assertNotEqual(a, b)              a != b
# # assertEqual(a, b)                 a == b
# # assertTrue(x)                     x é verdadeiro
# # assertFalse(y)                    y é falso
# # assertIn(item, lista)             item está na lista
# # assertNotIn(item, lista)          item não está na lista

