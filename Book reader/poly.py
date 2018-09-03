# print("hello")

class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'hello world'

p1 = Polynomial(1, 2, 3)
p2 = Polynomial(3, 4, 5)

p1