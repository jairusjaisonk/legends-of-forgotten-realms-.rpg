bosses = {

    "pesqure": {
        "name": "Pesqure",
        "title": "Possessed Leshen",
        "level": 10,
        "area": "Elven Forest",

        "max_hp": 1500,
        "attack": 85,
        "defense": 55,
        "speed": 15,

        "weaknesses": [
            "thunder",
            "poison"
        ],

        "abilities": {
            "forest slam": {
                "attack_bonus": 30,
                "type": "physical",
                "effect": None,
                "chance": 100
            },

            "root bind": {
                "attack_bonus": 10,
                "type": "nature",
                "effect": "bind",
                "chance": 30
            },

            "corrupted nature": {
                "attack_bonus": 20,
                "type": "dark",
                "effect": "corruption",
                "chance": 25
            },

            "summon wolves": {
                "attack_bonus": 0,
                "type": "summon",
                "effect": "summon_wolves",
                "chance": 30
            }
        },

        "passive": "corrupted forest",

        "reward": {
            "natural_regeneration": 1
        },

        "loot_rarity": [
            "uncommon",
            "rare"],

        "is_boss": True},

    "gaunter": {
        "name": "Gaunter",
        "title": "Earth Golem",
        "level": 20,
        "area": "Leonardo Dungeon",

        "max_hp": 3500,
        "attack": 150,
        "defense": 120,
        "speed": 8,

        "weaknesses": [
            "water",
            "ice",
            "thunder"
        ],

        "abilities": {
            "stone fist": {
                "attack_bonus": 10,
                "type": "physical",
                "effect": None,
                "chance": 100
            },

            "rock throw": {
                "attack_bonus": 15,
                "type": "earth",
                "effect": None,
                "chance": 100
            },

            "earthquake": {
                "attack_bonus": 30,
                "type": "earth",
                "effect": None,
                "chance": 100
            },

            "stone wall": {
                "attack_bonus": 0,
                "type": "defense",
                "effect": "defense_up",
                "chance": 100
            },

            "demonic crush": {
                "attack_bonus": 50,
                "type": "physical",
                "effect": None,
                "chance": 100
            }
        },

        "passive": "stone heart",

        "reward": {
            "natural_regeneration": 3,
            "angelic_power": 1,
            "detection": 1
        },

        "loot_rarity": [
            "rare",
            "super rare"
        ],

        "is_boss": True},

    "arthur": {
        "name": "Arthur",
        "title": "Necromancer of the Ten Rings",
        "level": 30,
        "area": "Royal Capital",

        "max_hp": 6000,
        "attack": 240,
        "defense": 100,
        "speed": 30,
        "max_mp": 5000,

        "weaknesses": [
            "fire",
            "ice",
            "holy"
        ],

        "abilities": {
            "soul drain": {
                "attack_bonus": 20,
                "type": "dark",
                "effect": "mana_drain",
                "chance": 100
            },

            "curse of death": {
                "attack_bonus": 30,
                "type": "dark",
                "effect": "death_curse",
                "chance": 20
            },

            "undead summon": {
                "attack_bonus": 0,
                "type": "summon",
                "effect": "summon_undead",
                "chance": 30
            },

            "ten rings": {
                "attack_bonus": 60,
                "type": "dark",
                "effect": "attack_up",
                "chance": 100
            },

            "dark meteor": {
                "attack_bonus": 80,
                "type": "dark",
                "effect": None,
                "chance": 100
            },

            "fear": {
                "attack_bonus": 0,
                "type": "dark",
                "effect": "fear",
                "chance": 100
            },

            "death dominion": {
                "attack_bonus": 150,
                "type": "dark",
                "effect": "massive_damage",
                "chance": 100
            }
        },

        "passive": "ten rings",

        "reward": {
            "quest_item": "royal mage's crystal"
        },

        "loot_rarity": [
            "rare",
            "super rare"],

        "is_boss": True},

    "cursed king": {
        "name": "Cursed King",
        "title": "Cursed King of the Ruins",
        "level": 40,
        "area": "Ancient Ruins",

        "max_hp": 9000,
        "attack": 320,
        "defense": 180,
        "speed": 18,

        "weaknesses": [
            "holy",
            "fire",
            "thunder"
        ],

        "abilities": {
            "cursed sword": {
                "attack_bonus": 25,
                "type": "physical",
                "effect": "curse",
                "chance": 20
            },

            "dark slash": {
                "attack_bonus": 20,
                "type": "dark",
                "effect": None,
                "chance": 100
            },

            "king's judgment": {
                "attack_bonus": 40,
                "type": "dark",
                "effect": "fear",
                "chance": 30
            },

            "royal guard": {
                "attack_bonus": 0,
                "type": "defense",
                "effect": "defense_up",
                "chance": 100
            },

            "curse of ruin": {
                "attack_bonus": 15,
                "type": "dark",
                "effect": "curse",
                "chance": 35
            },

            "summon undead": {
                "attack_bonus": 0,
                "type": "summon",
                "effect": "summon_undead",
                "chance": 30
            }
        },

        "passive": "cursed king",

        "reward": {
            "natural_regeneration": 4,
            "angelic_power": 2,
            "detection": 2
        },

        "loot_rarity": [
            "super rare",
            "epic"],

            "is_boss": True},

    "fire dragon": {
        "name": "Fire Dragon",
        "title": "Dragon of the Volcano",
        "level": 50,
        "area": "Volcano",

        "max_hp": 12000,
        "attack": 400,
        "defense": 250,
        "speed": 25,

        "weaknesses": [
            "ice",
            "water",
            "water bomb"
        ],

        "abilities": {
            "fire breath": {
                "attack_bonus": 40,
                "type": "fire",
                "effect": "burn",
                "chance": 30
            },

            "dragon claw": {
                "attack_bonus": 20,
                "type": "physical",
                "effect": None,
                "chance": 100
            },

            "flame tail": {
                "attack_bonus": 30,
                "type": "fire",
                "effect": "burn",
                "chance": 20
            },

            "inferno": {
                "attack_bonus": 80,
                "type": "fire",
                "effect": "burn",
                "chance": 50
            },

            "dragon roar": {
                "attack_bonus": 10,
                "type": "fire",
                "effect": "fear",
                "chance": 20
            }
        },

        "passive": "flame armor",

        "reward": {
            "dragon_core": "fire dragon core"
        },

        "loot_rarity": [
            "super rare",
            "epic"],

            "is_boss": True},

    "ice dragon": {
        "name": "Ice Dragon",
        "title": "Dragon of the Frozen Mountain",
        "level": 60,
        "area": "Frozen Mountain",

        "max_hp": 16000,
        "attack": 450,
        "defense": 280,
        "speed": 22,

        "weaknesses": [
            "fire",
            "fire bomb"
        ],

        "abilities": {
            "frost breath": {
                "attack_bonus": 40,
                "type": "ice",
                "effect": "freeze",
                "chance": 30
            },

            "ice claw": {
                "attack_bonus": 25,
                "type": "ice",
                "effect": None,
                "chance": 100
            },

            "frozen prison": {
                "attack_bonus": 15,
                "type": "ice",
                "effect": "freeze",
                "chance": 40
            },

            "blizzard": {
                "attack_bonus": 70,
                "type": "ice",
                "effect": "freeze",
                "chance": 30
            },

            "dragon roar": {
                "attack_bonus": 10,
                "type": "ice",
                "effect": "fear",
                "chance": 20
            },

            "absolute zero": {
                "attack_bonus": 100,
                "type": "ice",
                "effect": "freeze",
                "chance": 60
            }
        },

        "passive": "frozen scales",

        "reward": {
            "dragon_core": "ice dragon core"
        },

        "loot_rarity": [
            "epic",
            "mythical"],

            "is_boss": True},

    "wind dragon": {
        "name": "Wind Dragon",
        "title": "Dragon of the Sky Temple",
        "level": 70,
        "area": "Sky Temple",

        "max_hp": 20000,
        "attack": 520,
        "defense": 220,
        "speed": 45,

        "weaknesses": [
            "thunder",
            "thunder bomb"
        ],

        "abilities": {
            "wind slash": {
                "attack_bonus": 30,
                "type": "wind",
                "effect": None,
                "chance": 100
            },

            "tornado breath": {
                "attack_bonus": 60,
                "type": "wind",
                "effect": None,
                "chance": 100
            },

            "sky dive": {
                "attack_bonus": 45,
                "type": "physical",
                "effect": None,
                "chance": 100
            },

            "cyclone": {
                "attack_bonus": 80,
                "type": "wind",
                "effect": "multi_hit",
                "chance": 100
            },

            "dragon roar": {
                "attack_bonus": 10,
                "type": "wind",
                "effect": "fear",
                "chance": 20
            },

            "heaven's tornado": {
                "attack_bonus": 100,
                "type": "wind",
                "effect": "multi_hit",
                "chance": 100
            }
        },

        "passive": "wind step",

        "reward": {
            "dragon_core": "wind dragon core"
        },

        "loot_rarity": [
            "epic",
            "mythical"],

            "is_boss": True},

    "corrupted golden dragon": {
        "name": "Corrupted Golden Dragon",
        "title": "The Betrayed Dragon",
        "level": 80,
        "area": "Abyss",

        "max_hp": 45000,
        "attack": 950,
        "defense": 400,
        "speed": 40,

        "weaknesses": [
            "holy",
            "light"
        ],

        "abilities": {
            "golden breath": {
                "attack_bonus": 80,
                "type": "light",
                "effect": None,
                "chance": 100
            },

            "corrupted claw": {
                "attack_bonus": 40,
                "type": "dark",
                "effect": "corruption",
                "chance": 30
            },

            "abyssal roar": {
                "attack_bonus": 30,
                "type": "dark",
                "effect": "fear",
                "chance": 25
            },

            "dragon's fury": {
                "attack_bonus": 100,
                "type": "physical",
                "effect": None,
                "chance": 100
            },

            "golden meteor": {
                "attack_bonus": 120,
                "type": "light",
                "effect": None,
                "chance": 100
            },

            "corruption": {
                "attack_bonus": 20,
                "type": "dark",
                "effect": "corruption",
                "chance": 50
            }
        },

        "passive": "corrupted golden scales",

        "story": {
            "betrayed_by": [
                "fire dragon",
                "ice dragon",
                "wind dragon"
            ],

            "becomes_ally": True,

            "opens_demon_realm_portal": True,

            "helps_final_battle": True
        },

        "reward": {
            "special": "demon realm portal"
        },

        "loot_rarity": [
            "mythical",
            "legendary"],

            "is_boss": True},

    "demon general": {
        "name": "Demon General",
        "title": "General of Lucifero",
        "level": 90,
        "area": "Demon Realm",

        "max_hp": 35000,
        "attack": 800,
        "defense": 300,
        "speed": 35,

        "weaknesses": [
            "holy",
            "light"
        ],

        "abilities": {
            "demon blade": {
                "attack_bonus": 50,
                "type": "dark",
                "effect": None,
                "chance": 100
            },

            "hellfire": {
                "attack_bonus": 70,
                "type": "fire",
                "effect": "burn",
                "chance": 35
            },

            "dark shockwave": {
                "attack_bonus": 60,
                "type": "dark",
                "effect": None,
                "chance": 100
            },

            "demonic roar": {
                "attack_bonus": 20,
                "type": "dark",
                "effect": "fear",
                "chance": 30
            },

            "life drain": {
                "attack_bonus": 30,
                "type": "dark",
                "effect": "life_steal",
                "chance": 100
            },

            "regeneration": {
                "attack_bonus": 0,
                "type": "healing",
                "effect": "heal",
                "chance": 100
            },

            "hell dominion": {
                "attack_bonus": 120,
                "type": "dark",
                "effect": "attack_up",
                "chance": 100
            }
        },

        "passive": "demonic regeneration",

        "reward": {
            "rarity": "legendary"
        },

        "loot_rarity": [
            "mythical",
            "legendary"],

            "is_boss": True},

    "lucifero": {
        "name": "Lucifero",
        "title": "Ancient Demon King",
        "level": 100,
        "area": "Demon Realm",

        "max_hp": 100000,
        "attack": 2000,
        "defense": 600,
        "speed": 50,
        "max_mp": 20000,

        "weaknesses": [
            "holy",
            "light",
            "angelic energy"
        ],

        "abilities": {
            "demon king's blade": {
                "attack_bonus": 100,
                "type": "dark",
                "effect": None,
                "chance": 100
            },

            "hellfire": {
                "attack_bonus": 120,
                "type": "fire",
                "effect": "burn",
                "chance": 40
            },

            "dark meteor": {
                "attack_bonus": 150,
                "type": "dark",
                "effect": None,
                "chance": 100
            },

            "soul destroyer": {
                "attack_bonus": 200,
                "type": "dark",
                "effect": "life_drain",
                "chance": 30
            },

            "curse of death": {
                "attack_bonus": 80,
                "type": "dark",
                "effect": "death_curse",
                "chance": 25
            },

            "fear": {
                "attack_bonus": 0,
                "type": "dark",
                "effect": "fear",
                "chance": 100
            },

            "demonic regeneration": {
                "attack_bonus": 0,
                "type": "healing",
                "effect": "heal",
                "chance": 100
            },

            "hell gate": {
                "attack_bonus": 100,
                "type": "dark",
                "effect": "demon_summon",
                "chance": 50
            },

            "abyssal judgment": {
                "attack_bonus": 250,
                "type": "dark",
                "effect": "massive_damage",
                "chance": 100
            }
        },

        "passive": "ancient demon king",

        "phases": {

            "phase_1": {
                "name": "Demon King",
                "hp_above": 70
            },

            "phase_2": {
                "name": "Lord of Hell",
                "hp_below": 70,
                "hp_above": 40,
                "attack_bonus": 30,
                "speed_bonus": 20
            },

            "phase_3": {
                "name": "Ancient Demon",
                "hp_below": 40,
                "hp_above": 10,
                "abilities_unlocked": [
                    "curse of death",
                    "fear",
                    "soul destroyer",
                    "abyssal judgment"
                ]
            },

            "phase_4": {
                "name": "Final Stand",
                "hp_below": 10,
                "golden_dragon_assists": True
            }
        },

        "reward": {
            "victory": True,
            "story_completion": True
        },

        "loot_rarity": [
            "legendary"],

            "is_boss": True}
}