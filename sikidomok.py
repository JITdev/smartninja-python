class Negyzet():
    x = []

    def __init__(self, a_oldal:int):
       self.a_oldal = a_oldal

    def kerulet(self):
        return self.a_oldal * 4


class Teglalap(Negyzet):
    def __init__(self, a_oldal: int, b_oldal: int):
        super().__init__(a_oldal=a_oldal)
        self.b_oldal = b_oldal


    def kerulet(self):
        return 2 * (self.a_oldal + self.b_oldal)

n = Negyzet(5)
n_2 = Negyzet(7)
t = Teglalap(7, 9)
t_2 = Teglalap(4, 8)

print(t.x)
Teglalap.x = 3
print(t.x)
