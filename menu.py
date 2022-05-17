import time

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
    mark_gray = '\033[7m'

    bold = '\033[1m'            ####
    underline = '\033[4m'       ####
    end = '\033[0m'             ####

class game_menu():
    def __init__(self):
        pass
    def main(self):
        print()
        print("                                  ▄████████ ███▄▄▄▄    ▄█    █▄   ▄██████▄  ▄██   ▄               ")
        print("                                 ███    ███ ███▀▀▀██▄ ███    ███ ███    ███ ███   ██▄             ")
        print("                                 ███    █▀  ███   ███ ███    ███ ███    ███ ███▄▄▄███             ")
        print("                                ▄███▄▄▄     ███   ███ ███    ███ ███    ███ ▀▀▀▀▀▀███             ")
        print("                               ▀▀███▀▀▀     ███   ███ ███    ███ ███    ███ ▄██   ███             ")
        print("                                 ███    █▄  ███   ███ ███    ███ ███    ███ ███   ███             ")
        print("                                 ███    ███ ███   ███ ███    ███ ███    ███ ███   ███             ")
        print("                                 ██████████  ▀█   █▀   ▀██████▀   ▀██████▀   ▀█████▀              ")

        print("")
        print("")
        print(format.mark_gray+"                     |  Start "+format.end)
        print("                     |  Load ")
        print(format.mark_gray+"                     |  Settins "+format.end)
        print("                     |  Exit ")
    def load(self):
        print(" _____                     _   _____                          ")
        print("/  ___|                   | | |  __ \                          ")
        print("\ `--.  __ ___   _____  __| | | |  \/ __ _ _ __ ___   ___  ___ ")
        print(" `--. \/ _` \ \ / / _ \/ _` | | | __ / _` | '_ ` _ \ / _ \/ __|")
        print("/\__/ / (_| |\ V /  __/ (_| | | |_\ \ (_| | | | | | |  __/\__ \\")
        print("\____/ \__,_| \_/ \___|\__,_|  \____/\__,_|_| |_| |_|\___||___/")
        print("                                            ")
    def settings(self):
        print(" _____      _   _   _                 ")
        print("/  ___|    | | | | (_)                ")
        print("\ `--.  ___| |_| |_ _ _ __   __ _ ___ ")
        print(" `--. \/ _ \ __| __| | '_ \ / _` / __|")
        print("/\__/ /  __/ |_| |_| | | | | (_| \__ \\")
        print("\____/ \___|\__|\__|_|_| |_|\__, |___/")
        print("                             __/ |    ")
        print("                            |___/     ")
        print("                                      ")
    def exit(self):
        raise SystemExit

mainmenu = game_menu()

def auto_test(speed):
    test = [
        "This is a test of the autoreading function.",
        "If you have trouble reading this,",
        "Or it's too slow for your liking.",
        "Then perhaps you should consider changing the settings of the autoreading before starting the game with it.",
        "You don't want to miss out on the story, right?",
        "Also, bannana.",
    ]
    time.sleep(0.3)
    for x in test:
        print(x,"\n")
        time.sleep(((1*(speed/100)*len(x.split(" ")))))