class item():
    def __init__(self,name, description, type, price, drop_chance):
        self.name = name
        self.description = description
        self.type = type
        self.price = price
        self.drop_chance = drop_chance

###########################################################################################################
###  PLANTS  ##############################################################################################
###########################################################################################################

itfl_weed = item(
    "Weed",                                                                                         #name
    "Just some weed. You can burn it, but you shouldn't. Only villans do that.",                    #description
    "junk",                                                                                         #type
    0,                                                                                              #price
    100,                                                                                            #drop chance
)
itfl_daybloom = item(
    "Daybloom",                                                                                     #name
    "Common flower that blooms in well lit places. It makes for a decent tea.",                     #description
    "tea",                                                                                          #type
    1,                                                                                              #price
    100,                                                                                            #drop chance
)
itfl_nightbloom = item(
    "Nightbloom",                                                                                   #name
    "Common flower that blooms during the night. It makes for a decent tea.",                       #description
    "tea",                                                                                          #type
    1,                                                                                              #price
    100,                                                                                            #drop chance
)
itfl_bluemoss = item(
    "Blue Moss",                                                                                    #name
    "Type of moss that grows on rocks; has magic properties. Some say dead people turn into it.",   #description
    "moss",                                                                                         #type
    1,                                                                                              #price
    100,                                                                                            #drop chance
)


###########################################################################################################
###  JUNK  ################################################################################################
###########################################################################################################

itmi_pebble = item(
    "Pebble",                                                                                       #name
    "Literally a rock picked up from the ground. You can shove it up your...",                      #description
    "junk",                                                                                         #type
    0,                                                                                              #price
    100,                                                                                            #drop chance
)
itmi_metalscrap = item(
    "Metal Scrap",                                                                                  #name
    "A collection of verious metal parts. Some of those can still be of use if processed properly.",#description
    "junk",                                                                                         #type
    0,                                                                                              #price
    100,                                                                                            #drop chance
)
itmi_branch = item(
    "Branch",                                                                                       #name
    "A branch. Nothing special about it but you can start a campfire with it.",                     #description
    "junk",                                                                                         #type
    0,                                                                                              #price
    100,                                                                                            #drop chance
)
itmi_rustyequipment = item(
    "Rusty Equipment",                                                                              #name
    "A branch. Nothing special about it but you can start a campfire with it.",                     #description
    "junk",                                                                                         #type
    0,                                                                                              #price
    100,                                                                                             #drop chance
)


###########################################################################################################
###  MATERIALS  ###########################################################################################
###########################################################################################################

itma_bugshell = item(
    "Bug Shell",                                                                                    #name
    "Shell broken off a Meatbug. It's surprisingly resiliant to the enviromental conditions.",      #description
    "bone",                                                                                         #type
    1,                                                                                              #price
    25,                                                                                             #drop chance
)
itma_wolffur = item(
    "Wolf Fur",                                                                                     #name
    "Fur torn off a wolf. Some people might pay a good price for it.",                              #description
    "fur",                                                                                          #type
    3,                                                                                              #price
    20,                                                                                             #drop chance
)
itma_wereblood = item(
    "Werewolf Blood",                                                                               #name
    "An ounce of werewolf blood. It was once a human's blood but now holds a curse within it.",     #description
    "blood",                                                                                        #type
    8,                                                                                              #price
    25,                                                                                             #drop chance
)
itma_cursemana = item(
    "Cursed Mana Crystal",                                                                          #name
    "Dark mana crystal holding a curse within it. Better don't drop it",                            #description
    "crystal",                                                                                      #type
    15,                                                                                             #price
    5,                                                                                              #drop chance
)
itma_boarfur = item(
    "Boar Fur",                                                                                     #name
    "Thick hide of a boar. It makes for a decent armor material.",                                  #description
    "fur",                                                                                          #type
    2,                                                                                              #price
    25,                                                                                             #drop chance
)
itma_snakeskin = item(
    "Snake Skin",                                                                                    #name
    "Scaley skin of a snake. Some like their purses made of that.",                                  #description
    "fur",                                                                                           #type
    3,                                                                                               #price
    25,                                                                                              #drop chance
)
itma_firemana = item(
    "Fire Mana Crystal",                                                                              #name
    "Fire crystalized within mana. It's hot. Don't keep it near flamable stuff.",                    #description
    "crystal",                                                                                        #type
    15,                                                                                               #price
    3,                                                                                                #drop chance
)
itma_darkmana = item(
    "Dark Mana Crystal",                                                                              #name
    "A crystal that seems to be absorbing the light around it. It wouldn't make for a good lamp.",    #description
    "crystal",                                                                                        #type
    15,                                                                                               #price
    3,                                                                                                #drop chance
)
itma_goblinblood = item(
    "Goblin Blood",                                                                                   #name
    "A bottle of goblin blood. It's corrosive and acidic. Don't drink or put on swords.",             #description
    "blood",                                                                                          #type
    5,                                                                                                #price
    40,                                                                                               #drop chance
)
itma_windmana = item(
    "Wind Mana Crystal",                                                                              #name
    "Wind trapped witing a mana crystal. Don't let go or it will fly off.",                           #description
    "crystal",                                                                                        #type
    15,                                                                                               #price
    20,                                                                                               #drop chance
)
itma_entbranch = item(
    "Ent's Branch",                                                                                   #name
    "Seemingly a normal branch, but it's filled with ent's magic. Best kind of firewood out there",   #description
    "bone",                                                                                           #type
    15,                                                                                               #price
    20,                                                                                               #drop chance
)
itma_entsap = item(
    "Ent's Sap",                                                                                      #name
    "Lifeblood of an ent. Once lit, it can release magic flames for hours.",                          #description
    "bone",                                                                                           #type
    15,                                                                                               #price
    20,                                                                                               #drop chance
)
itma_fragcrystal = item(
    "Crystal Fragment",                                                                                #name
    "A Shattered piece of a crystal. With enough of those, a mana crystal can be created.",            #description
    "crystal",                                                                                         #type
    2,                                                                                                 #price
    100,                                                                                               #drop chance
)
itma_blackash = item(
    "Black Ashes",                                                                                      #name
    "Ashes of a night creature. Good fuel for the fireplace.",                                          #description
    "bone",                                                                                             #type
    4,                                                                                                  #price
    70,                                                                                                 #drop chance
)
itma_lightash = item(
    "Light Ashes",                                                                                      #name
    "Ashes of a light creature. They can easily ignite even in the sunlight..",                         #description
    "bone",                                                                                             #type
    4,                                                                                                  #price
    70,                                                                                                 #drop chance
)

###########################################################################################################
###  USABLES  #############################################################################################
###########################################################################################################


itus_woodtorch = item(
    "Wooden Torch",                                                                                 #name
    "Branch with a piece of cloth drenched in flamable sap. Doesn't burn for long.",                #description
    "tool",                                                                                         #type
    1,                                                                                              #price
    50,                                                                                             #drop chance
)
itus_coinpouch = item(
    "Coin Pouch",                                                                                   #name
    "Small pouch filled with coins. Can't tell how many.",                                          #description
    "tool",                                                                                         #type
    0,                                                                                              #price
    50,                                                                                             #drop chance
)


###########################################################################################################
###  TROPHYS  #############################################################################################
###########################################################################################################

ittr_wolffang = item(
    "Wolf Fang",                                                                                       #name
    "Wolf's fang. Still in good condition so it can be used to make a nice trophy.",                   #description
    "enemy trophy",                                                                                   #type
    2,                                                                                                 #price
    35,                                                                                                #drop chance
)
ittr_alphapaw = item(
    "Alpha Wolf's Paw",                                                                                #name
    "Alpha Wolf's Paw. It's large. Almost as big as human fist.",                                      #description
    "enemy trophy",                                                                                   #type
    10,                                                                                                #price
    5,                                                                                                 #drop chance
)
ittr_snakegg = item(
    "Snake Egg",                                                                                       #name
    "It's lika a chicken egg, but there's a small snake inside. Take care of it and it might grow.",    #description
    "enemy trophy",                                                                                   #type
    20,                                                                                                #price
    3,                                                                                                 #drop chance
)
ittr_boartusk = item(
    "Boar Tusk",                                                                                       #name
    "Hard and sturdy tusk. Farmers create makeshift tools using those.",                               #description
    "enemy trophy",                                                                                    #type
    2,                                                                                                 #price
    40,                                                                                                #drop chance
)
ittr_hobhert = item(
    "Hob's Heart",                                                                                     #name
    "Large blob of flesh ripped from a hobgoblin's chest. It carriews magical and alchemical properties.",#description
    "enemy trophy",                                                                                    #type
    20,                                                                                                #price
    10,                                                                                                #drop chance
)
ittr_pukstaff = item(
    "Puk's Staff",                                                                                     #name
    "Long wooden staff imbued with puk's magical powers. Works great as a blunt force weapon.",        #description
    "enemy trophy",                                                                                    #type
    15,                                                                                                #price
    15,                                                                                                #drop chance
)



###########################################################################################################

items_list = {
    "Alpha Wolf's Paw": ittr_alphapaw,
    "Boar Tusk": ittr_boartusk,
    "Hob's Heart": ittr_hobhert,
    "Puk's Staff": ittr_pukstaff,
    "Snake Egg": ittr_alphapaw,
    "Wolf Fang": ittr_wolffang,

    "Coin Pouch": itus_coinpouch,
    "Wooden Torch": itus_woodtorch,

    "Black Ashes": itma_blackash,
    "Boar Fur": itma_boarfur,
    "Bug Shell": itma_bugshell,
    "Crystal Fragment": itma_fragcrystal,
    "Cursed Mana Crystal": itma_cursemana,
    "Dark Mana Crystal": itma_darkmana,
    "Ent's Branch": itma_entbranch,
    "Ent's Sap": itma_entsap,
    "Fire Mana Crystal": itma_firemana,
    "Light Ashes": itma_lightash,
    "Snake Skin": itma_snakeskin,
    "Werewolf Blood": itma_wereblood,
    "Wind Mana Crystal": itma_windmana,
    "Wolf Fur": itma_wolffur,

    "Branch": itmi_branch,
    "Metal Scrap": itmi_metalscrap,
    "Pebble": itmi_pebble,
    "Rusty Equipment": itmi_rustyequipment,

    "Weed": itfl_weed,
    "Daybloom": itfl_daybloom,
    "Nightbloom": itfl_nightbloom,
    "Blue Moss": itfl_bluemoss,
    }

class inventory:
    materials = {
        "Black Ashes": 0,
        "Boar Fur": 0,
        "Boar Tusk": 0,
        "Bug Shell": 0,
        "Crystal Fragment": 0,
        "Cursed Mana Crystal": 0,
        "Dark Mana Crystal": 0,
        "Ent's Branch": 0,
        "Ent's Sap": 0,
        "Fire Mana Crystal": 0,
        "Light Mana Crystal": 0,
        "Goblin Blood": 0,
        "Snake Skin": 0,
        "Werewolf Blood": 0,
        "Wind Mana Crystal": 0,
        "Wolf Fur": 0,
    }
    plants = {
        "Blue Moss": 0,
        "Daybloom": 0,
        "Nightbloom": 0,
        "Weed": 0,
    }
    usables = {
        "Coin Pouch": 0,
        "Wooden Torch": 0,
    }
    trophys = {
        "Alpha Wolf's Paw": 0,
        "Boar Tusk": 0,
        "Hob's Heart": 0,
        "Puk's Staff": 0,
        "Snake Egg": 0,
        "Wolf Fang": 0,
    }
    junk = {
        "Branch": 0,
        "Metal Scrap": 0,
        "Pebble": 0,
        "Rusty Equipment": 0,
    }
    quest = {}