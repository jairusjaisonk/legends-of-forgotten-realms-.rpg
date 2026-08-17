import random

class Enemy:

    def __init__(
        self,
        name,
        level,
        max_hp,
        attack,
        defense,
        speed,
        weaknesses=None,
        abilities=None,
        xp_reward=0,
        gold_reward=0,
        is_boss=False
    ):

        self.name = name
        self.level = level

        self.max_hp = max_hp
        self.current_hp = max_hp

        self.attack = attack
        self.defense = defense
        self.speed = speed

        # Enemy characteristics
        self.weaknesses = weaknesses or []
        self.abilities = abilities or []

        # Rewards
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward

        # Boss information
        self.is_boss = is_boss

        # Used for abilities that depend on turns
        self.turn_count = 0

    def attack_player(self, player):

        damage = self.calculate_damage()

        player.current_hp -= damage

        if player.current_hp < 0:
            player.current_hp = 0

        print(
            f"{self.name} attacked "
            f"{player.name} for {damage} damage.")

    def take_damage(self, damage):

        damage -= self.defense

        if damage < 1:
            damage = 1

        self.current_hp -= damage

        if self.current_hp < 0:
            self.current_hp = 0

        print(
            f"{self.name} took "
            f"{damage} damage."
        )

    def calculate_damage(self):

        return self.attack

    def is_defeated(self):

        return self.current_hp <= 0
enemies = {

    "goblin": {
        "name": "Goblin",
        "region": "Forest",
        "level": 1,

        "max_hp": 120,
        "attack": 15,
        "defense": 8,
        "speed": 10,

        "weaknesses": ["blunt", "fire", "ice"],

        "abilities": [
            "slash",
            "bleed",
            "goblin rush"],

        "xp": 25,
        "gold": 15},

    "goblin_mage": {
        "name": "Goblin Mage",
        "region": "Forest",
        "level": 3,

        "max_hp": 90,
        "attack": 25,
        "defense": 5,
        "speed": 12,

        "weaknesses": ["blunt","ice"],

        "abilities": [
            "fire bolt",
            "mana burst",
            "arcane shield",
            "magic drain"],

        "xp": 40,
        "gold": 25},

    "werewolf": {
        "name": "Werewolf",
        "region": "Forest",
        "level": 5,

        "max_hp": 180,
        "attack": 30,
        "defense": 12,
        "speed": 18,

        "weaknesses": ["fire","thunder"],

        "abilities": [
            "quick slash",
            "savage bite",
            "howl",
            "regeneration"],

        "xp": 60,
        "gold": 35},

    "arachnophage": {
        "name": "Arachnophage",
        "region": "Forest",
        "level": 7,

        "max_hp": 150,
        "attack": 25,
        "defense": 10,
        "speed": 15,

        "weaknesses": [],

        "abilities": [
            "venom sting",
            "web trap",
            "venom spray",
            "spider rush"],

        "xp": 75,
        "gold": 40},

    "demon_bear": {
        "name": "Demon Bear",
        "region": "Forest",
        "level": 7,

        "max_hp": 250,
        "attack": 35,
        "defense": 18,
        "speed": 7,

        "weaknesses": ["holy bomb"],

        "abilities": [
            "claw swipe",
            "roar",
            "bear charge",
            "demonic rage"],

        "xp": 80,
        "gold": 50},

    "demon_wolf": {
        "name": "Dire Wolf",
        "region": "Forest",
        "level": 8,

        "max_hp": 160,
        "attack": 32,
        "defense": 10,
        "speed": 22,

        "weaknesses": [],

        "abilities": [
            "slash",
            "bite",
            "pack howl",
            "predator rush"],

        "xp": 80,
        "gold": 55},

    "unrest_undead": {
        "name": "Unrest Undead",
        "region": "Leonardo Dungeon",
        "level": 13,

        "max_hp": 220,
        "attack": 40,
        "defense": 15,
        "speed": 9,

        "weaknesses": [],

        "abilities": [
            "strong sword",
            "undead strength"],

        "xp": 125,
        "gold": 75},

    "zombie": {
    "name": "Zombie",
    "region": "Leonardo Dungeon",
    "level": 14,

    "max_hp": 190,
    "attack": 20,
    "defense": 8,
    "speed": 18,

    "weaknesses": [
        "fire",
        "thunder"],

    "abilities": [
        "slash",
        "poison bite"],

    "xp": 100,
    "gold": 60},

    "rock_troll": {
        "name": "Rock Troll",
        "region": "Leonardo Dungeon",
        "level": 15,

        "max_hp": 250,
        "attack": 30,
        "defense": 25,
        "speed": 5,

        "weaknesses": [],

        "abilities": [
            "rock smash",
            "ground slam",
            "stone skin",
            "throw rock"],

        "xp": 130,
        "gold": 70},

    "grave_rot": {
        "name": "Grave Rot",
        "region": "Leonardo Dungeon",
        "level": 17,

        "max_hp": 180,
        "attack": 25,
        "defense": 12,
        "speed": 10,

        "weaknesses": [
            "fire"],

        "abilities": [
            "ice field",
            "grave chill",
            "frost curse",
            "undead touch"],

        "xp": 150,
        "gold": 80},

    "necromancer_apprentice": {
        "name": "Necromancer Apprentice",
        "region": "Royal Capital",
        "level": 21,

        "max_hp": 200,
        "attack": 40,
        "defense": 10,
        "speed": 12,

        "weaknesses": [
            "fire",
            "ice"],

        "abilities": [
            "soul drain",
            "curse of death",
            "undead summon",
            "dark bolt",
            "necrotic blast"],

        "xp": 200,
        "gold": 120},

    "grave_knight": {
        "name": "Grave Knight",
        "region": "Royal Capital",
        "level": 23,

        "max_hp": 350,
        "attack": 50,
        "defense": 25,
        "speed": 10,

        "weaknesses": [
            "fire",
            "thunder"],

        "abilities": [
            "grave slash",
            "death strike",
            "dark shield",
            "grave charge"],

        "xp": 250,
        "gold": 150},

    "winged_gargoyle": {
        "name": "Winged Gargoyle",
        "region": "Ancient Ruins",
        "level": 26,

        "max_hp": 400,
        "attack": 55,
        "defense": 35,
        "speed": 15,

        "weaknesses": [],

        "abilities": [
            "stone claw",
            "wing slash",
            "gargoyle dive",
            "stone skin",
            "petrifying gaze"],

        "xp": 300,
        "gold": 180},

    "shadow_demon_panther": {
        "name": "Shadow Demon Panther",
        "region": "Ancient Ruins",
        "level": 27,

        "max_hp": 300,
        "attack": 55,
        "defense": 12,
        "speed": 25,

        "weaknesses": [
            "fire bomb",
            "fire magic"],

        "abilities": [
            "shadow claw",
            "shadow pounce",
            "dark fang",
            "shadow step",
            "nightmare roar"],

        "xp": 320,
        "gold": 200},

    "cursed_warrior": {
        "name": "Cursed Warrior",
        "region": "Ancient Ruins",
        "level": 28,

        "max_hp": 450,
        "attack": 60,
        "defense": 30,
        "speed": 12,

        "weaknesses": [
            "ice"],

        "abilities": [
            "cursed slash",
            "heavy strike",
            "frost curse",
            "dark guard",
            "cursed rage"],

        "xp": 350,
        "gold": 220},

    "higher_wraith": {
        "name": "Higher Wraith",
        "region": "Ancient Ruins",
        "level": 29,

        "max_hp": 300,
        "attack": 50,
        "defense": 10,
        "speed": 25,

        "weaknesses": [],

        "abilities": [
            "wraith slash",
            "soul drain",
            "phase shift",
            "death touch",
            "spirit scream"],

        "xp": 380,
        "gold": 240},

    "stone_golem": {
        "name": "Stone Golem",
        "region": "Ancient Ruins",
        "level": 30,

        "max_hp": 700,
        "attack": 65,
        "defense": 50,
        "speed": 5,

        "weaknesses": [],

        "abilities": [
            "stone fist",
            "ground slam",
            "rock throw",
            "stone wall",
            "earthquake"],

        "xp": 450,
        "gold": 300},

    "fire_ghoul": {
        "name": "Fire Ghoul",
        "region": "Volcano",
        "level": 41,

        "max_hp": 450,
        "attack": 65,
        "defense": 20,
        "speed": 18,

        "weaknesses": [
            "water",
            "ice"],

        "abilities": [
            "fire projectile",
            "flame bite",
            "burning touch",
            "fire burst"],

        "xp": 550,
        "gold": 350},

    "lava_wolf": {
        "name": "Lava Wolf",
        "region": "Volcano",
        "level": 44,

        "max_hp": 500,
        "attack": 75,
        "defense": 30,
        "speed": 28,

        "weaknesses": [
            "water",
            "ice",
            "water bomb"],

        "abilities": [
            "lava bite",
            "flame dash",
            "burning fang",
            "lava rush"],

        "xp": 600,
        "gold": 400},

    "magma_goblin": {
        "name": "Magma Goblin",
        "region": "Volcano",
        "level": 42,

        "max_hp": 400,
        "attack": 70,
        "defense": 25,
        "speed": 20,

        "weaknesses": [
            "water",
            "ice"],

        "abilities": [
            "magma slash",
            "lava throw",
            "fire bomb",
            "magma rage"],

        "xp": 580,
        "gold": 380},

    "molten_troll": {
        "name": "Molten Troll",
        "region": "Volcano",
        "level": 44,

        "max_hp": 800,
        "attack": 80,
        "defense": 45,
        "speed": 8,

        "weaknesses": [
            "water",
            "ice"],

        "abilities": [
            "molten smash",
            "lava slam",
            "magma armor",
            "burning roar",
            "magma explosion"],

        "xp": 700,
        "gold": 500},

    "rock_bats": {
        "name": "Rock Bats",
        "region": "Volcano",
        "level": 43,

        "max_hp": 300,
        "attack": 55,
        "defense": 15,
        "speed": 30,

        "weaknesses": [],

        "abilities": [
            "rock dive",
            "wing slash",
            "stone barrage",
            "sonic screech"],

        "xp": 500,
        "gold": 320},

    "yeti": {
        "name": "Yeti",
        "region": "Frozen Mountain",
        "level": 46,

        "max_hp": 1000,
        "attack": 100,
        "defense": 70,
        "speed": 5,

        "weaknesses": [
            "fire"],

        "abilities": [
            "snow ball",
            "ground smash",
            "slash",
            "frost roar",
            "frozen rage"],

        "xp": 850,
        "gold": 600},

    "high_wraith": {
        "name": "High Wraith",
        "region": "Frozen Mountain",
        "level": 47,

        "max_hp": 600,
        "attack": 75,
        "defense": 20,
        "speed": 35,

        "weaknesses": [
            "fire",
            "light"],

        "abilities": [
            "wonderland",
            "slash",
            "freeze frame",
            "soul drain",
            "phase shift"],

        "xp": 900,
        "gold": 650},

    "frostfang_wolf": {
        "name": "Frostfang Wolf",
        "region": "Frozen Mountain",
        "level": 48,

        "max_hp": 650,
        "attack": 110,
        "defense": 20,
        "speed": 45,

        "weaknesses": [
            "fire"
        ],

        "abilities": [
            "pounce",
            "frostbite",
            "ice fang",
            "howl",
            "frost dash"],

        "xp": 950,
        "gold": 700},

    "winter_stag": {
        "name": "Winter Stag",
        "region": "Frozen Mountain",
        "level": 49,

        "max_hp": 850,
        "attack": 100,
        "defense": 35,
        "speed": 35,

        "weaknesses": [
            "fire"
        ],

        "abilities": [
            "antler charge",
            "frozen roots",
            "ice hoof",
            "winter roar",
            "nature recovery"],

        "xp": 1000,
        "gold": 750},

    "glacial_golem": {
        "name": "Glacial Golem",
        "region": "Frozen Mountain",
        "level": 50,

        "max_hp": 1500,
        "attack": 120,
        "defense": 100,
        "speed": 3,

        "weaknesses": [
            "fire"
        ],

        "abilities": [
            "ice fist",
            "frost quake",
            "wall",
            "frozen armor",
            "glacial blast"],

        "xp": 1200,
        "gold": 900},

    "gale_hound": {
        "name": "Gale Hound",
        "region": "Sky Temple",
        "level": 52,

        "max_hp": 700,
        "attack": 110,
        "defense": 30,
        "speed": 45,

        "weaknesses": [],

        "abilities": [
            "wind fang",
            "gale rush",
            "wind howl",
            "cyclone bite"],

        "xp": 1300,
        "gold": 950},

    "zephyr_sprite": {
        "name": "Zephyr Sprite",
        "region": "Sky Temple",
        "level": 53,

        "max_hp": 400,
        "attack": 60,
        "defense": 10,
        "speed": 50,

        "weaknesses": [],

        "abilities": [
            "wind bolt",
            "gust",
            "air dash",
            "zephyr shield",
            "mini tornado"],

        "xp": 1250,
        "gold": 900},

    "storm_harpy": {
        "name": "Storm Harpy",
        "region": "Sky Temple",
        "level": 54,

        "max_hp": 750,
        "attack": 115,
        "defense": 25,
        "speed": 45,

        "weaknesses": [],

        "abilities": [
            "wind slash",
            "thunder talon",
            "storm call",
            "gale wing",
            "lightning dive"],

        "xp": 1400,
        "gold": 1000},

    "tornado_wyvern": {
        "name": "Tornado Wyvern",
        "region": "Sky Temple",
        "level": 56,

        "max_hp": 1100,
        "attack": 130,
        "defense": 45,
        "speed": 40,

        "weaknesses": [],

        "abilities": [
            "tornado breath",
            "wing strike",
            "cyclone",
            "wind shield",
            "tornado dive"],

        "xp": 1600,
        "gold": 1200},

    "windfang_mantis": {
        "name": "Windfang Mantis",
        "region": "Sky Temple",
        "level": 57,

        "max_hp": 750,
        "attack": 120,
        "defense": 35,
        "speed": 40,

        "weaknesses": [],

        "abilities": [
            "wind slash",
            "double claw",
            "gale blade",
            "mantis rush",
            "wind step"],

        "xp": 1550,
        "gold": 1100},

    "sky_jelly": {
        "name": "Sky Jelly",
        "region": "Sky Temple",
        "level": 58,

        "max_hp": 700,
        "attack": 90,
        "defense": 25,
        "speed": 35,

        "weaknesses": [],

        "abilities": [
            "electric shock",
            "gust blast",
            "static field",
            "air bubble",
            "thunder drop"],

        "xp": 1500,
        "gold": 1050},

    "dust_revenant": {
        "name": "Dust Revenant",
        "region": "Sky Temple",
        "level": 59,

        "max_hp": 750,
        "attack": 95,
        "defense": 25,
        "speed": 35,

        "weaknesses": [],

        "abilities": [
            "dust slash",
            "sand blast",
            "dust cloud",
            "wind drain",
            "phantom step"],

        "xp": 1650,
        "gold": 1200},

    "tempest_ram": {
        "name": "Tempest Ram",
        "region": "Sky Temple",
        "level": 60,

        "max_hp": 1100,
        "attack": 160,
        "defense": 45,
        "speed": 40,

        "weaknesses": [],

        "abilities": [
            "tempest charge",
            "horn strike",
            "cyclone ram",
            "storm roar",
            "wind armor"],

        "xp": 1800,
        "gold": 1400},

"hellspawn": {
    "name": "Hellspawn",
    "region": "Demon Realm",
    "level": 71,

    "max_hp": 1200,
    "attack": 180,
    "defense": 80,
    "speed": 25,

    "weaknesses": ["holy", "water"],

    "abilities": [
        "hell slash",
        "demonic roar",
        "burning claw",
        "blood rage"],

    "xp": 2000,
    "gold": 1500},

"demon_hound": {
    "name": "Demon Hound",
    "region": "Demon Realm",
    "level": 73,

    "max_hp": 900,
    "attack": 200,
    "defense": 50,
    "speed": 45,

    "weaknesses": ["holy", "ice"],

    "abilities": [
        "demon bite",
        "hell rush",
        "blood howl",
        "shadow pounce"],

    "xp": 2100,
    "gold": 1600},

"abyssal_imp": {
    "name": "Abyssal Imp",
    "region": "Demon Realm",
    "level": 74,

    "max_hp": 750,
    "attack": 230,
    "defense": 35,
    "speed": 40,

    "weaknesses": ["holy"],

    "abilities": [
        "dark bolt",
        "hellfire",
        "mana burn",
        "curse"],

    "xp": 2200,
    "gold": 1700},

"demon_knight": {
    "name": "Demon Knight",
    "region": "Demon Realm",
    "level": 76,

    "max_hp": 1800,
    "attack": 240,
    "defense": 130,
    "speed": 18,

    "weaknesses": ["holy", "thunder"],

    "abilities": [
        "demonic sword",
        "dark shield",
        "hell charge",
        "execution"],

    "xp": 2500,
    "gold": 2000},

"soul_devourer": {
    "name": "Soul Devourer",
    "region": "Demon Realm",
    "level": 78,

    "max_hp": 1400,
    "attack": 210,
    "defense": 70,
    "speed": 30,

    "weaknesses": ["holy", "fire"],

    "abilities": [
        "soul drain",
        "mana devour",
        "soul crush",
        "life steal"],

    "xp": 2700,
    "gold": 2200},

"blood_demon": {
    "name": "Blood Demon",
    "region": "Demon Realm",
    "level": 80,

    "max_hp": 1600,
    "attack": 260,
    "defense": 75,
    "speed": 35,

    "weaknesses": ["holy", "ice"],

    "abilities": [
        "blood slash",
        "blood drain",
        "crimson fang",
        "blood frenzy"],

    "xp": 2800,
    "gold": 2300},

"hellfire_brute": {
    "name": "Hellfire Brute",
    "region": "Demon Realm",
    "level": 82,

    "max_hp": 2500,
    "attack": 280,
    "defense": 150,
    "speed": 10,

    "weaknesses": ["water", "ice"],

    "abilities": [
        "hellfire punch",
        "infernal roar",
        "flame armor",
        "ground breaker"],

    "xp": 3000,
    "gold": 2500},

"void_stalker": {
    "name": "Void Stalker",
    "region": "Demon Realm",
    "level": 84,

    "max_hp": 1100,
    "attack": 320,
    "defense": 45,
    "speed": 50,

    "weaknesses": ["holy", "light"],

    "abilities": [
        "shadow strike",
        "void step",
        "backstab",
        "vanish"],

    "xp": 3200,
    "gold": 2700},

"demon_warlock": {
    "name": "Demon Warlock",
    "region": "Demon Realm",
    "level": 86,

    "max_hp": 1300,
    "attack": 350,
    "defense": 60,
    "speed": 32,

    "weaknesses": ["holy"],

    "abilities": [
        "dark meteor",
        "curse of death",
        "mana drain",
        "demon summon",
        "hellfire"],

    "xp": 3500,
    "gold": 3000},

"abyssal_reaper": {
    "name": "Abyssal Reaper",
    "region": "Demon Realm",
    "level": 90,

    "max_hp": 2200,
    "attack": 380,
    "defense": 100,
    "speed": 40,

    "weaknesses": ["holy", "light"],

    "abilities": [
        "soul reap",
        "death slash",
        "abyssal storm",
        "fear",
        "execution"],

    "xp": 4500,
    "gold": 4000},}
