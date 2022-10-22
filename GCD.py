class GCD:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.Results = {}

    def calc(self):
        a = self.a
        b = self.b
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        self.Results[(self.a, self.b)] = a + b
        return a + b