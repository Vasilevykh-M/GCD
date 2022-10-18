class GCD:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.Results = {}

    def calc(self):
        A = self.A
        B = self.B
        while self.A != self.B:

            if self.A > self.B:
                self.A -= self.B
            else:
                self.B -= self.A
        self.Results[(A, B)] = self.A
        return self.A