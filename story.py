class Story:

    def __init__(self, player, world_map):

        self.player = player
        self.world_map = world_map

        self.current_chapter = 1

        self.defeated_bosses = []

    def show_intro(self):

        print("\n" + "=" * 50)
        print("              THE FALL OF ELDORIA")
        print("=" * 50)

        print("\nThe kingdom of Eldoria has fallen into darkness.")
        print("Monsters have appeared throughout the kingdom.")
        print("Powerful bosses guard every region.")

        print("\nYour mission is simple:")

        print("Grow stronger.")
        print("Defeat the guardians.")
        print("Reach Level 100.")
        print("Destroy Lucifero, the Ancient Demon King.")

        print("=" * 50)

    def show_current_story(self):

        print("\n" + "=" * 40)
        print("             STORY")
        print("=" * 40)

        print(f"Chapter: {self.current_chapter}")

        print(f"Current Level: {self.player.level}")

        print(
            f"Current Location: "
            f"{self.world_map.locations[self.world_map.current_location]['name']}")

        print("=" * 40)

    def boss_defeated(self, boss_name):

        if boss_name in self.defeated_bosses:
            return

        self.defeated_bosses.append(boss_name)

        print( "==" * 10)
        print(f"      {boss_name} DEFEATED!")
        print("==" * 10)

        self.progress_story(boss_name)

    def progress_story(self, boss_name):

        if boss_name == "Pesqure":

            self.current_chapter = 2

            print("\nThe first guardian has fallen.")
            print("A new path has opened deeper into Eldoria.")

            self.world_map.unlock_location("leonardo_dungeon")

        elif boss_name == "Gaunter":

            self.current_chapter = 3

            print("\nGaunter has been defeated.")
            print("The path toward the Royal Capital is now open.")

            self.world_map.unlock_location("royal_capital")

        elif boss_name == "Arthur":

            self.current_chapter = 4

            print("\nArthur has been defeated.")

            print("\nArthur refuses to reveal the truth behind his power.")

            self.arthur_interrogation()

        elif boss_name == "Cursed King":

            self.current_chapter = 5

            print("\nThe Cursed King has fallen.")

            print("The path toward the Volcano has been opened.")

            self.world_map.unlock_location("volcano")

        elif boss_name == "Fire Dragon":

            self.current_chapter = 6

            print("\nThe Fire Dragon has been defeated.")

            print("A frozen lands beyond the mountains are now visible.")

            self.world_map.unlock_location("frozen_mountain")

        elif boss_name == "Ice Dragon":

            self.current_chapter = 7

            print("\nThe Ice Dragon has been defeated.")

            print("The ancient Sky Temple can now be reached.")

            self.world_map.unlock_location("sky_temple")

        elif boss_name == "Wind Dragon":

            self.current_chapter = 8

            print("\nThe Wind Dragon has been defeated.")

            print("A dark force is waiting beyond the Sky Temple.")

            self.world_map.unlock_location("abyss")

        elif boss_name == "Corrupted Golden Dragon":

            self.current_chapter = 9

            print("\nThe Corrupted Golden Dragon has fallen.")

            print("The gates to the Demon Realm have opened.")

            self.world_map.unlock_location("demon_realm")

        elif boss_name == "Demon General":

            self.current_chapter = 10

            print("\nThe Demon General has been defeated.")

            print("The final path toward Lucifero has been revealed.")

            self.world_map.unlock_location("inner_demon_realm")

        elif boss_name == "Lucifero":

            self.current_chapter = 11

            self.final_battle()

    def arthur_interrogation(self):

        print("\n" + "=" * 50)
        print("   ARTHUR'S SECRET")
        print("=" * 50)

        print("\nArthur has been defeated.")
        print("But something is wrong.")

        print("\nYou demand to know where "
            "Arthur received his power.")

        print("\nArthur remains silent.")

        print("\nAfter intense interrogation, "
            "Arthur finally reveals the truth.")

        print("\nHis power came from an ancient "
            "force hidden within the Ancient Ruins.")

        print("\nThe Ancient Ruins are now accessible.")

        self.world_map.unlock_location("ancient_ruins")

    def final_battle(self):

        print("\n" + "=" * 60)
        print("             THE FINAL BATTLE")
        print("=" * 60)

        print("\nYou have reached the end of your journey.")

        print("Lucifero, the Ancient Demon King, "
            "stands before you.")

        print("\nThe fate of Eldoria rests in your hands.")

        print("=" * 60)

    def check_story_progress(self):

        if self.player.level >= 100:

            print("\nYou have reached Level 100.")
            print("The final battle awaits.")