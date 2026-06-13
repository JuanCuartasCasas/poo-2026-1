class Stats:
    def __init__(
        self,
        hp: float = 10.0,
        attack: float = 1.0,
        defense: float = 0.5,
        special_attack: float = 1.0,
        special_defense: float = 1.0,
        speed: float = 1.0,
    ):

        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed

    def __str__(self):

        return (
            f"HP: {self.hp}, "
            f"Attack: {self.attack}, "
            f"Defense: {self.defense}, "
            f"Sp. Attack: {self.special_attack}, "
            f"Sp. Defense: {self.special_defense}, "
            f"Speed: {self.speed}"
        )
