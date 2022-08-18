class P:
    def __init__(self) -> None:
        self.a = 7


class C(P):
    b = 10


c = C()  # Instance of child class


print(c.a, c.b)


class Roster:
    def __init__(self, player, number, position) -> None:
        self.player = player
        self.number = number
        self.position = position


class Varsity(Roster):
    def __init__(self, player, number, position, tired) -> None:
        super().__init__(player, number, position)
        self.tired = tired
        return print(self.player + " " + str(self.number)+", " + self.position + " is " + self.tired)


class Substitutes(Roster):
    def __init__(self, player, number, position) -> None:
        super().__init__(player, number, position)
        self.ready = "yes"

    def status(self):
        if self.ready == "yes":
            return self.position + " " + str(self.number) + " " + self.player + ", Is ready to sub"
        else:
            return self.position + " " + str(self.number) + " " + self.player + ", Is not ready to sub"


tom = Varsity("Tom", 5, "Defender", "Tired")
gus = Varsity("Gus", 7, "Attacker", "Not Tired")

alan = Substitutes("Alan", 22, "Defender")
luis = Substitutes("Luis", 55, "Attacker")

print(alan.status())
print(luis.status())
