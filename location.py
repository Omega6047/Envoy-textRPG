class area():
    def __init__(self, name, local_fauna_day,local_fauna_night, local_flora_day, local_flora_night, local_junk, local_material,
                 connect_location, special_fauna_day, special_fauna_night, special_chance_day, special_chance_night, local_NPC,
                 search_chance):
        self.name = name
        self.local_fauna_day = local_fauna_day
        self.local_fauna_night = local_fauna_night
        self.local_flora_day = local_flora_day
        self.local_flora_night = local_flora_night
        self.local_junk = local_junk
        self.local_material = local_material
        self.connect_location = connect_location
        self.special_fauna_day = special_fauna_day
        self.special_fauna_night = special_fauna_night
        self.special_chance_day = special_chance_day
        self.special_chance_night = special_chance_night
        self.local_NPC = local_NPC
        self.search_chance = search_chance

rovok_forest_entrance = area(
    "Rovok Forest - Entrance",                  #name
    "Boar-Meatbug-Isondu",                      #local fauna day
    "Night Flame-Goblin Scout",                 #local fauna night
    "Weed-Daybloom-Blue Moss",                 #local flora day
    "Weed-Nightbloom-Blue Moss",                #local flora night
    "Pebble-Branch-Metal Scrap",                #local junk
    "Crystal Fragment",                         #local material
    "rovok_depth_001",                          #connected locations
    "Puk-Alpha Wolf",                           #special fauna day
    "Werewolf-Hobgoblin",                       #special fauna night
    5,                                          #special chance day
    10,                                         #special chance night
    "TestPC",                                   #local NPCs
    85,                                         #search chance
)
rovok_forest_depth = area(
    "Rovok Forest - Depth",                     #name
    "Wolf-Boar-Meatbug-Isondu-Python",          #local fauna day
    "Night Flame-Goblin Scout-Goblin Warrior",  #local fauna night
    "Weed-Daybloom-Blue Moss",                  #local flora day
    "Weed-Nightbloom-Blue Moss",                #local flora night
    "Pebble-Branch-Metal Junk",                 #local junk
    "Crystal Fragment",                         #local material
    "rovok_entrance_000",                       #connected locations
    "Ent",                                      #special fauna day
    "Werewolf-Hobgoblin",                       #special fauna night
    10,                                         #special chance day
    15,                                         #special chance night
    "",                                         #local NPCs
    70,                                         #search chance
)

instance = {
    "rovok_entrance_000": rovok_forest_entrance,
    "rovok_depth_001": rovok_forest_depth,
}
