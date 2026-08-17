
class Item:

    def __init__(self, name, rarity, price):

        self.name = name
        self.rarity = rarity
        self.price = price

class Potion(Item):

    def __init__(
        self,
        name,
        rarity,
        price,
        effect,
        amount
    ):

        super().__init__(
            name,
            rarity,
            price
        )

        self.effect = effect
        self.amount = amount

    def use(self, player):

        if self.effect.lower() == "health":

            old_hp = player.current_hp

            player.current_hp += self.amount

            if player.current_hp > player.max_hp:
                player.current_hp = player.max_hp

            restored = player.current_hp - old_hp

            print(
                f"{player.name} restored "
                f"{restored} HP."
            )

        elif self.effect.lower() == "mana":

            old_mp = player.current_mp

            player.current_mp += self.amount

            if player.current_mp > player.max_mp:
                player.current_mp = player.max_mp

            restored = player.current_mp - old_mp

            print(
                f"{player.name} restored "
                f"{restored} MP."
            )

        elif self.effect.lower() == "health + mana":

            old_hp = player.current_hp
            old_mp = player.current_mp

            player.current_hp += self.amount
            player.current_mp += self.amount

            if player.current_hp > player.max_hp:
                player.current_hp = player.max_hp

            if player.current_mp > player.max_mp:
                player.current_mp = player.max_mp

            restored_hp = player.current_hp - old_hp
            restored_mp = player.current_mp - old_mp

            print(
                f"{player.name} restored "
                f"{restored_hp} HP and "
                f"{restored_mp} MP."
            )

        else:

            print("Unknown potion effect.")

class Bomb(Item):

    def __init__(
        self,
        name,
        rarity,
        price,
        damage,
        element
    ):

        super().__init__(
            name,
            rarity,
            price
        )

        self.damage = damage
        self.element = element

    def use(self, enemy):

        damage = self.damage

        print(
            f"{self.name} dealt "
            f"{damage} {self.element} damage!"
        )

        return damage

class Weapon(Item):

    def __init__(
        self,
        name,
        rarity,
        price,
        damage,
        crit_chance,
        crit_damage
    ):

        super().__init__(
            name,
            rarity,
            price
        )

        self.damage = damage
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage

class Armor(Item):

    def __init__(
        self,
        name,
        rarity,
        price,
        defense
    ):

        super().__init__(
            name,
            rarity,
            price
        )

        self.defense = defense

class Accessory(Item):

    def __init__(
        self,
        name,
        rarity,
        price,
        attack_bonus=0,
        defense_bonus=0,
        speed_bonus=0,
        crit_chance_bonus=0,
        crit_damage_bonus=0,
        hp_bonus=0,
        mp_bonus=0
    ):

        super().__init__(
            name,
            rarity,
            price
        )

        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.speed_bonus = speed_bonus
        self.crit_chance_bonus = crit_chance_bonus
        self.crit_damage_bonus = crit_damage_bonus
        self.hp_bonus = hp_bonus
        self.mp_bonus = mp_bonus
        
class QuestItem(Item):

    def __init__(self, name, rarity, price, description):

        super().__init__(name, rarity, price)

        self.description = description

potions = {    
    "small health" : {
    "name"        : "small health potion",
    "rarity"       : "common",
    "price"        : 30 ,
    "effect"       : {"health" : 50}},

    "medium health" : {
    "name"        : "medium health potion",
    "rarity"       : "rare",
    "price"        : 70 ,
    "effect"       : {"health" : 100}},

    "large health" : {
    "name"        : "large health potion",
    "rarity"       : "unique",
    "price"        : 200 ,
    "effect"       : {"health" : 250}},

    "Giant health" : {
    "name"        : "Giant health potion",
    "rarity"       : "mythical",
    "price"        :  400,
    "effect"       : {"health" : 500}},

    "ultimate health" : {
    "name"        : "Ultimate health potion",
    "rarity"       : "Legendary",
    "price"        :  1000,
    "effect"       : {"health" : 99999}},

    "small mana" : {
    "name"        : "small mana potion",
    "rarity"       : "common",
    "price"        : 30 ,
    "effect"       : {"mana" : 50}},

    "medium mana" : {
    "name"        : "medium mana potion",
    "rarity"       : "uncommon",
    "price"        : 70 ,
    "effect"       : {"mana" : 100}},

    "large mana" : {
    "name"        : "large mana potion",
    "rarity"       : "rare",
    "price"        : 200 ,
    "effect"       : {"mana": 250}},

    "Giant mana" : {
    "name"        : "Giant mana potion",
    "rarity"       : "mythical",
    "price"        :  400,
    "effect"       : {"mana" : 500}},

    "ultimate mana" : {
    "name"        : "Ultimate mana potion",
    "rarity"       : "legendary",
    "price"        :  1000,
    "effect"       : {"mana" : 99999}},

    "mixed potion" : {
    "name"        : "mix match",
    "rarity"       : "rare",
    "price"        : 200 ,
    "effect"       : { "health" : 50,
                      "mana"  : 50 }},

    "attack potion" : {
    "name"          : "attack potion",
    "rarity"       : "rare",
    "price"        :  150,
    "effect"       : {"attack" : 30}},

    "defense potion" : {
    "name"          : "defense potion",
    "rarity"       : "rare",
    "price"        :  150,
    "effect"       : {"defense" : 30},
    "amount"       :  200},

    "speed potion" : {
    "name"          : "speed potion",
    "rarity"       : "rare",
    "price"        :  100,
    "effect"       : {"speed" : 10}},

    "crit chance potion" : {
    "name"          : "crit chance potion",
    "rarity"       : "rare",
    "price"        :  100,
    "effect"       : {"crit_chance" : 10}},

    " crit damage potion" : {
    "name"          : "crit damage potion",
    "rarity"       : "rare",
    "price"        :  100,
    "effect"       : {"crit_damage buff" : 1.0}}}

bombs = { 
    "fire bomb" :{
    "name"     : "fire Bomb",
    "rarity"   : "Common",
    "price"    : 50,                                                                
    "damage"  : 100,
    "element"  : "fire"},

    "uncommon_fire bomb" :{
    "name"     : "flame Bomb",
    "rarity"   : "uncommon",
    "price"    : 180,
    "damage"   : 200,
    "element"  : "fire",
    "status"   : "burn",
    "status_chance": 15},

    "rare_fire bomb" :{
    "name"     : "Inferno Bomb",
    "rarity"   : "rare",
    "price"    : 300,
    "damage"   : 300,
    "element"  : "fire",
    "status"   : "burn",
    "status_chance": 20},

   "super_rare_fire bomb" :{
    "name"     : "Magma Bomb",
    "rarity"   : "superrare",
    "price"    : 700,
    "damage"   : 500,
    "element"  : "fire",
    "status"   : "burn",
    "status_chance": 25},
 
   "epic_fire bomb" :{
    "name"     : "Dragonfire Bomb",
    "rarity"   : "epic",
    "price"    : 1500,
    "damage"   : 800,
    "element"  : "fire",
    "status"   : "burn",
    "status_chance": 30},

    "mythical_fire bomb" :{
    "name"     : "Phoenix Bomb",
    "rarity"   : "mythical",
    "price"    : 3500,
    "damage"   : 1300,
    "element"  : "fire",
    "status"   : "burn",
    "status_chance": 40},

    "legendary_fire bomb" :{
    "name"     : "Primordial flame",
    "rarity"   : "legendary",
    "price"    : 8000,
    "damage"   : 2500,
    "element"  : "fire",
    "status"   : "burn",
    "status_chance": 50},

        # WATER BOMBS

    "water bomb" :{
    "name"     : "Auqa Bomb",
    "rarity"   : "Common",
    "price"    : 50,
    "damage"   : 100,
    "element"  : "water"},                    

    "uncommon_water bomb" :{
    "name"     : "Tidal Bomb",
    "rarity"   : "uncommon",
    "price"    : 180,
    "damage"   : 200,
    "element"  : "water"},

    "rare_water bomb" :{
    "name"     : "Waterburst Bomb",
    "rarity"   : "rare",
    "price"    : 300,
    "damage"   : 300,
    "element"  : "water"},

   "super_rare_water bomb" :{
    "name"     : "Tsunami Bomb",
    "rarity"   : "superrare",
    "price"    : 700,
    "damage"   : 500,
    "element"  : "water"},
 
   "epic_water bomb" :{
    "name"     : "siren's Bomb",
    "rarity"   : "epic",
    "price"    : 1500,
    "damage"   : 800,
    "element"  : "water"},

    "mythical_water bomb" :{
    "name"     : "Leviathan's wrath",
    "rarity"   : "mythical",
    "price"    : 3500,
    "damage"   : 1300,
    "element"  : "water"},

    "legendary_water bomb" :{
    "name"     : "Abyssal Tide ",
    "rarity"   : "legendary",
    "price"    : 8000,
    "damage"   : 2500,
    "element"  : "water"},     

    # ICE BOMBS                                                                              

    "ice bomb" :{
    "name"     : "frost Bomb",
    "rarity"   : "Common",
    "price"    : 50,
    "Damage "  : 100,
    "element"  : "ice"},

    "uncommon_ice bomb" :{
    "name"     : "ice shards Bomb",
    "rarity"   : "uncommon",
    "price"    : 180,
    "damage"   : 200,
    "element"  : "ice"},

    "rare_ice bomb" :{
    "name"     : "Glacial Bomb",
    "rarity"   : "rare",
    "price"    : 300,
    "damage"   : 300,
    "element"  : "ice"},

   "super_rare_ice bomb" :{
    "name"     : "Frozen Heart Bomb",
    "rarity"   : "superrare",
    "price"    : 700,
    "damage"   : 500,
    "element"  : "ice"},
 
   "epic_ice bomb" :{
    "name"     : "dwarf star Bomb",
    "rarity"   : "epic",
    "price"    : 1500,
    "damage"   : 800,
    "element"  : "ice"},

    "mythical_ice bomb" :{
    "name"     : "sub zero bomb",
    "rarity"   : "mythical",
    "price"    : 3500,
    "damage"   : 1300,
    "element"  : "ice"},

    "legendary_ice bomb" :{
    "name"     : "Neptune's wrath",
    "rarity"   : "legendary",
    "price"    : 8000,
    "damage"   : 2500,
    "element"  : "ice"}, 

        # HOLY BOMBS

    "common_holy_bomb": {
    "name": "Holy Bomb",
    "rarity": "common",
    "price": 100,
    "damage": 120,
    "element": "holy"},

    "uncommon_holy_bomb": {
    "name": "Sacred Bomb",
    "rarity": "uncommon",
    "price": 250,
    "damage": 220,
    "element": "holy"},

    "rare_holy_bomb": {
    "name": "Purification Bomb",
    "rarity": "rare",
    "price": 500,
    "damage": 350,
    "element": "holy"},

    "super_rare_holy_bomb": {
    "name": "Divine Light Bomb",
    "rarity": "super rare",
    "price": 1000,
    "damage": 600,
    "element": "holy"},

    "epic_holy_bomb": {
    "name": "Angelic Bomb",
    "rarity": "epic",
    "price": 2000,
    "damage": 900,
    "element": "holy"},

    "mythical_holy_bomb": {
    "name": "Gaia's blessing ",
    "rarity": "mythical",
    "price": 5000,
    "damage": 1500,
    "element": "holy"},

    "legendary_holy_bomb": {
    "name": "Divine Retribution",
    "rarity": "legendary",
    "price": 10000,
    "damage": 3000,
    "element": "holy"},

    # THUNDER BOMBS

    "common_thunder_bomb": {
    "name": "Spark Bomb",
    "rarity": "common",
    "price": 100,
    "damage": 100,
    "element": "thunder",
    "status": "stun",
    "status_chance": 10},

    "uncommon_thunder_bomb": {
    "name": "Thunder Bomb",
    "rarity": "uncommon",
    "price": 250,
    "damage": 200,
    "element": "thunder",
    "status": "stun",
    "status_chance": 15},

    "rare_thunder_bomb": {
    "name": "Lightning Bomb",
    "rarity": "rare",
    "price": 500,
    "damage": 350,
    "element": "thunder",
    "status": "stun",
    "status_chance": 20},

    "super_rare_thunder_bomb": {
    "name": "Storm Bomb",
    "rarity": "super rare",
    "price": 1000,
    "damage": 600,
    "element": "thunder",
    "status": "stun",
    "status_chance": 25},

    "epic_thunder_bomb": {
    "name": "Thunderclap Bomb",
    "rarity": "epic",
    "price": 2000,
    "damage": 900,
    "element": "thunder",
    "status": "stun",
    "status_chance": 30},

    "mythical_thunder_bomb": {
    "name": "Heavenly Thunder",
    "rarity": "mythical",
    "price": 5000,
    "damage": 1500,
    "element": "thunder",
    "status": "stun",
    "status_chance": 40},

    "legendary_thunder_bomb": {
    "name": "Eye of the Storm",
    "rarity": "legendary",
    "price": 12000,
    "damage": 3000,
    "element": "thunder",
    "status": "stun",
    "status_chance": 50},

    # POISON BOMBS

    "poison_bomb": {
        "name": "Venom Bomb",
        "rarity": "common",
        "price": 100,
        "damage": 80,
        "element": "poison",
        "status": "poison",
        "status_chance": 30},

    "uncommon_poison_bomb": {
        "name": "Toxic Bomb",
        "rarity": "uncommon",
        "price": 250,
        "damage": 150,
        "element": "poison",
        "status": "poison",
        "status_chance": 40},

    "rare_poison_bomb": {
        "name": "Venomburst",
        "rarity": "rare",
        "price": 500,
        "damage": 250,
        "element": "poison",
        "status": "poison",
        "status_chance": 50},

    "super_rare_poison_bomb": {
        "name": "Plague Bomb",
        "rarity": "super rare",
        "price": 1000,
        "damage": 400,
        "element": "poison",
        "status": "poison",
        "status_chance": 60},

    "epic_poison_bomb": {
        "name": "Deathmist Bomb",
        "rarity": "epic",
        "price": 2000,
        "damage": 650,
        "element": "poison",
        "status": "poison",
        "status_chance": 70},

    "mythical_poison_bomb": {
        "name": "Plaguebringer",
        "rarity": "mythical",
        "price": 5000,
        "damage": 1000,
        "element": "poison",
        "status": "poison",
        "status_chance": 80},

    "legendary_poison_bomb": {
        "name": "Death's Breath",
        "rarity": "legendary",
        "price": 12000,
        "damage": 1800,
        "element": "poison",
        "status": "poison",
        "status_chance": 90},

    # UTILITY
    "smoke_bomb": {
    "name": "Smoke Bomb",
    "rarity": "common",
    "price": 100,
    "damage": 0,
    "element": "none",
    "status": "blind",
    "status_chance": 80},

    "flash_bomb": {
    "name": "Flash Bomb",
    "rarity": "uncommon",
    "price": 150,
    "damage": 50,
    "element": "light",
    "status": "blind",
    "status_chance": 60},}                  

weapons = {
        # SWORDS
    "Oakguard": {
        "name": "Oakguard",
        "category": "Sword",
        "rarity": "Common",
        "price": 150,
        "damage": 20,
        "crit_chance_bonus": 2,
        "crit_damage_bonus": 0.2 },

    "silveredge": {
        "name": "silveredge",
        "category": "Sword",
        "rarity": "uncommon",
        "price": 400,
        "damage": 15,
        "crit_chance_bonus": 4,
        "crit_damage_bonus": 0.2},

    "Burnheart": {
        "name": "burnheart",
        "category": "Sword",
        "rarity": "rare",
        "price": 900,
        "damage": 60,
        "crit_chance_bonus": 6,
        "crit_damage_bonus": 0.3},

    "Stormblade": {
        "name": "Stormblade",
        "category": "Sword",
        "rarity": "super_rare",
        "price": 1700,
        "damage": 100,
        "crit_chance_bonus": 10,
        "crit_damage_bonus": 0.2 },

    "Demonfang": {
        "name": "Demonfang",
        "category": "Sword",
        "rarity": "epic",
        "price": 2100,
        "damage": 120,
        "crit_chance_bonus": 8,
        "crit_damage_bonus": 0.5 },

    "Cereberus": {
        "name": "Cereberus",
        "category": "Sword",
        "rarity": "epic",
        "price": 5000,
        "damage": 180,
        "crit_chance_bonus": 12,
        "crit_damage_bonus": 0.4 },

    "Celestial Edge": {
        "name": "Celestial Edge",
        "category": "Sword",
        "rarity": "mythical",
        "price": 9000,
        "damage": 180,
        "crit_chance_bonus": 16,
        "crit_damage_bonus": 0.6 },

    "Excaliber": {
        "name": "Excaliber",
        "category": "Sword",
        "rarity": "mythical",
        "price": 11000,
        "damage": 220,
        "crit_chance_bonus": 16,
        "crit_damage_bonus": 0.8 },

    "Doomslayer": {
        "name": "Doomslayer",
        "category": "Sword",
        "rarity": "legendary",
        "price": 21000,
        "damage": 340,
        "crit_chance_bonus": 20,
        "crit_damage_bonus": 1.0 },

    "Eldoria's Fate": {
        "name": "Eldoria's Fate",
        "category": "Sword",
        "rarity": "legendary",
        "price": 29000,
        "damage": 400,
        "crit_chance_bonus": 25,
        "crit_damage_bonus": 1.6 },

        # STAFF 

    "Apprentice Staff": {
        "name": "Apprentice Staff",
        "category": "Staff",
        "rarity": "Common",
        "price": 100,
        "damage": 20,
        "crit_chance_bonus": 0.75,
        "crit_damage_bonus": 0.0
    },
                                      
    "Moonwood Staff": {
        "name": "Moonwood Staff",
        "category": "Staff",
        "rarity": "uncommon",
        "price": 250,
        "damage": 35,
        "crit_chance_bonus": 3,
        "crit_damage_bonus": 0.5              
    },

    "Frostspire": {
        "name": "Frostspire",
        "category": "Staff",
        "rarity": "rare",
        "price": 900,
        "damage": 60,
        "crit_chance_bonus": 6,
        "crit_damage_bonus": 0.3},

    "Voidbranch": {
        "name": "Voidbranch",
        "category": "Staff",
        "rarity": "super_rare",
        "price": 1200,
        "damage": 80,
        "crit_chance_bonus": 8,
        "crit_damage_bonus": 0.25 },

    "Storm caller": {
        "name": "Storm caller",
        "category": "Staff",
        "rarity": "epic",
        "price": 2100,
        "damage": 120,
        "crit_chance_bonus": 8,
        "crit_damage_bonus": 0.5 },

    "Meteor Staff": {
        "name": "Meteor Staff",
        "category": "Staff",
        "rarity": "epic",
        "price": 5000,
        "damage": 180,
        "crit_chance_bonus": 12,
        "crit_damage_bonus": 0.6 },

    "Celestial Staff": {
        "name": "Celestial Staff",
        "category": "Staff",
        "rarity": "mythical",
        "price": 9000,
        "damage": 190,
        "crit_chance_bonus": 17,
        "crit_damage_bonus": 0.7 },

    "Dragonheart Staff": {
        "name": "Dragonheart Staff",
        "category": "Staff",
        "rarity": "mythical",
        "price": 11000,
        "damage": 210,
        "crit_chance_bonus": 16,
        "crit_damage_bonus": 0.9 },

    "Staff of the Gods": {
        "name": "Staff of the Gods",
        "category": "Staff",
        "rarity": "legendary",
        "price": 18000,
        "damage": 340,
        "crit_chance_bonus": 20,
        "crit_damage_bonus": 1.2 },

    "Eternal Worldtree": {
        "name": "Eternal Worldtree",
        "category": "Staff",
        "rarity": "legendary",
        "price": 25000,
        "damage": 400,
        "crit_chance_bonus": 17,
        "crit_damage_bonus": 1.4 },

    # DAGGER

    "Rusty Dagger": {
    "name": "Rusty Dagger",
    "category": "Dagger",
    "rarity": "common",
    "price": 80,
    "damage": 18,
    "crit_chance_bonus": 2,
    "crit_damage_bonus": 0.0},

"Shadow Knife": {
    "name": "Shadow Knife",
    "category": "Dagger",
    "rarity": "uncommon",
    "price": 240,
    "damage": 30,
    "crit_chance_bonus": 5,
    "crit_damage_bonus": 0.3},

"Venom Fang": {
    "name": "Venom Fang",
    "category": "Dagger",
    "rarity": "rare",
    "price": 750,
    "damage": 50,
    "crit_chance_bonus": 8,
    "crit_damage_bonus": 0.5},

"Nightpiercer": {
    "name": "Nightpiercer",
    "category": "Dagger",
    "rarity": "super_rare",
    "price": 1500,
    "damage": 75,
    "crit_chance_bonus": 11,
    "crit_damage_bonus": 0.7},

"Phantom Fang": {
    "name": "Phantom Fang",
    "category": "Dagger",
    "rarity": "epic",
    "price": 3500,
    "damage": 110,
    "crit_chance_bonus": 14,
    "crit_damage_bonus": 0.9},

"Bloodmoon Daggers": {
    "name": "Bloodmoon Daggers",
    "category": "Dagger",
    "rarity": "epic",
    "price": 4800,
    "damage": 135,
    "crit_chance_bonus": 16,
    "crit_damage_bonus": 1.0},

"Assassin's Eclipse": {
    "name": "Assassin's Eclipse",
    "category": "Dagger",
    "rarity": "mythical",
    "price": 8500,
    "damage": 175,
    "crit_chance_bonus": 19,
    "crit_damage_bonus": 1.2},

"Voidfang Twins": {
    "name": "Voidfang Twins",
    "category": "Dagger",
    "rarity": "mythical",
    "price": 11000,
    "damage": 205,
    "crit_chance_bonus": 22,
    "crit_damage_bonus": 1.3},

"Death's Whisper": {
    "name": "Death's Whisper",
    "category": "Dagger",
    "rarity": "legendary",
    "price": 18000,
    "damage": 280,
    "crit_chance_bonus": 25,
    "crit_damage_bonus": 1.5},

"Godkiller Twins": {
    "name": "Godkiller Twins",
    "category": "Dagger",
    "rarity": "legendary",
    "price": 25000,
    "damage": 340,
    "crit_chance_bonus": 28,
    "crit_damage_bonus": 1.8},

    # DAGGER

"Rustfang Greatsword": {
    "name": "Rustfang Greatsword",
    "category": "Greatsword",
    "rarity": "common",
    "price": 120,
    "damage": 25,
    "crit_chance_bonus": 0.5,
    "crit_damage_bonus": 0.0},

"Knightbreaker": {
    "name": "Knightbreaker",
    "category": "Greatsword",
    "rarity": "uncommon",
    "price": 300,
    "damage": 42,
    "crit_chance_bonus": 2,
    "crit_damage_bonus": 0.3},

"Frostcleaver": {
    "name": "Frostcleaver",
    "category": "Greatsword",
    "rarity": "rare",
    "price": 900,
    "damage": 70,
    "crit_chance_bonus": 4,
    "crit_damage_bonus": 0.4},

"Doomfang": {
    "name": "Doomfang",
    "category": "Greatsword",
    "rarity": "super_rare",
    "price": 1800,
    "damage": 105,
    "crit_chance_bonus": 6,
    "crit_damage_bonus": 0.5},

"Dragon Slayer": {
    "name": "Dragon Slayer",
    "category": "Greatsword",
    "rarity": "epic",
    "price": 4000,
    "damage": 155,
    "crit_chance_bonus": 8,
    "crit_damage_bonus": 0.7},

"Oblivion Blade": {
    "name": "Oblivion Blade",
    "category": "Greatsword",
    "rarity": "epic",
    "price": 5500,
    "damage": 185,
    "crit_chance_bonus": 10,
    "crit_damage_bonus": 0.8},

"Fatebreaker": {
    "name": "Fatebreaker",
    "category": "Greatsword",
    "rarity": "mythical",
    "price": 9500,
    "damage": 230,
    "crit_chance_bonus": 13,
    "crit_damage_bonus": 1.0},

"Heaven's Ruin": {
    "name": "Heaven's Ruin",
    "category": "Greatsword",
    "rarity": "mythical",
    "price": 12000,
    "damage": 260,
    "crit_chance_bonus": 15,
    "crit_damage_bonus": 1.1},

"Worldsplitter": {
    "name": "Worldsplitter",
    "category": "Greatsword",
    "rarity": "legendary",
    "price": 20000,
    "damage": 350,
    "crit_chance_bonus": 18,
    "crit_damage_bonus": 1.3},

"Godslayer": {
    "name": "Godslayer",
    "category": "Greatsword",
    "rarity": "legendary",
    "price": 28000,
    "damage": 420,
    "crit_chance_bonus": 20,
    "crit_damage_bonus": 1.5},

    #AXES 

"Woodcutter's Axe": {
    "name": "Woodcutter's Axe",
    "category": "Axe",
    "rarity": "common",
    "price": 110,
    "damage": 28,
    "crit_chance_bonus": 0.5,
    "crit_damage_bonus": 0.0},

"Iron Cleaver": {
    "name": "Iron Cleaver",
    "category": "Axe",
    "rarity": "uncommon",
    "price": 280,
    "damage": 45,
    "crit_chance_bonus": 2,
    "crit_damage_bonus": 0.3},

"Bloodaxe": {
    "name": "Bloodaxe",
    "category": "Axe",
    "rarity": "rare",
    "price": 850,
    "damage": 72,
    "crit_chance_bonus": 4,
    "crit_damage_bonus": 0.4},

"Stormcleaver": {
    "name": "Stormcleaver",
    "category": "Axe",
    "rarity": "super_rare",
    "price": 1700,
    "damage": 110,
    "crit_chance_bonus": 5,
    "crit_damage_bonus": 0.6},

"Dragonbone Axe": {
    "name": "Dragonbone Axe",
    "category": "Axe",
    "rarity": "epic",
    "price": 3900,
    "damage": 165,
    "crit_chance_bonus": 7,
    "crit_damage_bonus": 0.8},

"Infernal Reaver": {
    "name": "Infernal Reaver",
    "category": "Axe",
    "rarity": "epic",
    "price": 5200,
    "damage": 195,
    "crit_chance_bonus": 9,
    "crit_damage_bonus": 0.9},

"Worldbreaker Axe": {
    "name": "Worldbreaker Axe",
    "category": "Axe",
    "rarity": "mythical",
    "price": 9000,
    "damage": 245,
    "crit_chance_bonus": 12,
    "crit_damage_bonus": 1.0},

"Ragnarok": {
    "name": "Ragnarok",
    "category": "Axe",
    "rarity": "mythical",
    "price": 12000,
    "damage": 275,
    "crit_chance_bonus": 14,
    "crit_damage_bonus": 1.2},

"Apocalypse Cleaver": {
    "name": "Apocalypse Cleaver",
    "category": "Axe",
    "rarity": "legendary",
    "price": 20000,
    "damage": 360,
    "crit_chance_bonus": 17,
    "crit_damage_bonus": 1.4},

" Leviathan Axe": {
    "name": " Leviathan Axe",
    "category": "Axe",
    "rarity": "legendary",
    "price": 27000,
    "damage": 430,
    "crit_chance_bonus": 19,
    "crit_damage_bonus": 1.6},

    # BLUNT WEAPON

"Training Mace": {
    "name": "Training Mace",
    "category": "Blunt",
    "rarity": "common",
    "price": 90,
    "damage": 23,
    "crit_chance_bonus": 0.5,
    "crit_damage_bonus": 0.0},

"Iron Warhammer": {
    "name": "Iron Warhammer",
    "category": "Blunt",
    "rarity": "uncommon",
    "price": 260,
    "damage": 40,
    "crit_chance_bonus": 2,
    "crit_damage_bonus": 0.3},

"Skullcrusher": {
    "name": "Skullcrusher",
    "category": "Blunt",
    "rarity": "rare",
    "price": 800,
    "damage": 68,
    "crit_chance_bonus": 4,
    "crit_damage_bonus": 0.4},

"Earthshaker": {
    "name": "Earthshaker",
    "category": "Blunt",
    "rarity": "super_rare",
    "price": 1600,
    "damage": 100,
    "crit_chance_bonus": 5,
    "crit_damage_bonus": 0.6},

"Titan Hammer": {
    "name": "Titan Hammer",
    "category": "Blunt",
    "rarity": "epic",
    "price": 3800,
    "damage": 150,
    "crit_chance_bonus": 7,
    "crit_damage_bonus": 0.8},

"Mountain Breaker": {
    "name": "Mountain Breaker",
    "category": "Blunt",
    "rarity": "epic",
    "price": 5200,
    "damage": 185,
    "crit_chance_bonus": 9,
    "crit_damage_bonus": 0.9},

"Colossus Hammer": {
    "name": "Colossus Hammer",
    "category": "Blunt",
    "rarity": "mythical",
    "price": 9000,
    "damage": 235,
    "crit_chance_bonus": 11,
    "crit_damage_bonus": 1.0},

"Starfall Mace": {
    "name": "Starfall Mace",
    "category": "Blunt",
    "rarity": "mythical",
    "price": 11500,
    "damage": 270,
    "crit_chance_bonus": 13,
    "crit_damage_bonus": 1.2},

"Worldbreaker Hammer": {
    "name": "Worldbreaker Hammer",
    "category": "Blunt",
    "rarity": "legendary",
    "price": 19000,
    "damage": 350,
    "crit_chance_bonus": 16,
    "crit_damage_bonus": 1.4},

"Judgment of the Gods": {
    "name": "Judgment of the Gods",
    "category": "Blunt",
    "rarity": "legendary",
    "price": 26000,
    "damage": 420,
    "crit_chance_bonus": 18,
    "crit_damage_bonus": 1.6},

    #SPEARS

"Hunter's Spear": {
    "name": "Hunter's Spear",
    "category": "Spear",
    "rarity": "common",
    "price": 100,
    "damage": 24,
    "crit_chance_bonus": 1,
    "crit_damage_bonus": 0.0},

"Iron Lance": {
    "name": "Iron Lance",
    "category": "Spear",
    "rarity": "uncommon",
    "price": 270,
    "damage": 40,
    "crit_chance_bonus": 3,
    "crit_damage_bonus": 0.3},

"Silver Pike": {
    "name": "Silver Pike",
    "category": "Spear",
    "rarity": "rare",
    "price": 850,
    "damage": 65,
    "crit_chance_bonus": 5,
    "crit_damage_bonus": 0.4},

"Thunder Lance": {
    "name": "Thunder Lance",
    "category": "Spear",
    "rarity": "super_rare",
    "price": 1700,
    "damage": 100,
    "crit_chance_bonus": 7,
    "crit_damage_bonus": 0.5},

"Dragonpiercer": {
    "name": "Dragonpiercer",
    "category": "Spear",
    "rarity": "epic",
    "price": 3900,
    "damage": 150,
    "crit_chance_bonus": 9,
    "crit_damage_bonus": 0.7},

"Storm Pike": {
    "name": "Storm Pike",
    "category": "Spear",
    "rarity": "epic",
    "price": 5200,
    "damage": 180,
    "crit_chance_bonus": 11,
    "crit_damage_bonus": 0.8},

"Heaven's Spear": {
    "name": "Heaven's Spear",
    "category": "Spear",
    "rarity": "mythical",
    "price": 9000,
    "damage": 225,
    "crit_chance_bonus": 14,
    "crit_damage_bonus": 1.0},

"Divine Lance": {
    "name": "Divine Lance",
    "category": "Spear",
    "rarity": "mythical",
    "price": 11500,
    "damage": 255,
    "crit_chance_bonus": 16,
    "crit_damage_bonus": 1.1},

"Celestial Piercer": {
    "name": "Celestial Piercer",
    "category": "Spear",
    "rarity": "legendary",
    "price": 19500,
    "damage": 340,
    "crit_chance_bonus": 19,
    "crit_damage_bonus": 1.3},

"Spear of Eternity": {
    "name": "Spear of Eternity",
    "category": "Spear",
    "rarity": "legendary",
    "price": 26000,
    "damage": 410,
    "crit_chance_bonus": 21,
    "crit_damage_bonus": 1.5},

    # BOWS 

"Hunters Bow": {
    "name": "Hunters Bow",
    "category": "Bow",
    "rarity": "common",
    "price": 100,
    "damage": 22,
    "crit_chance_bonus": 2,
    "crit_damage_bonus": 0.0},

"Adventurer's Bow": {
    "name": "Adventurer's Bow",
    "category": "Bow",
    "rarity": "uncommon",
    "price": 260,
    "damage": 36,
    "crit_chance_bonus": 4,
    "crit_damage_bonus": 0.3},

"Silverwind Bow": {
    "name": "Silverwind Bow",
    "category": "Bow",
    "rarity": "rare",
    "price": 850,
    "damage": 58,
    "crit_chance_bonus": 7,
    "crit_damage_bonus": 0.4
},

"Stormpiercer": {
    "name": "Stormpiercer",
    "category": "Bow",
    "rarity": "super_rare",
    "price": 1700,
    "damage": 90,
    "crit_chance_bonus": 10,
    "crit_damage_bonus": 0.6
},

"Dragonwind Bow": {
    "name": "Dragonwind Bow",
    "category": "Bow",
    "rarity": "epic",
    "price": 3800,
    "damage": 135,
    "crit_chance_bonus": 13,
    "crit_damage_bonus": 0.8
},

"Moonshadow Bow": {
    "name": "Moonshadow Bow",
    "category": "Bow",
    "rarity": "epic",
    "price": 5000,
    "damage": 160,
    "crit_chance_bonus": 15,
    "crit_damage_bonus": 0.9
},

"Heaven's Bow": {
    "name": "Heaven's Bow",
    "category": "Bow",
    "rarity": "mythical",
    "price": 9000,
    "damage": 200,
    "crit_chance_bonus": 18,
    "crit_damage_bonus": 1.0
},

"Celestial Longbow": {
    "name": "Celestial Longbow",
    "category": "Bow",
    "rarity": "mythical",
    "price": 11500,
    "damage": 230,
    "crit_chance_bonus": 21,
    "crit_damage_bonus": 1.2
},

"Worldtree Bow": {
    "name": "Worldtree Bow",
    "category": "Bow",
    "rarity": "legendary",
    "price": 19500,
    "damage": 320,
    "crit_chance_bonus": 24,
    "crit_damage_bonus": 1.4
},

"Bow of the Divine Hunt": {
    "name": "Bow of the Divine Hunt",
    "category": "Bow",
    "rarity": "legendary",
    "price": 26000,
    "damage": 390,
    "crit_chance_bonus": 27,
    "crit_damage_bonus": 1.6},

    # CROSSBOW

"Wooden Crossbow": {
    "name": "Wooden Crossbow",
    "category": "Crossbow",
    "rarity": "common",
    "price": 110,
    "damage": 28,
    "crit_chance_bonus": 1,
    "crit_damage_bonus": 0.0
},

"Iron Repeater": {
    "name": "Iron Repeater",
    "category": "Crossbow",
    "rarity": "uncommon",
    "price": 280,
    "damage": 45,
    "crit_chance_bonus": 3,
    "crit_damage_bonus": 0.3
},

"Silverbolt": {
    "name": "Silverbolt",
    "category": "Crossbow",
    "rarity": "rare",
    "price": 850,
    "damage": 70,
    "crit_chance_bonus": 5,
    "crit_damage_bonus": 0.4
},

"Storm Repeater": {
    "name": "Storm Repeater",
    "category": "Crossbow",
    "rarity": "super_rare",
    "price": 1700,
    "damage": 105,
    "crit_chance_bonus": 7,
    "crit_damage_bonus": 0.6
},

"Dragonfire Crossbow": {
    "name": "Dragonfire Crossbow",
    "category": "Crossbow",
    "rarity": "epic",
    "price": 3900,
    "damage": 155,
    "crit_chance_bonus": 9,
    "crit_damage_bonus": 0.8
},

"Executioner Crossbow": {
    "name": "Executioner Crossbow",
    "category": "Crossbow",
    "rarity": "epic",
    "price": 5200,
    "damage": 185,
    "crit_chance_bonus": 11,
    "crit_damage_bonus": 0.9
},

"Void Repeater": {
    "name": "Void Repeater",
    "category": "Crossbow",
    "rarity": "mythical",
    "price": 9000,
    "damage": 230,
    "crit_chance_bonus": 14,
    "crit_damage_bonus": 1.0
},

"Starfall Crossbow": {
    "name": "Starfall Crossbow",
    "category": "Crossbow",
    "rarity": "mythical",
    "price": 11500,
    "damage": 265,
    "crit_chance_bonus": 16,
    "crit_damage_bonus": 1.2
},

"Apocalypse Repeater": {
    "name": "Apocalypse Repeater",
    "category": "Crossbow",
    "rarity": "legendary",
    "price": 19500,
    "damage": 350,
    "crit_chance_bonus": 19,
    "crit_damage_bonus": 1.4
},

"Judgment Crossbow": {
    "name": "Judgment Crossbow",
    "category": "Crossbow",
    "rarity": "legendary",
    "price": 26000,
    "damage": 420,
    "crit_chance_bonus": 21,
    "crit_damage_bonus": 1.6},}

armor = {

    # COMMON

    "Leather Armor": {
        "name": "Leather Armor",
        "category": "Leather",
        "rarity": "Common",
        "price": 100,
        "defense": 10,
        "hp_bonus": 30,
        "mp_bonus": 0,
        "speed_bonus": 2,
        "crit_chance_bonus": 1,
        "crit_damage_bonus": 0.0},

    "Iron Chainmail": {
        "name": "Iron Chainmail",
        "category": "Chainmail",
        "rarity": "Common",
        "price": 130,
        "defense": 15,
        "hp_bonus": 40,
        "mp_bonus": 0,
        "speed_bonus": 0,
        "crit_chance_bonus": 0,
        "crit_damage_bonus": 0.0},
    # UNCOMMON

    "Hunter's Leather": {
        "name": "Hunter's Leather",
        "category": "Leather",
        "rarity": "Uncommon",
        "price": 300,
        "defense": 22,
        "hp_bonus": 60,
        "mp_bonus": 0,
        "speed_bonus": 4,
        "crit_chance_bonus": 2,
        "crit_damage_bonus": 0.1
    },

    "Reinforced Chainmail": {
        "name": "Reinforced Chainmail",
        "category": "Chainmail",
        "rarity": "Uncommon",
        "price": 350,
        "defense": 28,
        "hp_bonus": 80,
        "mp_bonus": 0,
        "speed_bonus": 0,
        "crit_chance_bonus": 0,
        "crit_damage_bonus": 0.1
    },

    # RARE

    "Shadowstalker Armor": {
        "name": "Shadowstalker Armor",
        "category": "Assassin Armor",
        "rarity": "Rare",
        "price": 900,
        "defense": 35,
        "hp_bonus": 100,
        "mp_bonus": 20,
        "speed_bonus": 7,
        "crit_chance_bonus": 5,
        "crit_damage_bonus": 0.2},

    "Arcane Robes": {
        "name": "Arcane Robes",
        "category": "Mage Robe",
        "rarity": "Rare",
        "price": 950,
        "defense": 20,
        "hp_bonus": 60,
        "mp_bonus": 120,
        "speed_bonus": 2,
        "crit_chance_bonus": 3,
        "crit_damage_bonus": 0.3},

    # SUPER RARE

    "Royal Templar Armor": {
        "name": "Royal Templar Armor",
        "category": "Paladin Armor",
        "rarity": "Super Rare",
        "price": 2000,
        "defense": 65,
        "hp_bonus": 180,
        "mp_bonus": 30,
        "speed_bonus": -1,
        "crit_chance_bonus": 2,
        "crit_damage_bonus": 0.2},

    "Storm Ranger Armor": {
        "name": "Storm Ranger Armor",
        "category": "Archer Armor",
        "rarity": "Super Rare",
        "price": 2200,
        "defense": 45,
        "hp_bonus": 120,
        "mp_bonus": 40,
        "speed_bonus": 10,
        "crit_chance_bonus": 7,
        "crit_damage_bonus": 0.3},

    # EPIC

    "Dragonbone Armor": {
        "name": "Dragonbone Armor",
        "category": "Dragon Armor",
        "rarity": "Epic",
        "price": 5000,
        "defense": 100,
        "hp_bonus": 300,
        "mp_bonus": 50,
        "speed_bonus": 0,
        "crit_chance_bonus": 3,
        "crit_damage_bonus": 0.4},

    "Berserker Warplate": {
        "name": "Berserker Warplate",
        "category": "Berserker Armor",
        "rarity": "Epic",
        "price": 5500,
        "defense": 75,
        "hp_bonus": 350,
        "mp_bonus": 0,
        "speed_bonus": 4,
        "crit_chance_bonus": 5,
        "crit_damage_bonus": 0.7},

    # MYTHICAL

    "Demonforged Armor": {
        "name": "Demonforged Armor",
        "category": "Demon Armor",
        "rarity": "Mythical",
        "price": 12000,
        "defense": 140,
        "hp_bonus": 450,
        "mp_bonus": 100,
        "speed_bonus": 5,
        "crit_chance_bonus": 8,
        "crit_damage_bonus": 0.8},

    "Celestial Raiment": {
        "name": "Celestial Raiment",
        "category": "Divine Armor",
        "rarity": "Mythical",
        "price": 14000,
        "defense": 125,
        "hp_bonus": 350,
        "mp_bonus": 250,
        "speed_bonus": 7,
        "crit_chance_bonus": 7,
        "crit_damage_bonus": 1.0},

    # LEGENDARY

    "Ancient Guardian Armor": {
        "name": "Ancient Guardian Armor",
        "category": "Heavy Armor",
        "rarity": "Legendary",
        "price": 25000,
        "defense": 220,
        "hp_bonus": 700,
        "mp_bonus": 100,
        "speed_bonus": -2,
        "crit_chance_bonus": 5,
        "crit_damage_bonus": 0.8},

    "Divine Aegis": {
        "name": "Divine Aegis",
        "category": "Divine Armor",
        "rarity": "Legendary",
        "price": 30000,
        "defense": 200,
        "hp_bonus": 600,
        "mp_bonus": 300,
        "speed_bonus": 10,
        "crit_chance_bonus": 10,
        "crit_damage_bonus": 1.2}}

accessories = {

    # COMMON

    "Copper Ring": {
        "name": "Copper Ring",
        "category": "Ring",
        "rarity": "Common",
        "price": 80,
        "attack_bonus": 2,
        "defense_bonus": 0,
        "speed_bonus": 0,
        "crit_chance_bonus": 1,
        "crit_damage_bonus": 0.0,
        "hp_bonus": 0,
        "mp_bonus": 0},

    "Apprentice Pendant": {
        "name": "Apprentice Pendant",
        "category": "Necklace",
        "rarity": "Common",
        "price": 100,
        "attack_bonus": 0,
        "defense_bonus": 2,
        "speed_bonus": 0,
        "crit_chance_bonus": 0,
        "crit_damage_bonus": 0.0,
        "hp_bonus": 30,
        "mp_bonus": 20},

    # UNCOMMON

    "Hunter's Bracelet": {
        "name": "Hunter's Bracelet",
        "category": "Bracelet",
        "rarity": "Uncommon",
        "price": 250,
        "attack_bonus": 5,
        "defense_bonus": 2,
        "speed_bonus": 3,
        "crit_chance_bonus": 2,
        "crit_damage_bonus": 0.1,
        "hp_bonus": 20,
        "mp_bonus": 0},

    "Swiftwind Boots": {
        "name": "Swiftwind Boots",
        "category": "Boots",
        "rarity": "Uncommon",
        "price": 300,
        "attack_bonus": 0,
        "defense_bonus": 3,
        "speed_bonus": 6,
        "crit_chance_bonus": 1,
        "crit_damage_bonus": 0.0,
        "hp_bonus": 20,
        "mp_bonus": 10},

    # RARE

    "Shadow Fang Ring": {
        "name": "Shadow Fang Ring",
        "category": "Ring",
        "rarity": "Rare",
        "price": 900,
        "attack_bonus": 8,
        "defense_bonus": 2,
        "speed_bonus": 5,
        "crit_chance_bonus": 5,
        "crit_damage_bonus": 0.3,
        "hp_bonus": 30,
        "mp_bonus": 0},

    "Arcane Crystal": {
        "name": "Arcane Crystal",
        "category": "Amulet",
        "rarity": "Rare",
        "price": 1000,
        "attack_bonus": 4,
        "defense_bonus": 3,
        "speed_bonus": 2,
        "crit_chance_bonus": 3,
        "crit_damage_bonus": 0.4,
        "hp_bonus": 50,
        "mp_bonus": 100},

    # SUPER RARE

    "Royal Templar Emblem": {
        "name": "Royal Templar Emblem",
        "category": "Amulet",
        "rarity": "Super Rare",
        "price": 2200,
        "attack_bonus": 10,
        "defense_bonus": 12,
        "speed_bonus": 2,
        "crit_chance_bonus": 3,
        "crit_damage_bonus": 0.3,
        "hp_bonus": 120,
        "mp_bonus": 50},

    "Stormrunner Bracelet": {
        "name": "Stormrunner Bracelet",
        "category": "Bracelet",
        "rarity": "Super Rare",
        "price": 2400,
        "attack_bonus": 12,
        "defense_bonus": 3,
        "speed_bonus": 10,
        "crit_chance_bonus": 6,
        "crit_damage_bonus": 0.4,
        "hp_bonus": 50,
        "mp_bonus": 40},

    # EPIC

    "Dragonheart Ring": {
        "name": "Dragonheart Ring",
        "category": "Ring",
        "rarity": "Epic",
        "price": 5000,
        "attack_bonus": 20,
        "defense_bonus": 10,
        "speed_bonus": 4,
        "crit_chance_bonus": 7,
        "crit_damage_bonus": 0.6,
        "hp_bonus": 200,
        "mp_bonus": 80},

    "Berserker's Core": {
        "name": "Berserker's Core",
        "category": "Amulet",
        "rarity": "Epic",
        "price": 5500,
        "attack_bonus": 30,
        "defense_bonus": 5,
        "speed_bonus": 5,
        "crit_chance_bonus": 6,
        "crit_damage_bonus": 0.8,
        "hp_bonus": 250,
        "mp_bonus": 20},

    # MYTHICAL

    "Demon King's Sigil": {
        "name": "Demon King's Sigil",
        "category": "Amulet",
        "rarity": "Mythical",
        "price": 12000,
        "attack_bonus": 45,
        "defense_bonus": 20,
        "speed_bonus": 8,
        "crit_chance_bonus": 10,
        "crit_damage_bonus": 1.0,
        "hp_bonus": 400,
        "mp_bonus": 150},

    "Celestial Tear": {
        "name": "Celestial Tear",
        "category": "Pendant",
        "rarity": "Mythical",
        "price": 14000,
        "attack_bonus": 25,
        "defense_bonus": 25,
        "speed_bonus": 10,
        "crit_chance_bonus": 8,
        "crit_damage_bonus": 1.1,
        "hp_bonus": 300,
        "mp_bonus": 300},

    # LEGENDARY

    "Ring of the Ancient Dragon": {
        "name": "Ring of the Ancient Dragon",
        "category": "Ring",
        "rarity": "Legendary",
        "price": 25000,
        "attack_bonus": 70,
        "defense_bonus": 40,
        "speed_bonus": 10,
        "crit_chance_bonus": 12,
        "crit_damage_bonus": 1.3,
        "hp_bonus": 600,
        "mp_bonus": 250},

    "Godslayer's Relic": {
        "name": "Godslayer's Relic",
        "category": "Relic",
        "rarity": "Legendary",
        "price": 30000,
        "attack_bonus": 90,
        "defense_bonus": 35,
        "speed_bonus": 15,
        "crit_chance_bonus": 15,
        "crit_damage_bonus": 1.5,
        "hp_bonus": 500,
        "mp_bonus": 400}}