import menu
import playerdata
import story
import NPC
import skill
import location
import location_search
import items
import fightdata
import comments
import manual

from cmd import Cmd
import datetime
import os
import sys
import random
import time

print(story.chapters[playerdata.player.curr_chapter_index])
clear = lambda: os.system('cls')
if os.path.exists("config.ini"):
    playerdata.load_settings()
else:
    playerdata.save_settings()
os.system('mode con: cols='+str(playerdata.settings.res_x)+' lines='+str(playerdata.settings.res_y))

class format:
    purple = '\033[95m'         ####
    blue = '\033[34m'           ####
    l_blue = '\033[94m'         ####
    cyan = '\033[36m'           ####
    green = '\033[32m'          ####
    l_green = '\033[92m'        ####
    yellow = '\033[33m'         ####
    l_yellow = '\033[93m'       ####
    red = '\033[91m'            ####
    gray = '\033[38m'           ####

    mark_red = '\033[41m'       ####
    mark_green = '\033[42m'     ####
    mark_yellow = '\033[43m'    ####
    mark_blue = '\033[44m'      ####
    mark_purple = '\033[45m'    ####
    mark_cyan = '\033[46m'      ####
    mark_gray = '\033[7m'       ####

    bold = '\033[1m'            ####
    underline = '\033[4m'       ####
    end = '\033[0m'             ####

class player_command(Cmd):
    player_state = "mainmenu"
    player_in_submenu = False
    player_turn = 1

    files_saved = []

    ###############################################################################################################
    ### MENU ACTIONS ##############################################################################################
    ###############################################################################################################

    def do_start(self, arg):
        if player_command.player_state == "mainmenu" and player_command.player_in_submenu == False:
            clear()
            read_story()
        else:
            print("You can't do that now!")

    def do_load(self, arg):
        if player_command.player_state == "mainmenu" and player_command.player_in_submenu == False:
            player_command.player_state = "loadgame"
            player_command.player_in_submenu = True
            clear()
            menu.mainmenu.load()
            num_saved = 0
            for paths, dirs, files in os.walk("saved_games/"):
                for file in files:
                    if file.endswith(".txt"):
                        if num_saved == 50:
                            break
                        player_command.files_saved.append(file)
                        num_saved += 1
                        print(num_saved, ". ", file)
        elif player_command.player_state == "loadgame":
            if arg == "":
                print("Error: no file selected!")
            elif int(arg) in range(1, 50):
                playerdata.load_game()
            else:
                print("File id not found!")
        else:
            print("You can't do that now!")

    def do_settings(self, arg):
        if player_command.player_state == "mainmenu" and player_command.player_in_submenu == False:
            player_command.player_in_submenu = True
            player_command.player_state = "settings"
            clear()
            menu.mainmenu.settings()
            playerdata.printsettings()
        else:
            print("You can't do that now!")

    def do_exit(self, arg):
        if player_command.player_state == "mainmenu":
            menu.mainmenu.exit()
        elif player_command.player_state == "gamemenu":
            if input("Are you sure about that? (Yes/No)").lower == 'yes':
                menu.mainmenu.exit()
        else:
            print("You can't do that now!")
    def do_return(self, arg):
        if player_command.player_in_submenu == True:
            clear()
            player_command.player_in_submenu = False
            player_command.player_state = "mainmenu"
            menu.mainmenu.main()
        else:
            print("You can't do that now!")

    ###############################################################################################################
    ### SETTINGS ##################################################################################################
    ###############################################################################################################

    def do_resize(self, arg):
        if player_command.player_state == "settings":
            arg = arg.split(" ")
            if len(arg) != 2 or arg[0].isnumeric() == False or arg[1].isnumeric() == False:
                print("Invalid input")

            elif (int(arg[0]) < 120 or int(arg[1]) < 25) or (int(arg[0]) > 200 or int(arg[1]) > 50):
                print("Invalid size\n\tMIN. size: 120x25\n\tMAX. size: 200x50")
            else:
                playerdata.settings.res_x = arg[0]
                playerdata.settings.res_y = arg[1]
                playerdata.save_settings()
                os.system('mode con: cols=' + str(playerdata.settings.res_x) + ' lines=' + str(playerdata.settings.res_y))
                menu.mainmenu.settings()
                playerdata.printsettings()
    def do_auto(self, arg):
        if player_command.player_state == "settings":
            if playerdata.settings.auto_read == 0:
                playerdata.settings.auto_read = 1
            else:
                playerdata.settings.auto_read = 0
            playerdata.save_settings()
            menu.mainmenu.settings()
            playerdata.printsettings()
        elif player_command.player_state == "text" and playerdata.settings.auto_read == 0:
            playerdata.settings.auto_read = 1
            player_command.player_state = "auto_text"
            print("\n\t\tAuto reading is ON\n")
            read(playerdata.player.text_progress)

    def do_autospeed(self, arg):
        if player_command.player_state == "settings":
            if arg.isnumeric() and (int(arg) > 0 and int(arg) <= 100):
                playerdata.settings.auto_speed = int(arg)
            elif arg == "test":
                clear()
                menu.auto_test(playerdata.settings.auto_speed)
                menu.mainmenu.settings()
                playerdata.printsettings()
            else:
                print("Invalid argument")
            playerdata.save_settings()
            menu.mainmenu.settings()
            playerdata.printsettings()

    ###############################################################################################################
    ### MISC ACTIONS ##############################################################################################
    ###############################################################################################################

    def emptyline(self):
        if player_command.player_state == "text":
            read(playerdata.player.text_progress)
    def do_save(self, arg):
        if player_command.player_state == "text" or player_command.player_state == "roam":
            currant_date = datetime.datetime.now()
            if arg != "":
               save_name = currant_date.strftime("%Y-%m-%d %H-%M-%S") + arg + ".txt"
            else:
                save_name = currant_date.strftime("%d-%m-%Y %H-%M-%S") + " |ManualSave" +".txt"
            if not os.path.exists('saved_games'):
                os.makedirs('saved_games')
            playerdata.save_game(os.path.join("saved_games", save_name), player_command.player_state)
    def do_manual(self, arg):
        man = {
            "all": manual.all,
            "text": manual.text,
            "mainmenu": manual.mainmenu,
            "settings": manual.settings,
            "loadgame": manual.loadgame,
            "fight": manual.fight,
            "storyfight": manual.fight,
            "roam": manual.roam
        }
        if arg != "all":
            arg = player_command.player_state
        man[arg]()

    ###############################################################################################################
    ### COMBAT ACTIONS ############################################################################################
    ###############################################################################################################
    def do_attack(self, arg):
        if (player_command.player_state == "storyfight" or player_command.player_state == "fight") and player_command.player_turn == 1:
            i = 0
            for enemy in fightdata.fight.enemy_list:
                i += 1
                id_string = '[' + str(i) + '] '
                print(id_string,enemy,"\t\t",fightdata.fighter[(i-1)+(len(fightdata.fight.party_list))].HP,"/",fightdata.fighter[(i-1)+(len(fightdata.fight.party_list))].HP_max)
            while True:
                attack_index = input("Pick target index: ")
                if attack_index.isnumeric() == False:
                    attack_index = -1
                else:
                    attack_index = int(attack_index) - 1

                if int(attack_index) not in range(0, len(fightdata.fight.enemy_list)):
                    print("Incorrect enemy index!")
                else:
                    attack_index = int(attack_index) + len(fightdata.fight.party_list)
                    break
            damage_base = fightdata.fighter[fightdata.fight.num_fighter].str
            enemy_defense = fightdata.fighter[attack_index].bld - (damage_base/2)
            if enemy_defense < 1:
                enemy_defense = 1
            damage_random = random.randrange((0-int(damage_base/2)),int(damage_base/2))
            damage_actual = int(damage_base / enemy_defense) + damage_random
            if damage_actual < 0:
                damage_actual = 0

            enemy_dodge = fightdata.fighter[attack_index].agi - fightdata.fighter[attack_index].agi
            if enemy_dodge < 0:
                enemy_dodge = 0
            if random.randrange(0,100) <= enemy_dodge:
                print(fightdata.fighter[attack_index].id, "dodged the attack")
            else:
                fightdata.fighter[attack_index].HP -= damage_actual
                print(fightdata.fighter[attack_index].id,"takes",damage_actual,"damage")
                if fightdata.fighter[attack_index].HP <= 0:
                    del fightdata.fighter[attack_index]
                    del fightdata.fight.enemy_list[attack_index - len(fightdata.fight.party_list)]
                    if fightdata.fight.enemy_list == []:
                        if player_command.player_state == "fight":
                            player_command.player_state = "fightend"
                        else:
                            player_command.player_state = "storyfightend"
                        print()
                        print(format.cyan + "\tVictory!\n" + format.end)
                        time.sleep(1)
                        input("Press ENTER to continue...")
                        fight_end()
                        return
                    fightdata.fight.max_fighter -= 1
            fightdata.fight.num_fighter += 1
            if fightdata.fighter[fightdata.fight.num_fighter].id in fightdata.fight.enemy_list:
                player_command.player_turn = 0
            else:
                player_command.player_turn = 1
            combat_actual()
    def do_guard(self, arg):
        if (player_command.player_state == "storyfight" or player_command.player_state == "fight") and player_command.player_turn == 1:
            print("You rise your gurad")
            fightdata.fighter[fightdata.fight.num_fighter].status_effect_1.append("Guard")
            fightdata.fight.num_fighter += 1
            if fightdata.fighter[fightdata.fight.num_fighter].id in fightdata.fight.enemy_list:
                player_command.player_turn = 0
            else:
                player_command.player_turn = 1
            combat_actual()
    def do_skill(self, arg):
        if (player_command.player_state == "storyfight" or player_command.player_state == "fight") and player_command.player_turn == 1:
            if arg.isnumeric() == True:
                arg = int(arg) - 1
                if arg < len(fightdata.fighter[fightdata.fight.num_fighter].skills.split("-")):
                    arg = fightdata.fighter[fightdata.fight.num_fighter].skills.split("-")[arg]
            else:
                string = ""
                for word in arg.split(" "):
                    if string != "":
                        string += "_"
                    string += word.capitalize()
                    arg = string
            while arg not in fightdata.fighter[fightdata.fight.num_fighter].skills.split("-"):
                arg = input("Input skill to use: ").capitalize()
            if fightdata.fighter[fightdata.fight.num_fighter].EP >= skill.skill_list[arg].cost:
                print("Pick target index: ")
                i = 0
                for enemy in fightdata.fight.enemy_list:
                    i += 1
                    id_string = '[' + str(i) + '] '
                    print(id_string, enemy, "\t\t", fightdata.fighter[(i - 1) + (len(fightdata.fight.party_list))].HP,
                          "/", fightdata.fighter[(i-1)+(len(fightdata.fight.party_list))].HP_max)
                while True:
                    attack_index = input("Pick target index: ")
                    if attack_index.isnumeric() == False:
                        attack_index = -1
                    else:
                        attack_index = int(attack_index) - 1

                    if int(attack_index) not in range(0, len(fightdata.fight.enemy_list)):
                        print("Incorrect enemy index!")
                    else:
                        attack_index = int(attack_index) + len(fightdata.fight.party_list)
                        break
                player = fightdata.fighter[fightdata.fight.num_fighter]
                damage_actual = skill.skill_list[arg].damage_output(player.str, player.tch, player.mgi, NPC.mobs[fightdata.fighter[attack_index].id].bld)
                status_chance = False
                if random.randrange(0, 100) <= skill.skill_list[arg].effect_chance:
                    if skill.skill_list[arg].spec_effect == "none":
                        pass
                    elif skill.skill_list[arg].spec_effect == "crit":
                        damage_actual = int(damage_actual*2.2)
                        status_chance = True
                    elif skill.skill_list[arg].spec_effect not in fightdata.fighter[attack_index].status_effect_3 + \
                            fightdata.fighter[attack_index].status_effect_2 + fightdata.fighter[attack_index].status_effect_1:
                        fightdata.fighter[attack_index].status_effect_3.append(skill.skill_list[arg].spec_effect)
                        status_chance = True
                enemy_dodge = fightdata.fighter[attack_index].agi - fightdata.fighter[attack_index].agi
                if enemy_dodge < 0:
                    enemy_dodge = 0
                if random.randrange(0, 100) <= enemy_dodge:
                    print(fightdata.fighter[attack_index].id, "dodged the attack")
                else:
                    fightdata.fighter[attack_index].HP -= damage_actual
                    fightdata.fighter[fightdata.fight.num_fighter].EP -= skill.skill_list[arg].cost
                    if status_chance == True:
                        print(fightdata.fighter[attack_index].id,skill.skill_list[arg].spec_comment)
                    print(fightdata.fighter[attack_index].id, "takes", damage_actual, "damage")
                if fightdata.fighter[attack_index].HP <= 0:
                    del fightdata.fighter[attack_index]
                    del fightdata.fight.enemy_list[attack_index - len(fightdata.fight.party_list)]
                    if fightdata.fight.enemy_list == []:
                        if player_command.player_state == "fight":
                            player_command.player_state = "fightend"
                        else:
                            player_command.player_state = "storyfightend"
                        print()
                        print(format.cyan + "\tVictory!\n" + format.end)
                        time.sleep(1)
                        input("Press ENTER to continue...")
                        fight_end()
                        return
                    fightdata.fight.max_fighter -= 1
                fightdata.fight.num_fighter += 1
                if fightdata.fighter[fightdata.fight.num_fighter].id in fightdata.fight.enemy_list:
                    player_command.player_turn = 0
                else:
                    player_command.player_turn = 1
                combat_actual()
            else:
                print("Not enough Energy!")
    def do_escape(self, arg):
        if player_command.player_state == "storyfight" and player_command.player_turn == 1:
            print("You can't escape now!")
        if player_command.player_state == "fight" and player_command.player_turn == 1:
            pass

    ###############################################################################################################
    ### ROAM ACTIONS ##############################################################################################
    ###############################################################################################################

    def do_move(self, arg):
        if arg != "" and arg.isnumeric():
            arg = int(arg)
        else:
            arg = 0
        connect_location = []
        i = 1
        for connect in location.instance[playerdata.player.location].connect_location.split("-"):
            connect_location.append(connect)
            print('[',i,'] ',location.instance[connect].name)
            i += 1
        if int(arg)-1 in range(0, len(connect_location)):
            playerdata.player.location = connect_location[arg - 1]
            roam_data()
        else:
            while True:
                if arg-1 not in range(0, len(connect_location)):
                    arg = int(input("Choose location index: "))
                else:
                    break
            playerdata.player.location = connect_location[arg-1]
            roam_data()
    def do_hunt(self, arg):
        if player_command.player_state == "roam" and datetime.datetime.now() >= playerdata.player.activity_delay:
            player_command.player_state = "fight"
            clear()
            if playerdata.player.daytime == "day":
                if random.randrange(0, 1) <= location.instance[playerdata.player.location].special_chance_day:
                    enemy = random.choice(location.instance[playerdata.player.location].special_fauna_day.split("-"))
                    boss = enemy
                    for minion in NPC.mobs[boss].minions.split("-"):
                        enemy += "-"+minion
                    min_enemy = len(playerdata.player.currant_char.split("-"))
                    max_enemy = 2 * min_enemy + 2
                    enemy_number = random.randrange(min_enemy, max_enemy)
                    for i in range(enemy_number):
                        enemy += "-"+random.choice(NPC.mobs[boss].minions.split("-"))
                else:
                    enemy = random.choice(location.instance[playerdata.player.location].local_fauna_day.split("-"))
                    allies = []
                    for hostile in location.instance[playerdata.player.location].local_fauna_day.split("-"):
                        if NPC.mobs[enemy].type == NPC.mobs[hostile].type:
                            allies.append(hostile)
                    cont_chance = 90
                    while random.randrange(0,100) <= cont_chance:
                        enemy += "-"+random.choice(allies)
                        cont_chance = int(cont_chance/2)
            else:
                if random.randrange(0, 100) <= location.instance[playerdata.player.location].special_chance_night:
                    enemy = random.choice(location.instance[playerdata.player.location].special_fauna_night.split("-"))
                    boss = enemy
                    for minion in NPC.mobs[boss].minions:
                        enemy += "-"+minion
                    cont_chance = 150
                    while random.randrange(0,100) <= cont_chance:
                        enemy += "-"+random.choice(NPC.mobs[boss].minions)
                        cont_chance = int(cont_chance/2)
                else:
                    enemy = random.choice(location.instance[playerdata.player.location].local_fauna_night.split("-"))
                    allies = []
                    for hostile in location.instance[playerdata.player.location].local_fauna_night.split("-"):
                        if NPC.mobs[enemy].type == NPC.mobs[hostile].type:
                            allies.append(hostile)
                    cont_chance = 90
                    while random.randrange(0,100) <= cont_chance:
                        enemy += "-"+random.choice(allies)
                        cont_chance = int(cont_chance/2)
            print(enemy)
            combat_start(playerdata.player.currant_char, enemy)
            combat_actual()
        elif player_command.player_state == "roam":
            print("You still have to wait",int(abs(datetime.datetime.now()-playerdata.player.activity_delay).total_seconds()),"seconds")
        else:
            print("You can't do that now!")
    def do_gather(self, arg):
        if player_command.player_state == "roam" and datetime.datetime.now() >= playerdata.player.activity_delay:
            cont_chance = 90
            if random.randrange(0, 100) <= cont_chance:
                cont_chance = 100
                material = location.instance[playerdata.player.location].local_material.split("-")
                item_found = []
                while random.randrange(0, 100) <= cont_chance:
                    item = random.choice(material)
                    item_found.append(item)
                    cont_chance = int(cont_chance * 0.4)
                for item in item_found:
                    items.inventory.materials[item] += 1
            else:
                cont_chance = 100
                material = location.instance[playerdata.player.location].local_junk.split("-")
                item_found = []
                while random.randrange(0, 100) <= cont_chance:
                    item = random.choice(material)
                    item_found.append(item)
                    cont_chance = int(cont_chance * 0.6)
                for item in item_found:
                    items.inventory.junk[item] += 1
            if item_found != []:
                print("You've found: ", item_found)
            else:
                print(random.choice(comments.gather_comments))
            action_delay(10)
        elif player_command.player_state == "roam" and datetime.datetime.now() < playerdata.player.activity_delay:
            print("You still have to wait",int(abs(datetime.datetime.now()-playerdata.player.activity_delay).total_seconds()),"seconds")
        else:
            print("You can't do that now!")
    def do_harvest(self, arg):
        if player_command.player_state == "roam" and datetime.datetime.now() >= playerdata.player.activity_delay:
            if playerdata.player.daytime == "day":
                flora = location.instance[playerdata.player.location].local_flora_day.split("-")
            else:
                flora = location.instance[playerdata.player.location].local_flora_night.split("-")
            cont_chance = 90
            item_found = []
            while random.randrange(0, 100) <= cont_chance:
                item = random.choice(flora)
                if item in  playerdata.player.known_flora:
                    item_found.append(item)
                cont_chance = cont_chance * 0.4
            if item_found != []:
                print("You've found: ",item_found)
            else:
                print(random.choice(comments.harvest_comments))
            for item in item_found:
                items.inventory.plants[item] += 1
            action_delay(15)
        elif player_command.player_state == "roam" and datetime.datetime.now() < playerdata.player.activity_delay:
            print("You still have to wait",int(abs(datetime.datetime.now()-playerdata.player.activity_delay).total_seconds()),"seconds")
        else:
            print("You can't do that now!")
    def do_search(self, arg):
        if player_command.player_state == "roam" and datetime.datetime.now() >= playerdata.player.activity_delay:
            if random.randrange(0, 100) <= location.instance[playerdata.player.location].search_chance:
                search_id = random.randrange(0, len(location_search.instance[playerdata.player.location]))
                search_event = location_search.instance[playerdata.player.location][search_id]()
                if len(search_event.split("|")) == 1:
                    search_type = search_event
                    search_arg = ""
                else:
                    search_type = search_event.split("|")[0]
                    search_arg = search_event.split("|")[1]
            else:
                search_type = "nothing"
                search_arg = ""
            search = {
                "nothing": search_nothing,
                "find_random": search_find_random,
            }
            search[search_type](search_arg)
        elif player_command.player_state == "roam" and datetime.datetime.now() < playerdata.player.activity_delay:
            print("You still have to wait",int(abs(datetime.datetime.now()-playerdata.player.activity_delay).total_seconds()),"seconds")
        else:
            print("You can't do that now!")
    def do_clear(self, arg):
        clear()
        roam_data()

###########################################################################################################

def read(progress):
    text = story.story[progress]
    line_len = 0
    words = 0
    for word in text.split(" "):
        word += " "
        words += 1
        line_len += len(word)+1
        if line_len >= int(playerdata.settings.res_x)-5:
            print("\n", end="")
            line_len = 0
        sys.stdout.write(word)
    print()
    line_len = 0
    playerdata.player.text_progress += 1
    if playerdata.player.text_progress == len(story.story):
        playerdata.player.story_progress += 1
        playerdata.player.text_progress = 0
        read_story = story_line[playerdata.player.story_progress]
        read_story()
    elif playerdata.settings.auto_read == 1:
        word_speed = 1*(int(playerdata.settings.auto_speed)/100)
        time.sleep(word_speed*words)
        if player_command.player_state == "auto_text":
            print()
            read(playerdata.player.text_progress)

###########################################################################################################

def combat_start(party, enemy):
    player_group = party.split("-")
    enemy_group = enemy.split("-")
    fightdata.fight.enemy_list = enemy_group
    fightdata.fight.enemy_backup = enemy.split("-")
    fightdata.fight.party_list = player_group
    i = 0
    for char in player_group:
        fightdata.fighter.append("")
        str = playerdata.char_fight[char].lvl * (5 + playerdata.char_fight[char].str)
        bld = playerdata.char_fight[char].lvl * (5 + playerdata.char_fight[char].bld)
        mgi = playerdata.char_fight[char].lvl * (5 + playerdata.char_fight[char].mgi)
        tch = playerdata.char_fight[char].lvl * (5 + playerdata.char_fight[char].tch)
        agi = playerdata.char_fight[char].lvl * (5 + playerdata.char_fight[char].agi)
        end = playerdata.char_fight[char].lvl * (5 + playerdata.char_fight[char].end)
        HP = playerdata.char_fight[char].lvl * (5 + playerdata.char_fight[char].HP)
        EP = playerdata.char_fight[char].lvl * (5 + playerdata.char_fight[char].EP)
        fightdata.fighter[i] = fightdata.fight(str, bld, mgi, tch, agi, end, playerdata.char_fight[char].skills, HP, HP, EP, EP, char)
        i += 1
    for enemy in enemy_group:
        fightdata.fighter.append("")
        str = NPC.mobs[enemy].lvl * (5 + NPC.mobs[enemy].str)
        bld = NPC.mobs[enemy].lvl * (5 + NPC.mobs[enemy].bld)
        mgi = NPC.mobs[enemy].lvl * (5 + NPC.mobs[enemy].mgi)
        tch = NPC.mobs[enemy].lvl * (5 + NPC.mobs[enemy].tch)
        agi = NPC.mobs[enemy].lvl * (5 + NPC.mobs[enemy].agi)
        end = NPC.mobs[enemy].lvl * (5 + NPC.mobs[enemy].end)
        HP = NPC.mobs[enemy].lvl * (5 + NPC.mobs[enemy].HP)
        fightdata.fighter[i] = fightdata.fight(str, bld, mgi, tch, agi, end, NPC.mobs[enemy].skills, HP, HP, 0, 0, enemy)
        i += 1

def combat_actual():
    fightdata.fight.max_fighter = len(fightdata.fight.enemy_list) + len(fightdata.fight.party_list) - 1
    if fightdata.fight.num_fighter == fightdata.fight.max_fighter:
        fightdata.fight.num_fighter = 0
        fightdata.fight.new_turn = True
    if fightdata.fight.new_turn == True:
        print(format.cyan)
        print("  ____  _        _ __   _______ ____    _____ _   _ ____  _   _ ")
        print(" |  _ \| |      / \\\\ \ / / ____|  _ \  |_   _| | | |  _ \| \ | |")
        print(" | |_) | |     / _ \\\\ V /|  _| | |_) |   | | | | | | |_) |  \| |")
        print(" |  __/| |___ / ___ \| | | |___|  _ <    | | | |_| |  _ <| |\  |")
        print(" |_|   |_____/_/   \_\_| |_____|_| \_\   |_|  \___/|_| \_\_| \_|")
        print(format.end)
        print("Player: ", fightdata.fight.party_list, "\nEnemy party: ", fightdata.fight.enemy_list)
        fightdata.fight.new_turn = False
    fightdata.fight.curr_fighter = fightdata.fighter[fightdata.fight.num_fighter].id
    if fightdata.fight.curr_fighter in fightdata.fight.party_list:
        player_command.player_turn = 1
    else:
        player_command.player_turn = 0
    if player_command.player_turn == 1 and (player_command.player_state == "fight" or player_command.player_state == "storyfight"):
        print("----------------------------------------------------------------------------------")
        pre_turn_check()
        print("Currant fighter: ",fightdata.fight.curr_fighter)
        print("HP:",str(fightdata.fighter[fightdata.fight.num_fighter].HP)+"/"+str(fightdata.fighter[fightdata.fight.num_fighter].HP_max),
              "\t\tEP:",str(fightdata.fighter[fightdata.fight.num_fighter].EP)+"/"+str(fightdata.fighter[fightdata.fight.num_fighter].EP_max))
        print()
        print("\tAttack")
        print("\tGuard")
        print("\tSkill")
        i = 1
        for element in fightdata.fighter[fightdata.fight.num_fighter].skills.split("-"):
            index = str(i)+'.'
            if len(element) >= 12:
                print("\t\t",index,element.replace("_", " "),"\t",skill.skill_list[element].info)
            elif len(element) >= 8:
                print("\t\t",index,element.replace("_", " "),"\t\t\t",skill.skill_list[element].info)
            elif len(element) >= 4:
                print("\t\t",index,element.replace("_", " "),"\t\t\t\t\t",skill.skill_list[element].info)
            else:
                print("\t\t",index,element.replace("_", " "),"\t\t\t\t\t\t",skill.skill_list[element].info)
            i += 1
        print("\tEscape")
        print()
    elif player_command.player_turn == 0 and (player_command.player_state == "fight" or player_command.player_state == "storyfight"):
        print(format.red)
        print("  _____ _   _ _____ __  ____   __  _____ _   _ ____  _   _ ")
        print(" | ____| \ | | ____|  \/  \ \ / / |_   _| | | |  _ \| \ | |")
        print(" |  _| |  \| |  _| | |\/| |\ V /    | | | | | | |_) |  \| |")
        print(" | |___| |\  | |___| |  | | | |     | | | |_| |  _ <| |\  |")
        print(" |_____|_| \_|_____|_|  |_| |_|     |_|  \___/|_| \_\_| \_|")
        print(format.end)
        for enemy in fightdata.fight.enemy_list:
            if player_command.player_turn == 0:
                pre_turn_check()
                enemy_turn(enemy)
                fightdata.fight.num_fighter += 1
        fightdata.fight.num_fighter = 0
        if player_command.player_turn == 0:
            player_command.player_turn = 1
            combat_actual()

def fight_end():
    print(format.gray)
    print("  ____  _____ ____  _   _ _   _____ ____ ")
    print(" |  _ \| ____/ ___|| | | | | |_   _/ ___|")
    print(" | |_) |  _| \___ \| | | | |   | | \___ \\")
    print(" |  _ <| |___ ___) | |_| | |___| |  ___) |")
    print(" |_| \_\_____|____/ \___/|_____|_| |____/ ")
    print(format.end)
    exp_gained = 0
    gold_gained = 0
    item_drops = []
    for enemy in fightdata.fight.enemy_backup:
        exp_gained += NPC.mobs[enemy].lvl * 10
        gold_gained += NPC.mobs[enemy].price
        for drop in NPC.mobs[enemy].drop.split("-"):
            if items.items_list[drop].drop_chance >= random.randrange(0, 100):
                item_drops.append(drop)
                if drop in items.inventory.materials:
                    items.inventory.materials[drop] += 1
                elif drop in items.inventory.trophys:
                    items.inventory.trophys[drop] += 1
                elif drop in items.inventory.junk:
                    items.inventory.junk[drop] += 1
                elif drop in items.inventory.usables:
                    items.inventory.usables[drop] += 1
                elif drop in items.inventory.plants:
                    items.inventory.plants[drop] += 1
                elif drop in items.inventory.quest:
                    items.inventory.quest[drop] += 1
    print("Gained experiance: ",format.green+str(exp_gained)+format.end)
    for char in playerdata.player.currant_char.split("-"):
        playerdata.char_fight[char].exp += exp_gained
        if playerdata.char_fight[char].exp >= playerdata.char_fight[char].exp_to_lvl:
            print("\t",char,"levels up! ",playerdata.char_fight[char].lvl, " --> ", playerdata.char_fight[char].lvl + 1)
            playerdata.char_fight[char].lvl += 1
            playerdata.char_fight[char].skill_p += 5
    print("Gained gold: ",format.yellow+str(gold_gained)+format.end)
    print("Gained items:", item_drops)
    playerdata.player.gold += gold_gained
    player_command.player_turn = 1
    fightdata.restart()
    i = 0
    for x in fightdata.fighter:
        del fightdata.fighter[i]
        i += 1
    time.sleep(1)
    input("Press ENTER to continue...")
    if player_command.player_state == "storyfightend":
        playerdata.player.story_progress += 1
        read_story = story_line[playerdata.player.story_progress]
        read_story()
    else:
        player_command.player_state = "roam"
        roam_data()

def enemy_turn(enemy):
    skill_aval = [0, 0, 0, 0]
    for x in fightdata.fighter[fightdata.fight.num_fighter].skills.split("-"):
        if skill.skill_list[x].att_type == "phys":
            skill_aval[0] +=1
        elif skill.skill_list[x].att_type == "mgi":
            skill_aval[1] +=1
        elif skill.skill_list[x].att_type == "tch":
            skill_aval[2] +=1
        elif skill.skill_list[x].att_type == "heal":
            skill_aval[3] +=1
    if skill_aval[3] == 0:
        time.sleep(.5)
        enemy_attack = random.choice(fightdata.fighter[fightdata.fight.num_fighter].skills.split("-"))
        print(enemy, "uses", enemy_attack)
        attack_index = random.randrange(0, len(fightdata.fight.party_list))
        enemy_stat = fightdata.fighter[fightdata.fight.num_fighter]
        target_stat = fightdata.fighter[attack_index]
        damage_actual = skill.skill_list[enemy_attack].damage_output(enemy_stat.str, enemy_stat.tch, enemy_stat.mgi, target_stat.bld)
        player_dodge = target_stat.agi - enemy_stat.agi
        time.sleep(.7)
        if player_dodge >= random.randrange(0,100):
            print(fightdata.fighter[attack_index].id,"dodged the attack")
        else:
            status_chance = False
            if random.randrange(0, 100) <= skill.skill_list[enemy_attack].effect_chance:
                if skill.skill_list[enemy_attack].spec_effect == "none":
                    pass
                elif skill.skill_list[enemy_attack].spec_effect == "crit":
                    damage_actual = int(damage_actual * 2.2)
                    status_chance = True
                elif skill.skill_list[enemy_attack].spec_effect not in fightdata.fighter[attack_index].status_effect_3 + \
                        fightdata.fighter[attack_index].status_effect_2 + fightdata.fighter[attack_index].status_effect_1:
                    fightdata.fighter[attack_index].status_effect_3.append(skill.skill_list[enemy_attack].spec_effect)
                    status_chance = True
            if status_chance == True:
                print(fightdata.fighter[attack_index].id, skill.skill_list[enemy_attack].spec_comment)
            fightdata.fighter[attack_index].HP -= damage_actual
            print(fightdata.fighter[attack_index].id,"takes", damage_actual, "damage")
            if fightdata.fighter[attack_index].HP <= 0:
                del fightdata.fighter[attack_index]
                del fightdata.fight.party_list[attack_index]
                fightdata.fight.num_fighter -= 1
                if fightdata.fight.party_list == []:
                    pre_turn_check()
    elif skill_aval[1] > 0 and skill_aval[2] == 0:
        pass
    time.sleep(.5)

def pre_turn_check():
    if player_command.player_state == "storyfight" or player_command.player_state == "fight":
        if fightdata.fight.party_list != [] and fightdata.fight.enemy_list != 0:
            temp = fightdata.fighter[fightdata.fight.num_fighter].status_effect_1
            for effect in fightdata.fighter[fightdata.fight.num_fighter].status_effect_1:
                if skill.status_effect_list[effect].effect_type == "active":
                    skill.status_effect_list[effect].effect()
                else:
                    skill.status_effect_list[effect].delete()
                temp.remove(effect)
            fightdata.fighter[fightdata.fight.num_fighter].status_effect_1 = temp

            temp = fightdata.fighter[fightdata.fight.num_fighter].status_effect_2
            for effect in fightdata.fighter[fightdata.fight.num_fighter].status_effect_2:
                if skill.status_effect_list[effect].effect_type == "active":
                    skill.status_effect_list[effect].effect()
                fightdata.fighter[fightdata.fight.num_fighter].status_effect_1.append(effect)
                temp.remove(effect)
            fightdata.fighter[fightdata.fight.num_fighter].status_effect_2 = temp

            temp = fightdata.fighter[fightdata.fight.num_fighter].status_effect_3
            for effect in fightdata.fighter[fightdata.fight.num_fighter].status_effect_3:
                if skill.status_effect_list[effect].effect_type == "active":
                    skill.status_effect_list[effect].effect()
                fightdata.fighter[fightdata.fight.num_fighter].status_effect_2.append(effect)
                temp.remove(effect)
            fightdata.fighter[fightdata.fight.num_fighter].status_effect_3 = temp

        if fightdata.fight.party_list == []:
            clear()
            print(format.red+"\tDEFEAT"+format.end)
            if player_command.player_state == "storyfight":
                player_command.player_state = "storydefeat"
            elif player_command.player_state == "fight":
                player_command.player_state = "defeat"
            time.sleep(1.5)
            while True:
                prompt = input("Do you want to try again? [yes/no]   ").lower()
                if prompt == "yes" or prompt == "no":
                    break
            if prompt == "no":
                clear()
                player_command.player_state = "mainmenu"
                player_command.player_turn = 1
                menu.mainmenu.main()
            if prompt == "yes":
                if player_command.player_state == "storydefeat":
                    playerdata.player.fight_progress -= 1
                    fightdata.restart()
                    player_command.player_turn = 1
                    story_state_storyfight()
                else:
                    clear()
                    enemy = ""
                    i = 0
                    for e in fightdata.fight.enemy_backup:
                        if i != len(fightdata.fight.enemy_backup)-1:
                            enemy += e+"-"
                        else:
                            enemy += e
                        i += 1
                    player_command.player_turn = 1
                    combat_start(playerdata.player.currant_char, enemy)
                    combat_actual()
        elif fightdata.fight.enemy_list == []:
            if player_command.player_state == "fight":
                player_command.player_state = "fightend"
            else:
                player_command.player_state = "storyfightend"
            time.sleep(0.5)
            print()
            print(format.cyan+"\tVictory!\n"+format.end)
            time.sleep(1.5)
            input("Press ENTER to continue...\n")
            fight_end()

###########################################################################################################

def roam_data():
    clear()
    print("Location: ",location.instance[playerdata.player.location].name)
    connect_location = []
    for connect in location.instance[playerdata.player.location].connect_location.split("-"):
        connect_location.append(location.instance[connect].name)
    print("Connected locations: ",connect_location)
    print()
    local_flora = []
    if playerdata.player.daytime == "day":
        flora_time = location.instance[playerdata.player.location].local_flora_day.split("-")
        local_fauna = location.instance[playerdata.player.location].local_fauna_day.split("-")
        local_special = location.instance[playerdata.player.location].special_fauna_day.split("-")
    else:
        flora_time = location.instance[playerdata.player.location].local_flora_night.split("-")
        local_fauna = location.instance[playerdata.player.location].local_fauna_night.split("-")
        local_special = location.instance[playerdata.player.location].special_fauna_night.split("-")
    for flora in flora_time:
        if flora in playerdata.player.known_flora:
            local_flora.append(flora)
    if local_flora == []:
        print("Local flora: You don't recognize any plants in the area.")
    else:
        print("Local flora: ",local_flora)
    print("Local enemies: ", local_fauna)
    print("Special enemies: ", local_special)

def action_delay(t):
    playerdata.player.activity_delay = datetime.datetime.now() + datetime.timedelta(seconds=t)

def search_nothing(arg):
    print(random.choice(comments.search_comments))

def search_find_random(arg):
    aval_items = []
    if playerdata.player.daytime == "day":
        aval_items.append(location.instance[playerdata.player.location].local_flora_day.split("-"))
    else:
        aval_items.append(location.instance[playerdata.player.location].local_flora_night.split("-"))
    aval_items.append(location.instance[playerdata.player.location].local_material.split("-"))
    item = random.choice(aval_items)
    if item[0] in location.instance[playerdata.player.location].local_material.split("-"):
        for x in item:
            items.inventory.materials[x] += 1
    else:
        for x in item:
            items.inventory.plants[x] += 1
    print("During the search you've found:",item)

###########################################################################################################

def story_state_read():
    player_command.player_state = "text"
    if playerdata.settings.auto_read == 1:
        player_command.player_state = "auto_text"
    prompt.prompt = "\t"
    playerdata.player.part_progress += 1
    read_prep = story.part_prog[playerdata.player.part_progress]
    story.story = read_prep()
    read(playerdata.player.text_progress)

def story_state_storyfight():
    prompt.prompt = "\n>>>"
    player_command.player_state = "storyfight"
    clear()
    combat_start(playerdata.player.currant_char, story.story_fight[playerdata.player.fight_progress])
    playerdata.player.fight_progress += 1
    combat_actual()

def story_state_roam():
    prompt.prompt = "\n>>>"
    player_command.player_state = "roam"
    roam_data()

def story_display_part():
    playerdata.player.curr_part += 1
    i = 0
    while i <= int(playerdata.settings.res_y):
        i += 1
        print()
        time.sleep(0.05)
    i = 0
    print("\t\t\t\t",playerdata.player.curr_chapter)
    print("\t\t\t\t Part", playerdata.player.curr_part)
    while i <= int(playerdata.settings.res_y)/2:
        print()
        i += 1
    time.sleep(3)
    i = 0
    while i <= int(playerdata.settings.res_y)/2:
        i += 1
        print()
        time.sleep(0.05)
    clear()
    playerdata.player.story_progress += 1
    story_line[playerdata.player.story_progress]()

def story_assign_chapter():
    playerdata.player.curr_chapter = story.chapters[playerdata.player.curr_chapter_index]
    playerdata.player.curr_chapter_index += 1
    playerdata.player.story_progress += 1
    story_line[playerdata.player.story_progress]()

story_line={
    0: story_state_read,
    1: story_assign_chapter,
    2: story_display_part,
    3: story_state_read,
    4: story_display_part,
    5: story_state_read,
    6: story_state_read,
    7: story_state_roam
}


###########################################################################################################

read_story = story_line[playerdata.player.story_progress]
menu.mainmenu.main()

prompt = player_command()
prompt.prompt = "\n>>>"
prompt.cmdloop()
