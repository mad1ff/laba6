class Trapezoid:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def area(self):
        return (self.a + self.b) / 2 * self.h

    def perimeter(self):
        return self.a + self.b + 2 * self.h

    def info(self):
        return f"Трапеция: a={self.a}, b={self.b}, h={self.h}"