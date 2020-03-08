class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()


class Complex:
    def __init__(slef, realpart, imagpart):
        slef.r = realpart
        slef.i = imagpart
x = Complex(3.0, -4.5)
x.r, x.i