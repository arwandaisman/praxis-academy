class Complex:
    def __init__(slef, realpart, imagpart):
        slef.r = realpart
        slef.i = imagpart
x = Complex(3.0, -4.5)
x.r, x.i

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter