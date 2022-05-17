import datetime
import configparser

class settings:
    res_x = 120
    res_y = 35
    auto_read = 0
    auto_speed = 50
class player:
    story_progress = 0
    part_progress = 0
    fight_progress = 0
    text_progress = 0
    curr_chapter = "Prologue"
    curr_chapter_index = 0
    curr_part = 0
    currant_char = "Vert-Yavin"
    location = "rovok_entrance_000"
    daytime = "day"
    known_flora = ["Weed"]
    known_material = ["Metal Junk"]
    gold = 0
    activity_delay = datetime.datetime.now()
class play_char:
    def __init__(self, lvl, exp, str, bld, mgi, tch, agi, end, skill_p, HP, skills, EP):
        self.lvl = lvl
        self.exp = exp
        self.exp_to_lvl = lvl*1000 + ((lvl-1) * 100)
        self.str = str
        self.bld = bld
        self.mgi = mgi
        self.tch = tch
        self.agi = agi
        self.end = end
        self.skill_p = skill_p
        self.HP = lvl*(10 + HP) + int(self.bld * 1.5)
        self.skills = skills
        self.EP = self.lvl*(5 + EP) + int(self.end * 2.5)

vert_10000 = play_char(
    1,                          #lvl
    0,                          #exp
    3,                         #str
    2,                          #bld
    -5,                         #mgi
    1,                          #tch
    1,                          #agi
    -3,                         #end
    0,                          #skill points
    0,                          #HP
    "Snipe-Bash-Poison_Dart",   #skills
    -1,                         #EP
)
yavin_10001 = play_char(
    1,                          #lvl
    0,                          #exp
    1,                          #str
    -3,                         #bld
    3,                          #mgi
    -5,                         #tch
    1,                          #agi
    2,                          #end
    0,                          #skill points
    -1,                         #HP
    "Knife_Throw-Mordhau-Bolt", #skills
    0,                          #EP
)
char_fight ={
    "Vert": vert_10000,
    "Yavin": yavin_10001
}

def save_game(save_name,state):
    save_file = open(save_name, "w")

    save_file.write("#### PLAYER DATA ####\n")
    save_file.write("\n")
    save_file.write("STORY_PROGRESS:" + str(player.story_progress) + "\n")
    save_file.write("TEXT_PROGRESS:" + str(player.text_progress) + "\n")
    save_file.write("PART_PROGRESS:" + str(player.part_progress) + "\n")
    save_file.write("FIGHT_PROGRESS:" + str(player.fight_progress) + "\n")
    save_file.write("CURRANT_CHARACTER:" + str(player.currant_char) + "\n")
    save_file.write("GAME_STATE:" + str(state) + "\n")
    save_file.write("\n")
    save_file.write("#### CHARACTER DATA ####\n")
    save_file.write("   -VERT-\n")
    save_file.write("LVL:" + str(vert_10000.lvl) + "\n")
    save_file.write("EXP:" + str(vert_10000.exp) + "\n")
    save_file.write("EXP_2_LVL:" + str(vert_10000.exp_to_lvl) + "\n")
    save_file.write("STR:" + str(vert_10000.str) + "\n")
    save_file.write("BLD:" + str(vert_10000.bld) + "\n")
    save_file.write("TCH:" + str(vert_10000.tch) + "\n")
    save_file.write("AGI:" + str(vert_10000.agi) + "\n")
    save_file.write("END:" + str(vert_10000.end) + "\n")
    save_file.write("SKILL_POINTS:" + str(vert_10000.skill_p) + "\n")
    save_file.write("SKILL:" + str(vert_10000.skills) + "\n")
    save_file.write("   -YAVIN-\n")
    save_file.write("LVL:" + str(yavin_10001.lvl) + "\n")
    save_file.write("EXP:" + str(yavin_10001.exp) + "\n")
    save_file.write("EXP_2_LVL:" + str(yavin_10001.exp_to_lvl) + "\n")
    save_file.write("STR:" + str(yavin_10001.str) + "\n")
    save_file.write("BLD:" + str(yavin_10001.bld) + "\n")
    save_file.write("MGI:" + str(yavin_10001.mgi) + "\n")
    save_file.write("AGI:" + str(yavin_10001.agi) + "\n")
    save_file.write("END:" + str(yavin_10001.end) + "\n")
    save_file.write("SKILL:" + str(yavin_10001.skills) + "\n")

    save_file.close()
    print("SAVE COMPLETE")

def load_game():
    pass
def save_settings():
    cfg = configparser.ConfigParser()
    cfg["DISPLAY"] = {
        "res_x": settings.res_x,
        "res_y": settings.res_y
    }
    cfg["GAMEPLAY"] = {
        "auto_read": settings.auto_read,
        "auto_speed": settings.auto_speed
    }
    with open("config.ini", "w") as config:
        cfg.write(config)
def load_settings():
    cfg = configparser.ConfigParser()
    cfg.read("config.ini")
    settings.res_x = cfg["DISPLAY"]['res_x']
    settings.res_y = cfg["DISPLAY"]['res_y']
    settings.auto_read = int(cfg["GAMEPLAY"]['auto_read'])
    settings.auto_speed = int(cfg["GAMEPLAY"]['auto_speed'])
def printsettings():
    size = str(settings.res_x)+'x'+str(settings.res_y)
    print("DISPLAY")
    print("\tWindow size:",size,"\t\t\t\t\t[RESIZE X Y]")
    print("GAMEPLAY")
    if settings.auto_read == 1:
        ao_set = "ON"
    else:
        ao_set = "OFF"
    print("\tAuto reading:",ao_set,"\t\t\t\t\t\t[AUTO]")
    print("\tAuto speed:",str(settings.auto_speed)+"%","\t\t\t\t\t\t[AUTOSPEED 1-100]")

