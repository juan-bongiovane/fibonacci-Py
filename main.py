import unittest  #import de la libreria de testeo
from fibo import fibonacci  #import función fibonacci


class TestFibonacci(unittest.TestCase):
    def __init__(self, methodName, param1=None, param2=None):
        super(TestFibonacci, self).__init__(methodName)

        self.param1 = param1
        self.param2 = param2


    def test_fibonacci(self):
        resultado = fibonacci(self.param1)
        self.assertAlmostEqual(resultado, self.param2)

if __name__ == "__main__":
    test_cases = unittest.TestSuite()
    test_cases.addTest(TestFibonacci('test_fibonacci', 5, 3))
    test_cases.addTest(TestFibonacci('test_fibonacci', 5, 0))
    test_cases.addTest(TestFibonacci('test_fibonacci', 2, 1))
    unittest.TextTestRunner().run(test_cases)
