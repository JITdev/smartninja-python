class Negyzet():
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

class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


# kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1, assists=4)

t = Teglalap(7, 9)

print(t.kerulet())

# n = Negyzet(5)
# n.a_oldal = 10
# n2 = Negyzet(7)
#
# print(n.kerulet())

