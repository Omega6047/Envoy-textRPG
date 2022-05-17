class mob():
    def __init__(self, lvl, str, bld, mgi, tch, agi, end, type, skills, HP, price, drop):
        self.lvl = lvl
        self.str = str
        self.bld = bld
        self.mgi = mgi
        self.tch = tch
        self.agi = agi
        self.end = end
        self.type = type
        self.skills = skills
        self.HP = HP
        self.price = price
        self.drop = drop
class mob_special():
    def __init__(self, lvl, str, bld, mgi, tch, agi, end, type, skills, HP, price, drop, minions):
        self.lvl = lvl
        self.str = str
        self.bld = bld
        self.mgi = mgi
        self.tch = tch
        self.agi = agi
        self.end = end
        self.type = type
        self.skills = skills
        self.HP = HP
        self.price = price
        self.drop = drop
        self.minions = minions

meatbug_20000 = mob(
    1,                                              #lvl
    1,                                              #str
    1,                                              #bld
    0,                                              #mgi
    0,                                              #tch
    1,                                              #agi
    1,                                              #end
    "bug",                                          #type
    "Nib",                                         #skills
    1,                                              #HP
    0,                                              #price
    "Bug Shell",                                    #drop
)

wolf_20100 = mob(
    3,                                              #lvl
    4,                                              #str
    2,                                              #bld
    0,                                              #mgi
    0,                                              #tch
    4,                                              #agi
    5,                                              #end
    "canine",                                       #type
    "Bite-Swipe",                                   #skills
    5,                                              #HP
    3,                                              #price
    "Wolf Fur-Wolf Fang",                           #drop
)
wolf_alpha_20101 = mob_special(
    7,                                              #lvl
    5,                                              #str
    2,                                              #bld
    0,                                              #mgi
    0,                                              #tch
    8,                                              #agi
    6,                                              #end
    "boss",                                         #type
    "Bite-Swipe-Howl",                              #skills
    9,                                              #HP
    6,                                              #price
    "Wolf Fur-Wolf Fang-Alpha Wolf's Paw",          #drop
    "Wolf"                                          #minions
)
werewolf_20101 = mob_special(
    15,                                             #lvl
    12,                                             #str
    7,                                              #bld
    0,                                              #mgi
    0,                                              #tch
    7,                                              #agi
    6,                                              #end
    "boss",                                         #type
    "Bite-Swipe-Howl",                              #skills
    16,                                             #HP
    35,                                             #price
    "Werewolf Blood-Cursed Mana Crystal",           #drop
    "Wolf"                                          #minions
)
boar_20200 = mob(
    2,                                              #lvl
    3,                                              #str
    5,                                              #bld
    0,                                              #mgi
    0,                                              #tch
    1,                                              #agi
    4,                                              #end
    "feral_neutral",                                        #type
    "Charge",                                       #skills
    3,                                              #HP
    2,                                              #price
    "Boar Fur-Boar Tusk",                           #drop
)
python_20201 = mob(
    3,                                              #lvl
    5,                                              #str
    6,                                              #bld
    0,                                              #mgi
    0,                                              #tch
    1,                                              #agi
    4,                                              #end
    "feral_predator",                                        #type
    "Choke-Swipe",                                  #skills
    4,                                              #HP
    2,                                              #price
    "Snake Skin-Snake Egg",                         #drop
)
isondu_20300 = mob(
    3,                                              #lvl
    2,                                              #str
    2,                                              #bld
    4,                                              #mgi
    0,                                              #tch
    5,                                              #agi
    2,                                              #end
    "fairy",                                        #type
    "Burn-Shine-Beam",                              #skills
    2,                                              #HP
    2,                                              #price
    "Fire Mana Crystal-Light Ashes",                #drop
)
nightflame_20301 = mob(
    4,                                              #lvl
    2,                                              #str
    3,                                              #bld
    6,                                              #mgi
    0,                                              #tch
    2,                                              #agi
    4,                                              #end
    "fairy",                                        #type
    "Burn-Darkflame Curse-Beam",                    #skills
    4,                                              #HP
    4,                                              #price
    "Dark Mana Crystal-Black Ashes",               #drop
)
goblin_scout_20400 = mob(
    4,                                              #lvl
    3,                                              #str
    2,                                              #bld
    0,                                              #mgi
    0,                                              #tch
    5,                                              #agi
    4,                                              #end
    "goblin",                                       #type
    "Swipe-Strike",                                 #skills
    3,                                              #HP
    5,                                              #price
    "Wooden Torch-Coin Pouch-Goblin Blood",         #drop
)
goblin_warrior_20401 = mob(
    5,                                              #lvl
    5,                                              #str
    4,                                              #bld
    0,                                              #mgi
    0,                                              #tch
    4,                                              #agi
    5,                                              #end
    "goblin",                                       #type
    "Swipe-Strike",                                 #skills
    5,                                              #HP
    7,                                              #price
    "Goblin blood-Rusty Equipment",                 #drop
)
hobgoblin_20402 = mob_special(
    8,                                              #lvl
    7,                                              #str
    6,                                              #bld
    0,                                              #mgi
    0,                                              #tch
    2,                                              #agi
    6,                                              #end
    "boss",                                         #type
    "Swipe-Strike-Crush",                           #skills
    9,                                              #HP
    17,                                             #price
    "Hob's Heart-Goblin Blood",                     #drop
    "Goblin Scout-Goblin Warrior"                   #minions
)
puk_20500 = mob_special(
    9,                                              #lvl
    3,                                              #str
    5,                                              #bld
    8,                                              #mgi
    0,                                              #tch
    4,                                              #agi
    5,                                              #end
    "boss",                                         #type
    "Trick-Forest Breath",                          #skills  --
    7,                                              #HP
    18,                                             #price
    "Wind Mana Crystal-Puk's Staff",                #drop --
    "Isondu"                                        #minions
)
ent_20600 = mob_special(
    25,                                             #lvl
    18,                                             #str
    20,                                             #bld
    15,                                             #mgi
    0,                                              #tch
    0,                                              #agi
    0,                                              #end
    "boss",                                         #type
    "Strike-Ivy Wip",                               #skills
    20,                                             #HP
    50,                                             #price
    "Ent's Branch-Ent's Sap",                       #drop
    "Night Flame"                                   #minions
)

###########################################################################################################

mobs = {
    "Meatbug": meatbug_20000,
    "Wolf": wolf_20100,
    "Alpha Wolf": wolf_alpha_20101,
    "Werewolf": werewolf_20101,
    "Boar": boar_20200,
    "Isondu": isondu_20300,
    "Night Flame": nightflame_20301,
    "Goblin Scout": goblin_scout_20400,
    "Goblin Warrior": goblin_warrior_20401,
    "Hobgoblin": hobgoblin_20402,
    "Python": python_20201,
    "Puk": puk_20500,
    "Ent": ent_20600,
    }
