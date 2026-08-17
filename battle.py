import random

from level_up import Levelup
from loot_system import LootSystem
from skills import Skills
from items import potions, Bomb


class Battle:

    def __init__(self, player, enemy):

        self.player = player
        self.enemy = enemy

        self.defending = False
        self.battle_over = False
        self.escape = False
        self.rewards_given = False

        self.level_system = Levelup(player)
        self.loot_system = LootSystem(player)

    def start(self):

        print("\n" + "=" * 30)
        print("       BATTLE BEGINS!")
        print("=" * 30)

        print(
            f"\n{self.player.name} "
            f"vs "
            f"{self.enemy.name}")

        while not self.battle_over:

            self.show_battle_status()

            self.player_turn()

            if self.battle_over:
                break

            self.enemy_turn()

        return self.get_result()

    def show_battle_status(self):

        print("\n" + "=" * 40)

        print(
            f"{self.enemy.name} "
            f"(Level {self.enemy.level})")

        print(
            f"HP: "
            f"{self.enemy.current_hp}/"
            f"{self.enemy.max_hp}")

        print("-" * 40)

        print(
            f"{self.player.name} "
            f"(Level {self.player.level})")

        print(
            f"HP: "
            f"{self.player.current_hp}/"
            f"{self.player.max_hp}")

        print(
            f"MP: "
            f"{self.player.current_mp}/"
            f"{self.player.max_mp}")

        print("=" * 40)

    def player_turn(self):

        self.defending = False

        while True:

            print("\nChoose an action:")

            print("1. Attack")
            print("2. Skills")
            print("3. Heal")
            print("4. Use Bomb")
            print("5. Use Potion")
            print("6. Defend")
            print("7. Inventory")
            print("8. View Stats")
            print("9. Run")

            try:

                choice = int(input("Choose an option: "))

            except ValueError:

                print("Please enter a valid number.")
                continue

            if choice < 1 or choice > 9:

                print(
                    "Please choose a number "
                    "between 1 and 9.")

                continue

            if choice == 1:

                self.attack()
                break

            elif choice == 2:

                used = self.skills()

                if used:
                    break

            elif choice == 3:

                used = self.heal()

                if used:
                    break

            elif choice == 4:

                used = self.use_bomb()

                if used:
                    break

            elif choice == 5:

                used = self.use_potion()

                if used:
                    break

            elif choice == 6:

                self.defend()
                break

            elif choice == 7:

                self.inventory()

            elif choice == 8:

                self.player.show_stats()

            elif choice == 9:

                self.run()

                if self.escape:
                    break

    def check_battle_end(self):

        # Enemy defeated
        if self.enemy.current_hp <= 0:

            print(
                f"\nYou have defeated "
                f"{self.enemy.name}!")

            if not self.rewards_given:

                self.victory_rewards()

                self.rewards_given = True

            self.battle_over = True

        elif self.player.current_hp <= 0:

            self.player.current_hp = 0

            print("\nYou have been defeated!")

            self.battle_over = True

    def attack(self):

        damage = self.player.attack

        critical = random.random() < (self.player.crit_chance / 100)

        if critical:

            damage = int(damage * self.player.crit_damage)

            print("\nCRITICAL HIT!")

        self.enemy.take_damage(damage)

        print(
            f"You attacked "
            f"{self.enemy.name} "
            f"for {damage} damage!")

        self.check_battle_end()

    def enemy_turn(self):

        if self.enemy.current_hp <= 0:

            return

        if self.player.current_hp <= 0:

            return

        print(f"\n{self.enemy.name}'s turn!")

        damage = self.enemy.attack

        if self.defending:

            damage = int(damage * 0.5)

            print(
                "Your defense reduced "
                "the damage by 50%!"
            )

        self.player.current_hp -= damage

        if self.player.current_hp < 0:

            self.player.current_hp = 0

        print(
            f"{self.enemy.name} dealt "
            f"{damage} damage!")

        self.check_battle_end()

    def defend(self):

        self.defending = True

        print("\nYou are defending!")

        print(
            "Incoming damage will be "
            "reduced by 50%.")

    def run(self):

        chance = (50+ (self.player.speed - self.enemy.speed))

        chance = max(10,min(chance, 90))

        roll = random.randint(1, 100)

        if roll <= chance:

            print("\nYou successfully escaped!")

            self.battle_over = True
            self.escape = True

        else:

            print("\nYou failed to escape!")

    def get_result(self):

        if self.enemy.current_hp <= 0:

            return "victory"

        if self.player.current_hp <= 0:

            return "defeat"

        if self.escape:

            return "escaped"

        return "unknown"

    def victory_rewards(self):

        print("\n" + "=" * 40)
        print("             REWARDS")
        print("=" * 40)

        self.level_system.exp_gained(self.enemy.xp_reward)

        self.player.gold += (self.enemy.gold_reward)

        print(
            f"You received "
            f"{self.enemy.gold_reward} gold.")

        print(
            f"Total Gold: "
            f"{self.player.gold}")

        self.loot_system.give_loot(self.player.level,self.enemy)

        print("=" * 40)

    def use_potion(self):

        potions = []

        for item in self.player.inventory.items:

            if isinstance(item, potions):

                potions.append(item)

        if not potions:

            print("\nYou don't have any potions.")

            return False

        print("\nAvailable Potions:")

        for number, potion in enumerate(potions,start=1):

            print(
                f"{number}. "
                f"{potion.name}")

        try:

            choice = int(input("Choose a potion: "))

        except ValueError:

            print("Please enter a valid number.")

            return False

        if choice < 1 or choice > len(potions):

            print("Invalid choice.")

            return False

        potion = potions[choice - 1]

        potion.use(self.player)

        self.player.inventory.remove_item(potion)

        return True

    def use_bomb(self):

        bombs = []

        # Find bombs in inventory
        for item in self.player.inventory.items:

            if isinstance(item, Bomb):

                bombs.append(item)

        if not bombs:

            print("\nYou don't have any bombs.")

            return False

        print("\nAvailable Bombs:")

        for number, bomb in enumerate(bombs,start=1):

            print(
                f"{number}. "
                f"{bomb.name} "
                f"- Damage: {bomb.damage}")

        try:

            choice = int(input("Choose a bomb: "))

        except ValueError:

            print("Please enter a valid number.")

            return False

        if choice < 1 or choice > len(bombs):

            print("Invalid choice.")

            return False

        bomb = bombs[choice - 1]

        damage = bomb.use(self.enemy)

        self.enemy.take_damage(damage)

        self.player.inventory.remove_item(bomb)

        self.check_battle_end()

        return True

    def heal(self):

        heal_amount = 40
        mp_cost = 15

        if self.player.current_mp < mp_cost:

            print("Not enough MP.")

            return False

        if (self.player.current_hp == self.player.max_hp):

            print("\nYour HP is already full.")

            return False

        self.player.current_mp -= mp_cost

        self.player.current_hp += heal_amount

        if (self.player.current_hp > self.player.max_hp):

            self.player.current_hp = (self.player.max_hp)

        print(f"\nYou restored "
            f"{heal_amount} HP.")

        print(f"You used "f"{mp_cost} MP.")

        return True

    def skills(self):

        player_class = (self.player.player_class.lower())

        if player_class not in Skills:

            print("\nYou don't have any skills.")

            return False

        player_skills = Skills[player_class]

        print("\nAvailable Skills:")

        for number, skill in enumerate(player_skills.values(),start=1):

            print(
                f"{number}. "
                f"{skill['name']} "
                f"- Damage: {skill['damage']} "
                f"- MP: {skill['mp_cost']}")

        try:

            choice = int(input("Choose a skill: "))

        except ValueError:

            print("Please enter a valid number.")

            return False

        if (choice < 1 or choice > len(player_skills)):

            print("Invalid choice.")

            return False

        skill_list = list(player_skills.values())

        skill = skill_list[
            choice - 1]

        if (self.player.current_mp
            < skill["mp_cost"]):

            print("\nNot enough MP.")

            return False

        self.player.current_mp -= (
            skill["mp_cost"])

        damage = skill["damage"]

        self.enemy.take_damage(
            damage)

        print(
            f"\nYou used "
            f"{skill['name']} "
            f"and dealt "
            f"{damage} damage!")

        self.check_battle_end()

        return True

    def inventory(self):

        print("\n" + "=" * 30)
        print("          INVENTORY")
        print("=" * 30)

        self.player.inventory.view_inventory()

        print("\nYou can use items from the battle menu.")