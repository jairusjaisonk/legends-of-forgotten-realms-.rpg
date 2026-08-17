from items import Weapon, Armor, Accessory


class Inventory:

    def __init__(self):

        self.items = []

    def add_item(self, item):

        self.items.append(item)

        print(
            f"{item.name} was added "
            f"to your inventory."
        )

    def view_inventory(self):

        if not self.items:

            print("\nYour inventory is empty.")
            return

        print("\n" + "=" * 40)
        print("              INVENTORY")
        print("=" * 40)

        for number, item in enumerate(
            self.items,
            start=1
        ):

            print(
                f"{number}. "
                f"{item.name} "
                f"[{item.rarity}]"
            )

        print("=" * 40)

    def get_item(self, number):

        if number < 1 or number > len(self.items):

            print("Invalid item number.")

            return None

        return self.items[number - 1]

    def remove_item(self, item):

        if item in self.items:

            self.items.remove(item)

            return True

        return False

    def use_item(self, number, player):

        item = self.get_item(number)

        if item is None:
            return

        # Check whether the item actually has a use()
        # method before trying to use it.
        if not hasattr(item, "use"):

            print(
                "This item cannot be used."
            )

            return

        item.use(player)

        self.remove_item(item)

    def equip_item(self, number, player):

        item = self.get_item(number)

        if item is None:
            return

        if isinstance(item, Weapon):

            # Unequip old weapon first
            if player.weapon is not None:

                print(
                    f"{player.weapon.name} "
                    f"was unequipped."
                )

            player.weapon = item

            print(
                f"{item.name} equipped."
            )

        elif isinstance(item, Armor):

            if player.armor is not None:

                print(
                    f"{player.armor.name} "
                    f"was unequipped."
                )

            player.armor = item

            print(
                f"{item.name} equipped."
            )

        elif isinstance(item, Accessory):

            if player.accessory is not None:

                print(
                    f"{player.accessory.name} "
                    f"was unequipped."
                )

            player.accessory = item

            print(
                f"{item.name} equipped."
            )

        else:

            print(
                "This item cannot be equipped."
            )

    def unequip_weapon(self, player):

        if player.weapon is None:

            print(
                "No weapon is equipped."
            )

            return

        print(
            f"{player.weapon.name} "
            f"unequipped."
        )

        player.weapon = None

    def unequip_armor(self, player):

        if player.armor is None:

            print(
                "No armor is equipped."
            )

            return

        print(
            f"{player.armor.name} "
            f"unequipped."
        )

        player.armor = None

    def unequip_accessory(self, player):

        if player.accessory is None:

            print(
                "No accessory is equipped."
            )

            return

        print(
            f"{player.accessory.name} "
            f"unequipped."
        )

        player.accessory = None

    def drop_item(self, number):

        item = self.get_item(number)

        if item is None:
            return

        self.items.remove(item)

        print(
            f"{item.name} was dropped."
        )

    def sell_item(self, number, player):

        item = self.get_item(number)

        if item is None:
            return

        sell_price = int(item.price * 0.5)

        player.gold += sell_price

        self.items.remove(item)

        print(
            f"You sold {item.name} "
            f"for {sell_price} gold."
        )