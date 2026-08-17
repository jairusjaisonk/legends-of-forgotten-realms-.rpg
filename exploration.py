import random

from enemy import Enemy, enemies
from battle import Battle


class Exploration:

    def __init__(self, player, world_map):

        self.player = player
        self.world_map = world_map

    def start(self):

        while True:

            # If player has been defeated, stop exploration
            if self.player.current_hp <= 0:

                print("\nYou cannot continue exploring.")
                break

            print("\n" + "=" * 40)
            print("              EXPLORATION")
            print("=" * 40)

            print(
                f"Location: "
                f"{self.world_map.current_location}"
            )

            print(
                f"Level: "
                f"{self.player.level}"
            )

            print(
                f"HP: "
                f"{self.player.current_hp}/"
                f"{self.player.max_hp}"
            )

            print("\n1. Explore Area")
            print("2. View World Map")
            print("3. Return to Game Menu")

            print("=" * 40)

            try:

                choice = int(
                    input("Choose an option: ")
                )

            except ValueError:

                print("Please enter a valid number.")
                continue

            if choice == 1:

                self.explore_area()

            elif choice == 2:

                self.world_map.show_map()

            elif choice == 3:

                print("\nReturning to game menu...")
                break

            else:

                print("Please choose between 1 and 3.")

    def explore_area(self):

        if self.player.current_hp <= 0:

            print("\nYou cannot explore because you have been defeated.")
            return

        print("\n" + "=" * 40)
        print("           EXPLORING AREA")
        print("=" * 40)

        print(
            f"\nYou begin exploring "
            f"{self.world_map.current_location}..."
        )

        available_enemies = self.get_available_enemies()

        # If there are no enemies in this region
        if not available_enemies:

            print(
                "\nThere are no suitable enemies "
                "available in this area."
            )

            return

        event = random.randint(1, 100)

        if event <= 70:

            # 70% enemy encounter
            self.enemy_encounter(
                available_enemies
            )

        elif event <= 90:

            # 20% treasure
            self.find_gold()

        else:

            # 10% nothing
            print(
                "\nYou explored the area "
                "but found nothing."
            )

    def get_available_enemies(self):

        available_enemies = []

        current_location = (
            self.world_map.current_location
        )

        for enemy_data in enemies.values():

            # Enemy must belong to current region
            if enemy_data["region"] != current_location:

                continue

            enemy_level = enemy_data["level"]

            player_level = self.player.level

            if enemy_level <= player_level + 5:

                available_enemies.append(enemy_data)

        return available_enemies

    def enemy_encounter(self, available_enemies):

        enemy_data = random.choice(
            available_enemies
        )

        print("\n" + "=" * 40)
        print("          ENEMY ENCOUNTER!")
        print("=" * 40)

        print(
            f"\nA {enemy_data['name']} appeared!"
        )

        print(
            f"Enemy Level: "
            f"{enemy_data['level']}"
        )

        print(
            f"HP: "
            f"{enemy_data['max_hp']}"
        )

        print("=" * 40)

        enemy = self.create_enemy(enemy_data)

        battle = Battle(
            self.player,
            enemy)

        result = battle.start()

        self.handle_battle_result(
            result)

    def create_enemy(self, data):

        enemy = Enemy(

            name=data["name"],

            level=data["level"],

            max_hp=data["max_hp"],

            attack=data["attack"],

            defense=data["defense"],

            speed=data["speed"],

            weaknesses=data.get(
                "weaknesses",
                []
            ),

            abilities=data.get(
                "abilities",
                []
            ),

            xp_reward=data.get(
                "xp",
                0
            ),

            gold_reward=data.get(
                "gold",
                0
            ),

            is_boss=data.get(
                "is_boss",
                False
            )
        )

        return enemy

    def handle_battle_result(self, result):

        print("\n" + "=" * 40)
        print("           BATTLE RESULT")
        print("=" * 40)

        if result == "victory":

            print("\nYou won the battle!")

            print(
                f"You can continue exploring "
                f"{self.world_map.current_location}."
            )

        elif result == "defeat":

            print("\nYou were defeated.")

            print(
                "Your adventure has ended."
            )

        elif result == "escaped":

            print(
                "\nYou escaped from the enemy."
            )

        else:

            print(
                "\nThe battle ended unexpectedly."
            )

        print("=" * 40)

    def find_gold(self):

        minimum_gold = 10

        maximum_gold = 50 + (
            self.player.level * 5
        )

        amount = random.randint(
            minimum_gold,
            maximum_gold
        )

        self.player.gold += amount

        print("\n" + "=" * 40)
        print("             TREASURE!")
        print("=" * 40)

        print(
            f"\nYou found {amount} gold!"
        )

        print(
            f"Current Gold: "
            f"{self.player.gold}"
        )

        print("=" * 40)