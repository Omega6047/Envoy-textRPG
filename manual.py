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
    mark_green = '\033[42m'
    mark_yellow = '\033[43m'    ####
    mark_blue = '\033[44m'      ####
    mark_purple = '\033[45m'    ####
    mark_cyan = '\033[46m'      ####
    mark_gray = '\033[7m'       ####

    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'

def all():
    print(format.mark_green+"\t\t\tBASIC\t\t\t\n"+format.end)
    print(format.underline+"\nSTART"+format.end+"\t–\tStarts the game")
    print(format.underline+"\nLOAD"+format.end+"\t–\tWhile in main menu or game menu, opens the load sub - menu. Using the command again while load\n screen "
          "is open, allows to load a previously saved game "+format.bold+"[LOAD SAVE_ID]"+format.end+".\n If SAVE_ID is not provided, the most recent save will be loaded.")
    print(format.underline+"\nSETTINGS"+format.end+"\t-\tWhile in main menu or game menu, opens settings sub-menu.\n To edit game's settings, use commands written on screen.")
    print(format.underline+"\nEXIT"+format.end+"\t-\tCloses the game.")
    print(format.underline+"\nRETURN"+format.end+"\t-\tIf used while in sub-menu, moves back to main or game menu.")
    print(format.underline+"\nSAVE"+format.end+"\t-\tSaves the currant progress. The save file can be named by adding an argument "+format.bold+"[SAVE SAVE_NAME]"+format.end+". \n If an alternative name is not provided, the save will be named 'ManualSave'.")
    print(format.underline+"\n*empty line*"+format.end+"\t–\tDuring a dialogue or a story event, inputting an empty line will move the dialogue forward.")
    print(format.underline+"\nAUTO"+format.end+"\t–\tWill start to automatically display lines during a story event. Speed of the process can be \nadjusted in the settings sub-menu\n"
          "where it can also be tested with "+format.bold+"[AUTOSPEED TEST]"+format.end+". Once a story \nevent is in the auto reading mode, all other actions are disabled until the end of event.")
    print("\n")
    print(format.mark_green + "\t\t\tCOMBAT\t\t\t" + format.end)
    print(format.underline+"\nATTACK"+format.end+"\t-\tPerforms basic physical attack. ")
    print(format.underline+"\nSKILL"+format.end+"\t-\tUses a chosen skill. A skill can be chosen either by inputting it's name or id "+format.bold+"[SKILL ID/NAME]"+format.end)
    print(format.underline+"\nGUARD"+format.end+"\t-\tRises all defenses until next turn.")
    print(format.underline+"\nITEM"+format.end+"\t-\tUses an item from the inventory.")
    print(format.underline+"\nESCAPE"+format.end+"\t-\tAttempt at an escape from combat. You can't run away run away from \nany fight that is part of a story event.")
    print("\n")
    print(format.mark_green + "\t\t\tROAM\t\t\t" + format.end)
    print(format.underline+"\nMOVE"+format.end+"\t-\tMoves to a connected location chosen by inputting \nit's id "+format.bold+"[MOVE LOCATION_ID]"+format.end)
    print(format.underline+"\nHUNT"+format.end+"\t-\tStarts a fight with a group of local enemies. Possibility \nof starting an encounter with a special enemy.")
    print(format.underline+"\nGATHER"+format.end+"\t-\tGathers materials available in the area. 10 second delay \nbefore another action can be taken. ")
    print(format.underline+"\nHARVEST"+format.end+"\t-\tHarvests plants available in the area. 15 second delay \nbefore another action can be taken. ")
    print(format.underline+"\nSEARCH"+format.end+"\t-\tSearches the area for any points of interest. Some require special \nconditions to be met. 20 second delay before another action can be taken. ")
    print(format.underline+"\nCLEAR"+format.end+"\t-\tClears the terminal and reprints base information about the currant location")

def text():
    print(format.underline + "\n*empty line*" + format.end + "\t–\tMoves the dialogue forward.")
    print(format.underline + "\nAUTO" + format.end + "\t–\tWill start to automatically display lines during a story event. "
        "where it can also be tested with " + format.bold + "[AUTOSPEED TEST]" + format.end + ". Once a story \nevent is in the auto reading mode, all other actions are disabled until the end of event.")

def settings():
    print(format.underline + "\nRETURN" + format.end + "\t-\tMoves back to main or game menu.")
    print(format.underline + "\nRESIZE" + format.end + "Changes window size.")
    print(format.underline + "\nAUTO" + format.end + "Enables or disables auto reading for all story events.")
    print(format.underline + "\nAUTOSPEED" + format.end + "Changes the speed of auto reading. Accepts values in range 1-100")

def loadgame():
    print(format.underline+"\nLOAD"+format.end+"\t–\tAllows to load a previously saved game with"+format.bold+"[LOAD SAVE_ID]"+format.end+".\n If SAVE_ID is not provided, the most recent save will be loaded.")
    print(format.underline + "\nRETURN" + format.end + "\t-\tMoves back to main or game menu.")

def mainmenu():
    print(format.underline + "\nSTART" + format.end + "\t–\tStarts the game")
    print(format.underline + "\nLOAD" + format.end + "\t–\tOpens the load sub-menu.")
    print(format.underline + "\nSETTINGS" + format.end + "\t-\tOpens settings sub-menu.")
    print(format.underline + "\nEXIT" + format.end + "\t-\tCloses the game.")

def fight():
    print(format.underline+"\nATTACK"+format.end+"\t-\tPerforms basic physical attack. ")
    print(format.underline+"\nSKILL"+format.end+"\t-\tUses a chosen skill. A skill can be chosen either by inputting it's name or id "+format.bold+"[SKILL ID/NAME]"+format.end)
    print(format.underline+"\nGUARD"+format.end+"\t-\tRises all defenses until next turn.")
    print(format.underline+"\nITEM"+format.end+"\t-\tUses an item from the inventory.")
    print(format.underline+"\nESCAPE"+format.end+"\t-\tAttempt at an escape from combat. You can't run away run away from \nany fight that is part of a story event.")

def roam():
    print(format.underline + "\nMOVE" + format.end + "\t-\tMoves to a connected location chosen by inputting \nit's id " + format.bold + "[MOVE LOCATION_ID]" + format.end)
    print(format.underline + "\nHUNT" + format.end + "\t-\tStarts a fight with a group of local enemies. Possibility \nof starting an encounter with a special enemy.")
    print(format.underline + "\nGATHER" + format.end + "\t-\tGathers materials available in the area. 10 second delay \nbefore another action can be taken. ")
    print(format.underline + "\nHARVEST" + format.end + "\t-\tHarvests plants available in the area. 15 second delay \nbefore another action can be taken. ")
    print(format.underline + "\nSEARCH" + format.end + "\t-\tSearches the area for any points of interest. Some require special \nconditions to be met. 20 second delay before another action can be taken. ")
    print(format.underline + "\nCLEAR" + format.end + "\t-\tClears the terminal and reprints base information about the currant location")