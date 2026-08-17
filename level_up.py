class Levelup:

    def __init__(self, player):

        self.player = player

    def exp_gained(self, amount):

        self.player.xp += amount

        print(f"You gained {amount} XP.")
        print(f"XP: {self.player.xp}/{self.player.xp_needed}")

        while self.player.xp >= self.player.xp_needed:

            if self.player.level >= 100:

                self.player.xp = 0

                print("You have reached the maximum level!")

                return

    def level_up(self):
        if self.player.level >= 100:

            print("You have reached the maximum level!")

            return
        
        self.player.xp -= self.player.xp_needed

        self.player.level += 1

        self.player.xp_needed += 50

        self.player.skill_points += 1

        print("==" * 20)
        print("     LEVEL UP!")
        print("==" * 20)

        print(f"You are now Level {self.player.level}!")
        print("You received 1 Skill Point.")

        self.increase_stats()

    def increase_stats(self):

        self.player.max_hp += 100
        self.player.max_mp += 50
        self.player.attack += 10
        self.player.defense += 6
        self.player.speed += 3

        self.player.current_hp = self.player.max_hp
        self.player.current_mp = self.player.max_mp