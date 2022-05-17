import random

class format:
    purple = '\033[95m'
    blue = '\033[34m'           ####
    l_blue = '\033[94m'         ####
    cyan = '\033[36m'           ####
    green = '\033[32m'          ####
    l_green = '\033[92m'        ####
    yellow = '\033[33m'
    l_yellow = '\033[93m'
    red = '\033[91m'
    gray = '\033[38m'

    mark_red = '\033[41m'       ####
    mark_green = '\033[42m'     ####
    mark_yellow = '\033[43m'    ####
    mark_blue = '\033[44m'      ####
    mark_purple = '\033[45m'    ####
    mark_cyan = '\033[46m'      ####
    mark_gray = '\033[7m'       ####

    bold = '\033[1m'            ####
    underline = '\033[4m'       ####
    end = '\033[0m'

class skill():
    def __init__(self, info, dmg_mlt, effect_chance, att_type, spec_effect, spec_comment, cost):
        self.info = info
        self.dmg_mlt = dmg_mlt
        self.effect_chance = effect_chance
        self.att_type = att_type
        self.spec_effect = spec_effect
        self.spec_comment = spec_comment
        self.cost = cost
    def damage_output(self, attack_str, attack_tch, attack_mgi, target_def):
        if self.att_type == "phys":
            enemy_def = target_def - (attack_str/2)
            if enemy_def < 1:
                enemy_def = 1
            damage_random = random.randrange(0,int(attack_str/2))
            damage = int(attack_str/enemy_def) + damage_random
            if damage < 1:
                damage = 1
            return int(damage*self.dmg_mlt)
        elif self.att_type == "mgi":
            enemy_def = target_def - attack_str
            if enemy_def < 1:
                enemy_def = 1
            damage_random = random.randrange(0, attack_mgi)
            damage = int(attack_str / enemy_def) + damage_random
            if damage < 1:
                damage = 1
            return int(damage * self.dmg_mlt)
        elif self.att_type == "tch":
            enemy_def = target_def - attack_str
            if enemy_def < 1:
                enemy_def = 1
            damage_random = random.randrange(0, attack_tch)
            damage = int(attack_tch / enemy_def) + damage_random
            if damage < 1:
                damage = 1
            return int(damage * self.dmg_mlt)

phys_def_snipe = skill(
    "(Light physical damage to single enemy with 50% chance for Critical hit)",
    1.2,
    50,
    "phys",
    "crit",
    "sustains"+format.red+" Critical Hit "+format.end+" to the head",
    5
)
phys_def_bash = skill(
    "(Medium physical damage to single enemy with 20% to inflict Dizzy)",
    1.5,
    20,
    "phys",
    "dizzy",
    "feels a bit"+format.l_yellow+" Dizzy "+format.end+"in the head",
    4
)
phys_def_mordhau = skill(
    "(Medium physical damage to single enemy with 20% to inflict Dizzy)",
    1.5,
    20,
    "phys",
    "dizzy",
    "is"+format.l_yellow+" Dizzy "+format.end+"from a skull fracture",
    4
)
phys_def_poisondart = skill(
    "(Minimal physical damage to single enemy with 30% to inflict Poison)",
    0.9,
    30,
    "tch",
    "poison",
    "takes a"+format.purple+" Poisoned "+format.end+"dart to the knee",
    4
)
phys_def_knifethrow = skill(
    "(Light physical damage to single enemy with 40% to inflict Bleeding)",
    1.2,
    30,
    "phys",
    "bleed",
    "profusely"+format.red+" Bleeds "+format.end+"from the stomach",
    4
)
mgi_elec_bolt = skill(
    "(Light magic damage to single enemy with 30% chance to inflict Paralysis)",
    1.2,
    30,
    "mgi",
    "paralysis",
    "is"+format.yellow+" Paralyzed "+format.end+"and can't move an inch",
    5
)

###########################################################################################################

enemy_attack_bite = skill(
    "",
    1,
    10,
    "phys",
    "bleed",
    "can't stop the"+format.red+" Bleeding"+format.end,
    0
)
enemy_attack_nib = skill(
    "",
    0.2,
    0,
    "phys",
    "none",
    "none",
    0
)
enemy_attack_swipe = skill(
    "",
    1.2,
    0,
    "phys",
    "none",
    "none",
    0
)
enemy_heal_howl = skill(
    "",
    1,
    0,
    "heal",
    "none",
    "none",
    0
)
enemy_attack_charge = skill(
    "",
    1,
    5,
    "phys",
    "dizzy",
    "feels"+format.l_yellow+" Dizzy"+format.end,
    0
)
enemy_attack_choke = skill(
    "",
    1.4,
    0,
    "phys",
    "none",
    "none",
    0
)
enemy_magic_shine = skill(
    "",
    1,
    15,
    "mgi",
    "blind",
    "is"+format.gray+" Blinded "+format.end+"by the light",
    0
)
enemy_magic_beam = skill(
    "",
    1.3,
    0,
    "mgi",
    "none",
    "none",
    0
)
enemy_magic_burn = skill(
    "",
    0.7,
    0,
    "mgi",
    "ignite",
    "gets"+format.red+" Ignited "+format.end+"by the flames",
    0
)
enemy_magic_darkcurse = skill(
    "",
    1,
    0,
    "mgi",
    "curse",
    "becomes affected by a"+format.red+" Curse"+format.end,
    0
)
enemy_attack_strike = skill(
    "",
    1.5,
    20,
    "phys",
    "crit",
    "takes a"+format.red+" Critical hit"+format.end,
    0
)
enemy_attack_crush = skill(
    "",
    1.8,
    0,
    "phys",
    "none",
    "none",
    0
)
enemy_magic_trick = skill(
    "",
    0,
    0,
    "mgi",
    "randomize",
    "none",
    0
)
enemy_magic_forestbreath = skill(
    "",
    1,
    0,
    "mgi",
    "none",
    "none",
    0
)
enemy_attack_ivywhip = skill(
    "",
    1,
    20,
    "phys",
    "crit",
    "gets wipped in"+format.red+" Critical "+format.end+"areas",
    0
)


skill_list = {
#VERT
    "Snipe": phys_def_snipe,
    "Bash": phys_def_bash,
    "Poison_Dart": phys_def_poisondart,
#YAVIN
    "Mordhau": phys_def_mordhau,
    "Knife_Throw": phys_def_knifethrow,
    "Bolt": mgi_elec_bolt,
#ENEMY
    "Bite": enemy_attack_bite,
    "Nib": enemy_attack_nib,
    "Swipe": enemy_attack_swipe,
    "Charge": enemy_attack_charge,
    "Choke": enemy_attack_choke,
    "Crush": enemy_attack_crush,
    "Ivy Wip": enemy_attack_ivywhip,
    "Shine": enemy_magic_shine,
    "Beam": enemy_magic_beam,
    "Burn": enemy_magic_burn,
    "Trick": enemy_magic_burn,
    "Darkflame Curse": enemy_magic_darkcurse,
    "Forest Breath": enemy_magic_forestbreath,
    "Howl": enemy_heal_howl,
}

###########################################################################################################

def effect_guard():
    pass
def effect_dizzy():
    pass
def effect_paralysis():
    pass
def effect_bleed():
    pass
def effect_poison():
    pass
def effect_blind():
    pass
def effect_burn():
    pass
def effect_curse():
    pass
def effect_random():
    pass

def delete_guard():
    pass
def delete_dizzy():
    pass
def delete_paralysis():
    pass
def delete_bleed():
    pass
def delete_poison():
    pass
def delete_blind():
    pass
def delete_burn():
    pass
def delete_curse():
    pass
def delete_random():
    pass

class status_effect:
    def __init__(self, effect_type, effect, delete):
        self.effect_type = effect_type
        self.effect = effect
        self.delete = delete

stat_guard = status_effect(
    "passive",
    effect_guard,
    delete_guard,
)
stat_dizzy = status_effect(
    "passive",
    effect_dizzy,
    delete_dizzy,
)
stat_paralysis = status_effect(
    "active",
    effect_paralysis,
    delete_paralysis,
)
stat_bleed = status_effect(
    "active",
    effect_bleed,
    delete_bleed,
)
stat_poison = status_effect(
    "active",
    effect_poison,
    delete_poison,
)
stat_blind = status_effect(
    "passive",
    effect_blind,
    delete_blind,
)
stat_burn = status_effect(
    "active",
    effect_burn,
    delete_burn,
)
stat_curse = status_effect(
    "active",
    effect_burn,
    delete_burn,
)
stat_random = status_effect(
    "active",
    effect_random,
    delete_random,
)


status_effect_list = {
    "Guard": stat_guard,
    "dizzy": stat_dizzy,
    "paralysis": stat_paralysis,
    "bleed": stat_bleed,
    "poison": stat_poison,
    "blind": stat_blind,
    "curse": stat_curse,
}
