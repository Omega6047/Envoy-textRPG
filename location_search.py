class search_flags:
    level_vert = 1
def find_random():
    return "find_random"

###########################################################################################################

def find_set_000_01():
    if search_flags.level_vert < 1:
        return "find_set|Branch-Pebble"
    else:
        return "nothing"
def find_set_000_02():
    if search_flags.level_vert < 1:
        return "find_set|Metal Scrap"
    else:
        return "nothing"

###########################################################################################################

rovok_forest_entrance = [
    find_random,
    #find_set_000_01,
    #find_set_000_02,
]
rovok_forest_depth = [

]

instance = {
    "rovok_entrance_000": rovok_forest_entrance,
    "rovok_depth_001": rovok_forest_depth,
}