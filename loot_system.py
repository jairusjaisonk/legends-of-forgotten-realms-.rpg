import random

from items import (
    potions,
    bombs,
    weapons,
    armor,
    accessories,
    Potion,
    Bomb,
    Weapon,
    Armor,
    Accessory
)


class LootSystem:

    def __init__(self, player):

        self.player = player

    # ==========================================
    # CHOOSE RARITY
    # ==========================================

    def get_rarity(self, level):

        if level <= 10:

            rarities = ["common", "uncommon"]

        elif level <= 30:

            rarities = ["uncommon", "rare"]

        elif level <= 50:

            rarities = ["rare", "super rare"]

        elif level <= 70:

            rarities = ["super rare", "epic"]

        elif level <= 90:

            rarities = ["epic", "mythical"]

        else:

            rarities = ["mythical", "legendary"]

        # 70% chance of the lower rarity
        # 30% chance of the higher rarity

        roll = random.randint(1, 100)

        if roll <= 70:

            return rarities[0]

        return rarities[1]

    # ==========================================
    # CHOOSE ITEM TYPE
    # ==========================================

    def get_item_type(self):

        roll = random.randint(1, 100)

        if roll <= 25:

            return "potion"

        elif roll <= 40:

            return "bomb"

        elif roll <= 60:

            return "weapon"

        elif roll <= 75:

            return "armor"

        else:

            return "accessory"

    # ==========================================
    # GET RANDOM ITEM
    # ==========================================

    def get_random_item(self, level):

        rarity = self.get_rarity(level)

        item_type = self.get_item_type()

        if item_type == "potion":

            return self.get_item(
                potions,
                Potion,
                rarity
            )

        elif item_type == "bomb":

            return self.get_item(
                bombs,
                Bomb,
                rarity
            )

        elif item_type == "weapon":

            return self.get_item(
                weapons,
                Weapon,
                rarity
            )

        elif item_type == "armor":

            return self.get_item(
                armor,
                Armor,
                rarity
            )

        elif item_type == "accessory":

            return self.get_item(
                accessories,
                Accessory,
                rarity
            )

        return None

    # ==========================================
    # FIND ITEM WITH THE CORRECT RARITY
    # ==========================================

    def get_item(
        self,
        item_dictionary,
        item_class,
        rarity
    ):

        possible_items = []

        for item in item_dictionary.values():

            if item["rarity"].lower() == rarity:

                possible_items.append(item)

        if not possible_items:

            return None

        item_data = random.choice(possible_items)

        return self.create_item(
            item_data,
            item_class
        )

    # ==========================================
    # CREATE ITEM OBJECT
    # ==========================================

    def create_item(self, data, item_class):

        if item_class == Potion:

            return Potion(
                data["name"],
                data["rarity"],
                data["price"],
                data["effect"],
                data["amount"]
            )

        elif item_class == Bomb:

            return Bomb(
                data["name"],
                data["rarity"],
                data["price"],
                data["damage"],
                data["element"]
            )

        elif item_class == Weapon:

            return Weapon(
                data["name"],
                data["rarity"],
                data["price"],
                data["damage"],
                data["crit_chance"],
                data["crit_damage"]
            )

        elif item_class == Armor:

            return Armor(
                data["name"],
                data["rarity"],
                data["price"],
                data["defense"]
            )

        elif item_class == Accessory:

            return Accessory(
                data["name"],
                data["rarity"],
                data["price"],
                data.get("attack_bonus", 0),
                data.get("defense_bonus", 0),
                data.get("speed_bonus", 0),
                data.get("crit_chance_bonus", 0),
                data.get("crit_damage_bonus", 0),
                data.get("hp_bonus", 0),
                data.get("mp_bonus", 0)
            )

        return None

    # ==========================================
    # NORMAL ENEMY LOOT
    # ==========================================

    def normal_loot(self, level):

        item = self.get_random_item(level)

        if item is None:

            print("No suitable loot was found.")

            return

        self.player.inventory.add_item(item)

        print(
            f"Loot obtained: "
            f"{item.name} [{item.rarity}]"
        )

    # ==========================================
    # ELITE ENEMY LOOT
    # ==========================================

    def elite_loot(self, level):

        print("\nElite enemy defeated!")

        number_of_items = random.randint(1, 2)

        for i in range(number_of_items):

            item = self.get_random_item(level)

            if item is None:

                continue

            self.player.inventory.add_item(item)

            print(
                f"Elite Loot: "
                f"{item.name} [{item.rarity}]"
            )

    # ==========================================
    # BOSS LOOT
    # ==========================================

    def boss_loot(self, level):

        print("\n" + "=" * 40)
        print("              BOSS LOOT")
        print("=" * 40)

        # Boss gets guaranteed equipment

        boss_item = self.get_boss_item(level)

        if boss_item is not None:

            self.player.inventory.add_item(
                boss_item
            )

            print(
                f"Boss Reward: "
                f"{boss_item.name} "
                f"[{boss_item.rarity}]"
            )

        # Additional loot

        extra_items = random.randint(1, 3)

        for i in range(extra_items):

            item = self.get_random_item(level)

            if item is None:

                continue

            self.player.inventory.add_item(item)

            print(
                f"Boss Loot: "
                f"{item.name} "
                f"[{item.rarity}]"
            )

        print("=" * 40)

    # ==========================================
    # BOSS EQUIPMENT
    # ==========================================

    def get_boss_item(self, level):

        if level <= 10:

            rarity = "rare"

        elif level <= 30:

            rarity = "super rare"

        elif level <= 50:

            rarity = "epic"

        elif level <= 70:

            rarity = "epic"

        elif level <= 90:

            rarity = "mythical"

        else:

            rarity = "legendary"

        # Boss can drop equipment only

        item_type = random.choice([
            "weapon",
            "armor",
            "accessory"
        ])

        if item_type == "weapon":

            return self.get_item(
                weapons,
                Weapon,
                rarity
            )

        elif item_type == "armor":

            return self.get_item(
                armor,
                Armor,
                rarity
            )

        elif item_type == "accessory":

            return self.get_item(
                accessories,
                Accessory,
                rarity
            )

        return None

    # ==========================================
    # GIVE LOOT
    # ==========================================

    def give_loot(self, level, enemy):

        if enemy.is_boss:

            self.boss_loot(level)

        elif enemy.level >= level + 3:

            self.elite_loot(level)

        else:

            self.normal_loot(level)