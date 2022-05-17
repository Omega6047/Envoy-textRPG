class fight():
    enemy_list = []
    enemy_backup = []
    party_list = []
    curr_fighter = ""
    num_fighter = 0
    max_fighter = 0
    new_turn = True
    fight_restart = 0

    def __init__(self, str, bld, mgi, tch, agi, end, skills, HP, HP_max, EP, EP_max, id):
        self.str = str
        self.bld = bld
        self.mgi = mgi
        self.tch = tch
        self.agi = agi
        self.end = end
        self.skills = skills
        self.HP = HP
        self.HP_max = HP_max
        self.EP = EP
        self.EP_max = EP_max
        self.status_effect_3 = []
        self.status_effect_2 = []
        self.status_effect_1 = []
        self.id = id
fighter = []

def restart():
    fight.enemy_list = []
    fight.enemy_backup = []
    fight.party_list = []
    fight.curr_fighter = ""
    fight.num_fighter = 0
    fight.max_fighter = 0
    fight.new_turn = True