import unittest
import streamlit as st
from view.CrearActa import *
from controller.EvalController import EvaluadorController
from view.ImprimirActa import *

class TestFunciones(unittest.TestCase):
    def test_convertir(self):
        self.assertEqual(convertir(4.6), 'Cuatro punto seis')
    def test_search(self):
        d = {6: 4, 1: 0, 2: 3}
        self.assertEqual(search(1, d), 1)
    def test_sinLetras(self):
        self.assertEqual(id_sinLetras('1a2344d 2'), True)
if __name__ == "__main__":
    unittest.main()
