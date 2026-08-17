import pickle
import os

from player import Player
from world_map import WorldMap
from story import Story
from exploration import Exploration


SAVE_FILE = "save_game.pkl"

def create_player():

    print("=" * 40)
    print("       CREATE YOUR CHARACTER")
    print("=" * 40)

    name = input("Enter your name: ")

    while True:

        print("\nChoose your class:")

        print("1. Warrior")
        print("2. Mage")
        print("3. Archer")
        print("4. Assassin")
        print("5. Berserker")

        try:

            choice = int(
                input("Enter your choice: ")
            )

        except ValueError:

            print(
                "Please enter a number."
            )

            continue

        if choice < 1 or choice > 5:

            print(
                "Please choose a number "
                "between 1 and 5."
            )

            continue

        if choice == 1:

            player_class = "warrior"

        elif choice == 2:

            player_class = "mage"

        elif choice == 3:

            player_class = "archer"

        elif choice == 4:

            player_class = "assassin"

        else:

            player_class = "berserker"

        break

    player = Player(name,player_class)

    return player

def save_game(player, world_map, story):

    save_data = {

        "player": player,

        "world_map": world_map,

        "story": story}

    with open(
        SAVE_FILE,
        "wb"
    ) as file:

        pickle.dump(save_data,file)

    print("\nGame saved successfully!")

def load_game():

    if not os.path.exists(SAVE_FILE):

        print("\nNo save file found.")

        return None

    try:

        with open(
            SAVE_FILE,
            "rb"
        ) as file:

            save_data = pickle.load(file)

    except (
        EOFError,
        pickle.PickleError):

        print("\nThe save file is corrupted.")

        return None

    player = save_data["player"]
    world_map = save_data["world_map"]
    story = save_data["story"]

    print(
        "\nGame loaded successfully!"
    )

    return player, world_map, story

def main_menu():

    print("\n" + "=" * 40)
    print("   HERO'S OF THE FORGOTTEN REALM")
    print("=" * 40)

    print("1. Start New Game")
    print("2. Load Game")
    print("3. Exit")

    print("=" * 40)

def game_menu(player,world_map,story):

    exploration = Exploration(player,world_map)

    while True:

        print("\n" + "=" * 40)
        print("              GAME MENU")
        print("=" * 40)

        print("1. Explore")
        print("2. World Map")
        print("3. Inventory")
        print("4. View Stats")
        print("5. Story")
        print("6. Save Game")
        print("7. Quit to Main Menu")

        print("=" * 40)

        try:
            choice = int(input("Choose an option: "))

        except ValueError:

            print("Please enter a valid number.")

            continue

        if choice == 1:
            exploration.start()

        elif choice == 2:

            world_map.show_map()

            print("\n1. Travel")
            print("2. Return")

            try:

                map_choice = int(input("Choose an option: "))

            except ValueError:

                print("Please enter a valid number.")
                continue

            if map_choice == 1:
                world_map.travel_menu()

        elif choice == 3:
            player.inventory.view_inventory()

        elif choice == 4:
            player.show_stats()

        elif choice == 5:
            story.show_current_story()

        elif choice == 6:

            save_game(
                player,
                world_map,
                story)

        elif choice == 7:

            print("\nReturning to main menu...")
            break

        else:

            print("Please choose a number "
                "between 1 and 7.")

def main():

    while True:

        main_menu()

        try:
            choice = int(input("Choose an option: "))

        except ValueError:

            print("Please enter a valid number.")

            continue

        if choice == 1:

            player = create_player()

            world_map = WorldMap(
                player)

            story = Story(
                player,
                world_map)

            story.show_intro()

            game_menu(
                player,
                world_map,
                story)

        elif choice == 2:
            loaded_data = load_game()

            if loaded_data is None:
                continue
            player, world_map, story = loaded_data
            game_menu(
                player,
                world_map,
                story)

        elif choice == 3:

            print("\nThank you for playing "
                "Eldoria RPG!")
            break
        else:
            print("Please choose 1, 2, or 3.")

if __name__ == "__main__":

    main()