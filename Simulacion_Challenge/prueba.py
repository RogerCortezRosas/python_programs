import unittest
import checkpoint as ch

class test(unittest.TestCase):
    def test_factorial(self):
        valor = 24
        obj = ch.Factorial(4)
       # self.assertEqual(valor,obj)
       #assert valor == obj ,'Prueba factorial fallida'

        if(valor != obj):
            raise ValueError(f'Error prueba factorial, {valor} es diferente que {obj}')


    def test_primo(self):
        primo = True
        obj = ch.EsPrimo(7)
        self.assertEqual(primo,obj)

    def test_Animal(self):
        a = ch.ClaseAnimal('gato','blanco')
        valor_test = a.CumplirAnios()
        valor_esperado = 1
        self.assertEqual(valor_test,valor_esperado)

    def test_Animal_2(self):
        b = ch.ClaseAnimal('perro','cafe')
        for i in range(0,100):
            valor_test = b.CumplirAnios()
        self.assertEqual(110,valor_test)
