from inventory import Inventory


class Player:

    def __init__(
        self,
        name,
        player_class,
        xp=0,
        gold=0,
        level=1
    ):

        self.name = name
        self.player_class = player_class.lower()

        self.level = level
        self.xp = xp
        self.xp_needed = 100
        self.skill_points = 0

        if self.player_class == "warrior":

            self.max_hp = 200
            self.max_mp = 40

            self.attack = 20
            self.defense = 15
            self.speed = 5

            self.crit_chance = 5
            self.crit_damage = 1.75

        elif self.player_class == "mage":

            self.max_hp = 100
            self.max_mp = 200

            self.attack = 25
            self.defense = 5
            self.speed = 8

            self.crit_chance = 10
            self.crit_damage = 2.25

        elif self.player_class == "archer":

            self.max_hp = 120
            self.max_mp = 80

            self.attack = 25
            self.defense = 10
            self.speed = 15

            self.crit_chance = 15
            self.crit_damage = 2.0

        elif self.player_class == "assassin":

            self.max_hp = 110
            self.max_mp = 100

            self.attack = 30
            self.defense = 8
            self.speed = 20

            self.crit_chance = 20
            self.crit_damage = 2.5

        elif self.player_class == "berserker":

            self.max_hp = 250
            self.max_mp = 50

            self.attack = 35
            self.defense = 12
            self.speed = 7

            self.crit_chance = 10
            self.crit_damage = 2.25

        else:

            raise ValueError("Invalid player class.")

        self.current_hp = self.max_hp
        self.current_mp = self.max_mp

        self.weapon = None
        self.armor = None
        self.accessory = None

        self.inventory = Inventory()

    def show_stats(self):

        print("\n" + "=" * 40)
        print("              PLAYER STATS")
        print("=" * 40)

        print(f"Name: {self.name}")
        print(f"Class: {self.player_class.capitalize()}")
        print(f"Level: {self.level}")

        print(
            f"XP: "
            f"{self.xp}/{self.xp_needed}")

        print(
            f"Skill Points: "
            f"{self.skill_points}")

        print("-" * 40)

        print(
            f"HP: "
            f"{self.current_hp}/{self.max_hp}")

        print(
            f"MP: "
            f"{self.current_mp}/{self.max_mp}")

        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Speed: {self.speed}")

        print(
            f"Crit Chance: "
            f"{self.crit_chance}%")

        print(
            f"Crit Damage: "
            f"{self.crit_damage}x")

        print(f"Gold: {self.gold}")

        print("-" * 40)
        if self.weapon:

            print(
                f"Weapon: "
                f"{self.weapon.name}")

        else:
            print("Weapon: None")

        if self.armor:
            print(
                f"Armor: "
                f"{self.armor.name}")

        else:
            print("Armor: None")

        if self.accessory:
            print(
                f"Accessory: "
                f"{self.accessory.name}")

        else:
            print("Accessory: None")

        print("=" * 40)

