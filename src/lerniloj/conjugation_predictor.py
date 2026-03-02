from copy import deepcopy
import re


RED = "\033[0;31m"
RESET = "\033[0m"


def verb_conjugator(verb_in):
    note = ""
    TARGET = verb_in.lower().replace("e^", "ê").replace("e'", "é").replace("i^", "î")
    if len(TARGET) <= 3:
        print(f"{RED}verb must be at least 4 letters long")
        quit()
    if TARGET[-2:] not in ["er", "ir", "ïr", "re"]:
        print(f"{RED}verb ending {TARGET[-2:]} is not valid")
        quit()
    
    is_reflexive = False
    if TARGET[:3] == "se ":
        is_reflexive = True
        TARGET = TARGET[3:]
    elif TARGET[:2] == "s'":
        is_reflexive = True
        TARGET = TARGET[2:]
    
    if TARGET == "etre":
        TARGET = "être"
    if TARGET == "":
        print(f"{RED}empty input so quitting")
        quit()

    TARGET = TARGET.lower()
    ENDING = TARGET[-2:]
    STEM = TARGET[:-2]

    PRESENT_STEM = STEM
    PRESENT_JE_TU_IL_STEM = ""
    NOUS_VOUS_PRESENT_STEM = ""
    ILS_PRESENT_STEM = ""
    ils_present_use_nous_stem = False
    FUTURE_CONDITIONAL_STEM = ""
    SUBJUNCTIVE_STEM = ""
    SUBJUNCTIVE_NOUS_STEM = ""
    IMPERFECT_SUBJUNCTIVE_STEM = STEM
    PASSE_SIMPLE_STEM = STEM
    PAST_PARTCIPLE_STEM = STEM
    past_participle = ""

    defects = []
    AUXILLARY = "avoir"


    def remove_codes(x):
        return x.replace(RED, "").replace(RESET, "")


    def il_add_t():
        present_endings[2] += RED + "t"

    
    def is_target_ends(x):
        l = len(x)
        return TARGET[-l:] == x
    

    def red(x):
        if type(x) == list:
            return [red(i) for i in x]
        return f"{RED}{x}{RESET}"
    

    def start_red(x):
        return f"{RED}{x}"


    if TARGET in [
        "aller",
        "arriver",
        "descendre",
        "entrer",
        "monter",
        "mourir",
        "naître",
        "partir"
        "rentrer",
        "retourner",
        "sortir",
        "tomber",
        "venir",
        "devenir",
        "intervenir",
        "parvenir",
        "provenir",
        "revenir",
        "survenir",
    ] or is_reflexive:
        AUXILLARY = f"{RED}être"


    imperfect_endings = ["ais", "ais", "ait", "ions", "iez", "aient"]
    future_endings = ["ai", "as", "a", "ons", "ez", "ont"]
    conditional_endings = ["ais", "ais", "ait", "ions", "iez", "aient"]
    subjunctive_endings = ["e", "es", "e", "ions", "iez", "ent"]

    er_present_pattern = present_endings = ["e", "es", "e", "ons", "ez", "ent"]
    sst_present_pattern = [f"{RED}s", f"{RED}s", f"{RED}t", "ons", "ez", "ent"]
    i_passe_simple_pattern = [f"i{RESET}s", f"i{RESET}s", f"it", f"î{RESET}mes", f"î{RESET}tes", f"i{RESET}rent"]
    in_passe_simple_pattern = [RED + i[0] + "n" + i[1:] for i in i_passe_simple_pattern]
    u_passe_simple_pattern = [f"u{RESET}s", f"u{RESET}s", f"ut", f"û{RESET}mes", f"û{RESET}tes", f"u{RESET}rent"]
    û_passe_simple_pattern = [i.replace("u", "û") for i in u_passe_simple_pattern]
    smart_passe_simple = False

    if ENDING == "er":
        present_endings = er_present_pattern
        passe_simple_endings = ["ai", "as", "a", "âmes", "âtes", "èrent"]
        past_participle_ending = "é"

        if TARGET == "aller":
            PRESENT_STEM = red("v")
            present_endings = [f"{RED}ais", f"{RED}as", f"{RED}a", "ons", "ez", f"{RED}ont"]
            NOUS_VOUS_PRESENT_STEM = "all"
            FUTURE_CONDITIONAL_STEM = "ir"
            SUBJUNCTIVE_STEM = red("aill")
            SUBJUNCTIVE_NOUS_STEM = "all"

        if any([
            TARGET[-4:] == "ager",
            TARGET[-5:] == "anger",
        ]):
            present_endings[3] = RED + "e" + RESET + "ons"
            imperfect_endings = ["eais", "eais", "eait", "ions", "iez", "eaient"]
            IMPERFECT_SUBJUNCTIVE_STEM += "e"
            passe_simple_endings = ["e" + k for k in passe_simple_endings[:-1]] + ["èrent"]
            present_participle = TARGET[:-2] + red("eant")

        if TARGET[-4] == "e":
            p1 = TARGET[:-4]
            p2 = TARGET[-3]
            PRESENT_STEM = p1 + red("è") + p2
            NOUS_VOUS_PRESENT_STEM = p1 + "e" + p2
            FUTURE_CONDITIONAL_STEM = TARGET
            SUBJUNCTIVE_NOUS_STEM = TARGET[:-2]

        if TARGET[-4] == "é":
            p1 = TARGET[:-4]
            p2 = TARGET[-3]
            PRESENT_STEM = p1 + red("è") + p2
            NOUS_VOUS_PRESENT_STEM = p1 + "é" + p2
            FUTURE_CONDITIONAL_STEM = TARGET
        
        if TARGET == "appeler":
            PRESENT_STEM = "appe" + red("ll")
            NOUS_VOUS_PRESENT_STEM = f"{RESET}appel"
            FUTURE_CONDITIONAL_STEM = f"{RESET}appe{RED}ll{RESET}er"

        if is_target_ends("oyer") or is_target_ends("ayer") or is_target_ends("uyer"):
            p1 = TARGET[:-3]
            PRESENT_STEM = p1 + red("i")
            NOUS_VOUS_PRESENT_STEM = p1 + "y"
            if TARGET == "envoyer":
                FUTURE_CONDITIONAL_STEM = "enverr"

        if TARGET == "jeter":
            PRESENT_STEM = "je" + red("tt")
            NOUS_VOUS_PRESENT_STEM = f"{RESET}jet"
            FUTURE_CONDITIONAL_STEM = f"{RESET}je{RED}tt{RESET}er"

        if TARGET == "reléguer":
            PRESENT_STEM = "rel" + red("è") + "gu"
            NOUS_VOUS_PRESENT_STEM = RESET + STEM

    if ENDING == "ir":
        present_endings = ["is", "is", "it", "issons", "issez", "issent"]
        passe_simple_endings = ["is", "is", "it", "îmes", "îtes", "irent"]
        past_participle_ending = "i"
        if TARGET == "asseoir":
            PRESENT_JE_TU_IL_STEM = "assied"
            NOUS_VOUS_PRESENT_STEM = "assey"
            ils_present_use_nous_stem = True
            present_endings = ["s", "s", "", "ons", "ez", "ent"]
            FUTURE_CONDITIONAL_STEM = "assiér"
            past_participle = "assis"
            PASSE_SIMPLE_STEM = "ass"
            note = "assois and similar are the old conjugation form"
        if TARGET == "avoir":
            FUTURE_CONDITIONAL_STEM = red("aur")
            PASSE_SIMPLE_STEM = red("e")
            passe_simple_endings = u_passe_simple_pattern
        elif TARGET == "choir":
            NOUS_VOUS_PRESENT_STEM = "cho" + red("y")
            PRESENT_STEM = "cho" + red("i")
            present_endings = sst_present_pattern
            past_participle = "chu"
            smart_passe_simple = True
            defects = ["imperfect", "subjunctive", "imperfect_subjunctive", "imperative"]
        elif TARGET == "devoir":
            PRESENT_STEM = start_red("doi")
            NOUS_VOUS_PRESENT_STEM = red("dev")
            ILS_PRESENT_STEM = "doiv"
            FUTURE_CONDITIONAL_STEM = "devr"
            present_endings = sst_present_pattern
            past_participle = "dû"
            PASSE_SIMPLE_STEM = red("d")
        elif TARGET == "faillir":
            note = "only normally used in passé composé"
        elif TARGET == "falloir":
            defects = ["non_il"]
            NOUS_VOUS_PRESENT_STEM = "fall"
            FUTURE_CONDITIONAL_STEM = "faudr"
            PASSE_SIMPLE_STEM = "fall"
            passe_simple_endings = u_passe_simple_pattern
            past_participle = "fallu"
            SUBJUNCTIVE_STEM = "faill"
        elif TARGET == "mourir":
            PRESENT_STEM = f"{RED}meur{RESET}"
            NOUS_VOUS_PRESENT_STEM = "mour"
            present_endings = sst_present_pattern
            FUTURE_CONDITIONAL_STEM = f"mour{RED}r{RESET}"
            PASSE_SIMPLE_STEM += RED
            passe_simple_endings = u_passe_simple_pattern
        elif TARGET == "pleuvoir":
            defects = ["non_il"]
            PRESENT_STEM = "pleu"
            present_endings = sst_present_pattern
            NOUS_VOUS_PRESENT_STEM = "pleuv"
            ils_present_use_nous_stem = True
            FUTURE_CONDITIONAL_STEM = "pleuvr"
            PASSE_SIMPLE_STEM = "pl"
            passe_simple_endings = u_passe_simple_pattern
            past_participle = red("plu")
        elif TARGET == "pouvoir":
            FUTURE_CONDITIONAL_STEM = f"{RED}pourr{RESET}"
            PASSE_SIMPLE_STEM = start_red("p")
            defects = "imperative"
        elif TARGET == "savoir":
            PRESENT_STEM = f"{RED}sai"
            NOUS_VOUS_PRESENT_STEM = f"{RED}sav{RESET}"
            ils_present_use_nous_stem = True
            present_endings = sst_present_pattern
            SUBJUNCTIVE_STEM = f"{RED}sach{RESET}"
            PASSE_SIMPLE_STEM = f"{RED}s{RESET}"
            FUTURE_CONDITIONAL_STEM = "saur"
        elif TARGET == "valoir":
            PRESENT_STEM = "v"
            present_endings = ["aux", "aux", "aut", "ons", "ez", "ent"]
            NOUS_VOUS_PRESENT_STEM = "val"
            ils_present_use_nous_stem = True
            FUTURE_CONDITIONAL_STEM = "vaudr"
            PASSE_SIMPLE_STEM = f"{RED}val"
            passe_simple_endings = u_passe_simple_pattern
        elif TARGET == "voir":
            FUTURE_CONDITIONAL_STEM = "verr"
            PASSE_SIMPLE_STEM = f"v{RED}"
            SUBJUNCTIVE_NOUS_STEM = red("voy")
        elif TARGET == "vouloir":
            PRESENT_STEM = red("v")
            NOUS_VOUS_PRESENT_STEM = red("voul")
            present_endings = [red("eux"), red("eux"), red("eut"), "ons", "ez", red("eul") + "ent"]
            FUTURE_CONDITIONAL_STEM = "voudr"
            SUBJUNCTIVE_STEM = red("veuill")
            PASSE_SIMPLE_STEM = red("voul")
            SUBJUNCTIVE_NOUS_STEM = "voul"
            passe_simple_endings = u_passe_simple_pattern
            past_participle = "voulu"

    if ENDING == "ïr":
        present_endings = [f"{RED}is", f"{RED}is", f"{RED}it", "ïssons", "ïssez", "ïssent"]
        passe_simple_endings = ["ïs", "ïs", "ït", "ïmes", "ïtes", "ïrent"]
        past_participle_ending = "ï"

    if ENDING == "re":
        present_endings = ["s", "s", "", "ons", "ez", "ent"]
        if TARGET == "naître":  
            PASSE_SIMPLE_STEM = f"na{RED}qu{RESET}"
        elif TARGET == "nuire":
            PASSE_SIMPLE_STEM = f"nui{RED}s{RESET}"
        elif TARGET == "plaire":
            PASSE_SIMPLE_STEM = f"pl{RED}"
        passe_simple_endings = ["is", "is", "it", "îmes", "îtes", "irent"]
        past_participle_ending = "u"
        if TARGET == "boire":
            NOUS_VOUS_PRESENT_STEM = f"{RED}buv{RESET}"
            SUBJUNCTIVE_NOUS_STEM = "buv"
            PASSE_SIMPLE_STEM = f"{RED}b"
            passe_simple_endings = u_passe_simple_pattern
        elif TARGET == "connaître":
            pass
        elif TARGET == "craindre":
            PRESENT_STEM = f"{RED}craign{RESET}"
        elif TARGET == "croire":
            NOUS_VOUS_PRESENT_STEM = f"cro{RED}y{RESET}"
            il_add_t()
            PASSE_SIMPLE_STEM = RED + "cr"
            passe_simple_endings = u_passe_simple_pattern
        elif TARGET == "croître":
            PRESENT_JE_TU_IL_STEM = "croî"
            NOUS_VOUS_PRESENT_STEM = "croiss"
            ils_present_use_nous_stem = True
            present_endings = sst_present_pattern
            past_participle = "crû"
            PASSE_SIMPLE_STEM = "cr"
            passe_simple_endings = û_passe_simple_pattern
        elif TARGET == "être":
            PASSE_SIMPLE_STEM = f"{RED}f"
            passe_simple_endings = u_passe_simple_pattern
            FUTURE_CONDITIONAL_STEM = "ser"
            subjunctive_endings = ["s", "s", "t", "ons", "ez", "ent"]
            SUBJUNCTIVE_STEM = start_red("soi")
            SUBJUNCTIVE_NOUS_STEM = "soy"
        elif TARGET == "frire":
            defects = ["nous", "ils", "passe_simple"]
        elif TARGET == "inclure":
            PASSE_SIMPLE_STEM = f"{RED}incl{RESET}"
            il_add_t()
            passe_simple_endings = u_passe_simple_pattern
        elif TARGET == "lire":
            PRESENT_STEM = f"{RED}li"
            NOUS_VOUS_PRESENT_STEM = f"{RED}lis{RESET}"
            ils_present_use_nous_stem = True
            present_endings = sst_present_pattern
            PASSE_SIMPLE_STEM = f"{RED}l"
        elif is_target_ends("mettre"):
            p1 = TARGET[:-6]
            PRESENT_JE_TU_IL_STEM = p1 + "met"
            PASSE_SIMPLE_STEM = p1 + red("m")
            passe_simple_endings = i_passe_simple_pattern
            past_participle = p1 + "mis"
        elif TARGET == "moudre":
            NOUS_VOUS_PRESENT_STEM = f"mou{RED}l{RESET}"
            ils_present_use_nous_stem = True
            PASSE_SIMPLE_STEM = f"mou{RED}l{RESET}"
        elif TARGET == "peindre":
            PRESENT_JE_TU_IL_STEM = "pein"
            present_endings = sst_present_pattern
            NOUS_VOUS_PRESENT_STEM = "peign"
            ils_present_use_nous_stem = True
            past_participle = red("peint")
            PASSE_SIMPLE_STEM = "peign"
            passe_simple_endings = i_passe_simple_pattern
        elif TARGET == "plaire":
            passe_simple_endings = u_passe_simple_pattern
            past_participle_ending = "u"
        elif TARGET == "suivre":
            PRESENT_JE_TU_IL_STEM = "sui"
            present_endings = sst_present_pattern
            past_participle_ending = red("i")
            passe_simple_endings = i_passe_simple_pattern
        elif TARGET == "taire":
            il_add_t()
            NOUS_VOUS_PRESENT_STEM = "tai" + red("s")
            ils_present_use_nous_stem = True
            PASSE_SIMPLE_STEM = red("t")
            passe_simple_endings = u_passe_simple_pattern
            past_participle = "tu"
        elif TARGET == "traire":
            NOUS_VOUS_PRESENT_STEM = "tray"
            SUBJUNCTIVE_NOUS_STEM = "tray"
        elif TARGET == "vaincre":
            NOUS_VOUS_PRESENT_STEM = f"{RESET}vain{RED}qu{RESET}"
            ils_present_use_nous_stem = True
            PASSE_SIMPLE_STEM = f"{RESET}vain{RED}qu"
            passe_simple_endings = i_passe_simple_pattern

    if is_target_ends("aître"):
        p1 = TARGET[:-5]
        PRESENT_STEM = p1 + "a"
        present_endings = ["is", "is", "ît", "issons", "issez", "issent"]
        past_participle = p1 + "u"
        PASSE_SIMPLE_STEM = "appar"
        passe_simple_endings = u_passe_simple_pattern

    if is_target_ends("cevoir"):
        p1 = TARGET[:-6]
        PRESENT_STEM = p1 + red("çoi")
        NOUS_VOUS_PRESENT_STEM = p1 + "cev"
        ILS_PRESENT_STEM = p1 + "çoiv"
        present_endings = sst_present_pattern
        FUTURE_CONDITIONAL_STEM = p1 + "cev" + red("r")
        PASSE_SIMPLE_STEM = p1 + "ç"
        passe_simple_endings = u_passe_simple_pattern
        past_participle = p1 + "çu"

    if is_target_ends("courir"):
        p1 = TARGET[:-2]
        PRESENT_STEM = p1
        present_endings = sst_present_pattern
        FUTURE_CONDITIONAL_STEM = p1 + red("r")
        PASSE_SIMPLE_STEM = p1
        passe_simple_endings = u_passe_simple_pattern
        past_participle = p1 + red("u")

    if is_target_ends("dire"):
        PRESENT_STEM = TARGET[:-2]
        il_add_t()
        present_endings[3] = red("s") + "ons"
        present_endings[4] = red("tes")
        present_endings[5] = red("s") + "ent"
        past_participle = TARGET[:-2] + red("t")
        PASSE_SIMPLE_STEM = red(TARGET[:-3])

    if TARGET[-4:] == "enir":
        remainder = TARGET[:-4]
        PRESENT_STEM = remainder + f"{RED}ien"
        present_endings = sst_present_pattern
        NOUS_VOUS_PRESENT_STEM = remainder + f"{RED}en{RESET}"
        SUBJUNCTIVE_NOUS_STEM = remainder + "en"
        present_endings[5] = f"n{RESET}ent"
        FUTURE_CONDITIONAL_STEM = remainder + "iendr"
        past_participle_ending = RED + "u"
        PASSE_SIMPLE_STEM = remainder
    

    if TARGET[-5:] == "faire":
        il_add_t()
        present_endings[3] = f"{RED}s{RESET}ons"
        present_endings[4] = f"{RED}tes"
        FUTURE_CONDITIONAL_STEM = TARGET[:-4] + "er"
        past_participle_ending = RED + "t"
        PASSE_SIMPLE_STEM = RED + TARGET[:-4] + RESET

    if TARGET[-4:] == "fire":
        il_add_t()
        NOUS_VOUS_PRESENT_STEM += STEM + RED + "s" + RESET
        ils_present_use_nous_stem = True
        PASSE_SIMPLE_STEM = RED + TARGET[:-3] + RESET
        if TARGET != "suffire":
            past_participle_ending = RED + "t"

    if is_target_ends("indre"):
        PRESENT_JE_TU_IL_STEM = TARGET[:-3]
        NOUS_VOUS_PRESENT_STEM = RESET + TARGET[:-4] + RED + "gn" + RESET
        ils_present_use_nous_stem = True
        present_endings = sst_present_pattern
        past_participle = TARGET[:-3] + RED + "t"
        PASSE_SIMPLE_STEM =  RED + NOUS_VOUS_PRESENT_STEM
        passe_simple_endings = i_passe_simple_pattern
    
    if is_target_ends("mouvoir"):
        p1 = TARGET[:-7]
        PRESENT_JE_TU_IL_STEM = p1 + "meu"
        NOUS_VOUS_PRESENT_STEM = p1 + "mouv"
        ILS_PRESENT_STEM = p1 + "meuv"
        FUTURE_CONDITIONAL_STEM = p1 + "mouvr"
        present_endings = sst_present_pattern
        past_participle = p1 + "mû"
        PASSE_SIMPLE_STEM = p1 + "m"
        passe_simple_endings = u_passe_simple_pattern


    if TARGET[-7:] == "prendre":
        NOUS_VOUS_PRESENT_STEM = red(STEM[:-1])
        SUBJUNCTIVE_NOUS_STEM = TARGET[:-3]
        PASSE_SIMPLE_STEM = RED + TARGET[:-5] + RESET

    if is_target_ends("quérir"):
        p1 = TARGET[:-6]
        PRESENT_JE_TU_IL_STEM = p1 + "quier"
        NOUS_VOUS_PRESENT_STEM = p1 + red("quér")
        ILS_PRESENT_STEM = p1 + "quièr"
        FUTURE_CONDITIONAL_STEM = p1 + "querr"
        PASSE_SIMPLE_STEM = p1 + "qu"
        past_participle = p1 + red("quis")
        present_endings = sst_present_pattern


    if is_target_ends("rire"):
        il_add_t()
        PASSE_SIMPLE_STEM = red(TARGET[:-3])

    if TARGET[-5:] == "crire":
        NOUS_VOUS_PRESENT_STEM += RED + "v" + RESET
        ils_present_use_nous_stem = True
        PASSE_SIMPLE_STEM += f"{RED}iv{RESET}"

    if TARGET[-6:] == "rompre":
        il_add_t()

    if is_target_ends("soudre"):
        p1 = TARGET[:-6]
        PRESENT_JE_TU_IL_STEM = p1 + "sou"
        NOUS_VOUS_PRESENT_STEM = p1 + "solv"
        ils_present_use_nous_stem = True
        present_endings = sst_present_pattern
        past_participle = p1 + "solu"
        if TARGET == "absoudre":
            past_participle = "absous"
        PASSE_SIMPLE_STEM = p1 + "sol"
        passe_simple_endings = u_passe_simple_pattern


    if is_target_ends("tir") or is_target_ends("mir") or is_target_ends("vir"):
        remainder = TARGET[:-3]
        PRESENT_STEM = f"{remainder}{RED}"
        NOUS_VOUS_PRESENT_STEM = PRESENT_STEM + TARGET[-3] + RESET
        present_endings = sst_present_pattern
        ils_present_use_nous_stem = True
        if TARGET == "vêtir":
            present_endings[0] = red("ts")
            present_endings[1] = red("ts")
            past_participle = "vêtu"

    if is_target_ends("llir") or is_target_ends("frir") or is_target_ends("vrir"):
        if TARGET != "faillir":
            r1 = TARGET[:-4]
            r2 = TARGET[-4:-2]
            PRESENT_STEM = r1 + r2 + RED
            present_endings = er_present_pattern
            PAST_PARTCIPLE_STEM = r1 + r2[0] + RED
            if is_target_ends("llir"):
                if TARGET == "bouillir":
                    PRESENT_JE_TU_IL_STEM = "bou"
                    present_endings = sst_present_pattern
                    FUTURE_CONDITIONAL_STEM = TARGET
                else:
                    FUTURE_CONDITIONAL_STEM = r1 + "ll" + RED + "e" + RESET + "r"
                past_participle_ending = "li"
            else:
                past_participle_ending = "ert"

    if TARGET[-4:] == "uire":
        present_endings = ["s", "s", f"{RED}t{RESET}", f"{RED}s{RESET}ons", f"{RED}s{RESET}ez", f"{RED}s{RESET}ent"]
        PASSE_SIMPLE_STEM = STEM + f"{RED}s{RESET}"

    if TARGET[-5:] == "vivre":
        PRESENT_STEM = f"{RED}{TARGET[:-3]}"
        NOUS_VOUS_PRESENT_STEM = TARGET[:-2]
        present_endings[2] = f"{RED}t"
        present_endings[5] = f"{RED}v{RESET}ent"
        PASSE_SIMPLE_STEM = f"{TARGET[:-4]}{RED}éc"
        passe_simple_endings = u_passe_simple_pattern


        
    # PRESENT ***********************************
    present = [f"{PRESENT_STEM}{j}" for j in present_endings]
    if NOUS_VOUS_PRESENT_STEM:
        NOUS_VOUS_PRESENT_STEM = red(NOUS_VOUS_PRESENT_STEM)
        for i in [3, 4]:
            present[i] = f"{NOUS_VOUS_PRESENT_STEM}{present_endings[i]}"
    if PRESENT_JE_TU_IL_STEM:
        PRESENT_JE_TU_IL_STEM = red(PRESENT_JE_TU_IL_STEM)
        for i in [0, 1, 2]:
            present[i] = f"{PRESENT_JE_TU_IL_STEM}{present_endings[i]}"
    if ILS_PRESENT_STEM:
        ILS_PRESENT_STEM = red(ILS_PRESENT_STEM)
        present[5] = f"{ILS_PRESENT_STEM}{present_endings[5]}"
    if ils_present_use_nous_stem:
        present[5] = f"{NOUS_VOUS_PRESENT_STEM}{present_endings[5]}"
    if TARGET == "avoir":
        present = ["ai", "as", "a", f"av{RESET}ons", f"av{RESET}ez", "ont"]
        present = [start_red(i) for i in present]
    elif TARGET == "battre":
        p1 = f"bat{RED}s"
        p2 = f"{RED}bat"
        present = [p1, p1, p2] + present[3:]
    elif TARGET == "boire":
        il_add_t()
        present[5] = f"boi{RED}v{RESET}ent"
    elif TARGET == "craindre":
        p1 = f"{RED}crains"
        p2 = f"{RED}craint"
        present = [p1, p1, p2] + present[3:]
        PASSE_SIMPLE_STEM = f"{RED}craign{RESET}"
    elif TARGET == "être":
        present = red(["suis", "es", "est", "sommes", "êtes", "sont"])
    elif TARGET == "falloir":
        present[2] = "faut"
    elif TARGET == "lire":
        p1 = f"{RED}lis"
        p2 = f"{RED}lit"
        present = [p1, p1, p2] + present[3:]
    elif TARGET == "luire":
        present[2] = RED + "lui"
    elif TARGET == "naître":
        p1 = f"na{RED}is"
        p2 = f"na{RED}iss{RESET}"
        present = [p1, p1, present[2], p2 + "ons", p2 + "ez", p2 + "ent"]
    elif TARGET == "plaire":
        p1 = f"plai{RED}s"
        present = present[:2] + [f"pla{RED}ît", p1 + "ons", p1 + "ez", p1 + "ent"]
    elif TARGET == "pouvoir":
        p1 = f"{RED}peux"
        p2 = f"{RED}peut"
        p3 = f"{RED}pouv{RESET}"
        p4 = f"{RED}peuvent"
        present = [p1, p1, p2, p3 + "ons", p3 + "ez", p4]
    elif TARGET == "voir":
        p1 = f"vo{RED}y{RESET}"
        present = present[:3] + [p1 + "ons", p1 + "ez", f"vo{RED}i{RESET}ent"]
    if TARGET[-5:] == "faire":
        present[5] = RED + TARGET[:-4] + "ont"
    if TARGET[-7:] == "prendre":
        present[5] = f"{TARGET[:-3]}{RED}n{RESET}ent"
    if SUBJUNCTIVE_STEM == "":
        SUBJUNCTIVE_STEM = present[5][:-3]
    special_subjunctives = {
        "avoir": "ai",
        "pouvoir": "puiss",
        "valoir": "vaill",
    }
    for k, v in special_subjunctives.items():
        if TARGET == k:
            SUBJUNCTIVE_STEM = f"{RED}{v}{RESET}"
    if TARGET[-5:] == "faire":
        SUBJUNCTIVE_STEM = RED + TARGET[:-4] + "ass" + RESET
    IMPERFECT_STEM = present[3][:-3]
    if any([
        TARGET[-4:] == "ager",
        TARGET[-5:] == "anger",
    ]):
        IMPERFECT_STEM = present[3][:-4]
    if TARGET == "être":
        IMPERFECT_STEM = f"{RED}ét{RESET}"
    if TARGET == "falloir":
        IMPERFECT_STEM = "fall"
    imperfect = [f"{IMPERFECT_STEM}{j}" for j in imperfect_endings]
    if FUTURE_CONDITIONAL_STEM:
        FUTURE_CONDITIONAL_STEM = red(FUTURE_CONDITIONAL_STEM)
    else:
        FUTURE_CONDITIONAL_STEM = TARGET[:-1] if ENDING == "re" else TARGET
    future = [f"{FUTURE_CONDITIONAL_STEM}{j}" for j in future_endings]
    conditional = [f"{FUTURE_CONDITIONAL_STEM}{j}" for j in conditional_endings]

    # subjunctive
    subjunctive = [f"{SUBJUNCTIVE_STEM}{j}" for j in subjunctive_endings]
    if SUBJUNCTIVE_NOUS_STEM:
        subjunctive[3] = RED + SUBJUNCTIVE_NOUS_STEM + RESET + subjunctive_endings[3]
        subjunctive[4] = RED + SUBJUNCTIVE_NOUS_STEM + RESET + subjunctive_endings[4]

    if TARGET == "avoir":
        subjunctive[2] = f"{RED}ait"
        subjunctive[3] = f"{RED}ay{RESET}ons"
        subjunctive[4] = f"{RED}ay{RESET}ez"
    if TARGET == "croire":
        subjunctive[3] = f"cro{RED}y{RESET}ions"
        subjunctive[4] = f"cro{RED}y{RESET}iez"
    
    # imperative
    imperative = deepcopy(present)
    if ENDING == "er" or present[1][-2:] == "es":
        imperative[1] = imperative[1][:-1]
    if TARGET == "avoir":
        imperative[1] = f"{RED}aie"
        imperative[3] = f"{RED}ay{RESET}ons"
        imperative[4] = f"{RED}ay{RESET}ez"        
    if TARGET == "savoir":
        imperative = deepcopy(subjunctive)
        imperative[1] = f"{RED}sache"
    elif TARGET == "être":
        imperative[1] = f"{RED}sois"
        imperative[3] = f"{RED}soy{RESET}ons"
        imperative[4] = f"{RED}soy{RESET}ez"
    if is_reflexive:
        imperative[1] += "-toi"
        imperative[3] += "-nous"
        imperative[4] += "-vous"
    present_participle = present[3][:-3] + "ant"

    # past participle
    if past_participle:
        past_participle = red(past_participle)
    elif past_participle == "":
        past_participle = PAST_PARTCIPLE_STEM + past_participle_ending
    if TARGET[-7:] == "prendre":
        past_participle = f"{TARGET[:-5]}{RED}is"
    if TARGET[-4:] == "rire":
        past_participle = f"{TARGET[:-4]}{RED}ri"
    if TARGET[-5:] == "crire":
        past_participle += "t"
    if TARGET[-4:] == "uire":
        past_participle = f"{STEM}{RED}t"
    if TARGET[-5:] == "vivre":
        past_participle = f"{TARGET[:-4]}{RED}écu"
    irregular_past_participles = {
        "avoir": "eu",
        "battre": "battu",
        "boire": "bu",
        "craindre": "craint",
        "croire": "cru",
        "être": "été",
        "frire": "frit",
        "inclure": "inclus",
        "lire": "lu",
        "luire": "lui",
        "moudre": "moulu",
        "mourir": "mort",
        "naître": "né",
        "nuire": "nui",
        "plaire": "plu",
        "pouvoir": "pu",
        "savoir": "su",
        "valoir": "valu",
        "voir": "vu",
    }
    for k, v in irregular_past_participles.items():
        if TARGET == k:
            past_participle = f"{RED}{v}"

    if TARGET == "être":
        present_participle = f"{RED}étant"
            
    # passe simple and imperfect subjunctive
    if smart_passe_simple:
        PASSE_SIMPLE_STEM = remove_text_colour(past_participle)[:-1]
        if remove_text_colour(past_participle)[-1] == "u":
            passe_simple_endings = u_passe_simple_pattern
        elif remove_text_colour(past_participle)[-1] == "i":
            passe_simple_endings = i_passe_simple_pattern
        else:
            raise Exception(f"smart passe simple vowel error: past partciple = {past_participle}")
    if past_participle[-1] in ["u", "û"] and TARGET not in ["vaincre", "suffire"]:
        passe_simple_endings = u_passe_simple_pattern
    if is_target_ends("enir"):
        passe_simple_endings = in_passe_simple_pattern
    passe_simple = [f"{PASSE_SIMPLE_STEM}{j}" for j in passe_simple_endings]
    IMPERFECT_SUBJUNCTIVE_STEM = passe_simple[2][:-2]
    extra_imperfect_subjunctive_letter = ""
    if is_target_ends("er"):
        IMPERFECT_SUBJUNCTIVE_STEM = passe_simple[2][:-1]
        vowel = "a"
    else:
        vowel = remove_codes(passe_simple[2])[-2]
    if vowel == "n":
        IMPERFECT_SUBJUNCTIVE_STEM = IMPERFECT_SUBJUNCTIVE_STEM[:-1]
        vowel = remove_codes(passe_simple[2])[-3]
        extra_imperfect_subjunctive_letter = "n"
    imperfect_subjunctive_endings = ["sse", "sses", "t", "ssions", "ssiez", "ssent"]
    imperfect_subjunctive_endings = [vowel + extra_imperfect_subjunctive_letter + RESET + i for i in imperfect_subjunctive_endings]
    if vowel == "a":
        imperfect_subjunctive_endings[2] = f"â"
    elif vowel == "i":
        imperfect_subjunctive_endings[2] = f"î"
    elif vowel == "ï":
        imperfect_subjunctive_endings[2] = f"ï"
    elif vowel == "u" or vowel == "û":
        imperfect_subjunctive_endings[2] = f"û"
    else:
        raise Exception("vowel missing for imperfect subjunctive")
    imperfect_subjunctive_endings[2] += extra_imperfect_subjunctive_letter + RESET + "t"
    imperfect_subjunctive = [f"{IMPERFECT_SUBJUNCTIVE_STEM}{j}" for j in imperfect_subjunctive_endings]

    tenses = [
        present, 
        imperfect, 
        future, 
        conditional,
        subjunctive, 
        imperfect_subjunctive, 
        passe_simple, 
        imperative,
    ]
    for tense in tenses:
        for pronoun in range(6):
            if any([
                tense is imperative and pronoun in [0, 2, 5],
                pronoun == 3 and "nous" in defects and (tense is present or tense is imperative),
                pronoun == 4 and "nous" in defects and (tense is present or tense is imperative),
                pronoun == 5 and "ils" in defects and tense is present,
                pronoun != 2 and "non_il" in defects,
                "nous" in defects and tense is imperfect,
                "ils" in defects and tense is subjunctive,
                "passe_simple" in defects and tense is passe_simple,
                "passe_simple" in defects and tense is imperfect_subjunctive,
                "imperative" in defects and tense is imperative,
                "imperfect" in defects and tense is imperfect,
                "subjunctive" in defects and tense is subjunctive,
            ]):
                tense[pronoun] = "-"

    if "nous" in defects:
        present_participle = "-"

    if is_target_ends("cer"):
        ç_endings = [
            "ons",
            "ais",
            "ait",
            "aient",
            "asse",
            "asses",
            "ât",
            "assions",
            "assiez",
            "assent",
            "ai",
            "as",
            "a",
            "âmes",
            "âtes",
            "ant",
        ]

        for i in range(8):
            for j in range(6):
                for k in ç_endings:
                    tenses[i][j] = re.sub(f"c{k}", red("ç") + k, tenses[i][j])
        imperfect_subjunctive[2] = TARGET[:-3] + red("ç") + "ât" 


    output = { 
        "tense": {
            "present": present,
            "imperfect": imperfect, 
            "future": future, 
            "conditional": conditional,
            "subjunctive": subjunctive, 
            "imperfect_subjunctive": imperfect_subjunctive, 
            "passe_simple": passe_simple, 
            "imperative": imperative,
        },
        "present_participle": present_participle,
        "past_participle": past_participle,
        "auxillary": AUXILLARY,
        "is_reflexive": is_reflexive,
        "defects": defects,
        "note": note
    }

    return output


pronoun_number = {
    "je": 0,
    "tu": 1,
    "il": 2,
    "elle": 2,
    "on": 2,
    "nous": 3,
    "vous": 4,
    "ils": 5,
    "elles": 5,
    "il/elle/on": 2,
    "ils/elles": 5,
}


def remove_text_colour(x):
    return x.replace(RED, "").replace(RESET, "")


def get_tense_conjugation_from_verb(verb_in, tense, pronoun=""):
    return get_tense_conjugation(verb_conjugator(verb_in), tense, pronoun)


def get_tense_conjugation_by_pronoun(verb_in, pronoun):
    o = verb_conjugator(verb_in)
    return [remove_text_colour(o["tense"][tense][pronoun_number[pronoun]]) for tense in o["tense"].keys()]


def get_tense_conjugation(dict_in, tense, pronoun=""):
    if not pronoun:
        return [remove_text_colour(i) for i in dict_in["tense"][tense]]
    return remove_text_colour(dict_in["tense"][tense][pronoun_number[pronoun]])

def print_conjugation(dict_in):
    PRONOUNS = ["je", "tu", "il/elle/on", "nous", "vous", "ils/elles"]
    tenses = list(dict_in["tense"].values())
    is_reflexive = dict_in["is_reflexive"]
    if is_reflexive:
        PRONOUNS = ["je me", "tu te", "il/elle/on se", "nous nous", "vous vous", "ils/elles se"]
    if "non_il" in dict_in["defects"]:
        PRONOUNS[2] = "il"

    def justify(x: str, number_char):
        spaces = number_char - len(remove_text_colour(x))
        if spaces > 0:
            return x + " " * spaces
        return x
    

    s1 = f"\n{" "*16}{'PRESENT':15} {'IMPERFECT':15} {'FUTURE':15} {'CONDITIONAL':15}"
    s2 = f"\n{" "*16}{'SUBJUNCTIVE':15} {'IMP. SUBJ.':15} {'PASSE SIMPLE':15} {'IMPERATIVE':15}"
    for k in [[s1, tenses[:4]], [s2, tenses[4:]]]:
        print(k[0])
        for pronoun in range(6):
            print(f"{PRONOUNS[pronoun].rjust(15)}", end=" ")
            for tense in k[1]:
                print(justify(f"{tense[pronoun]}", 15), end=" ")
                print(f"{RESET}", end="")
            print("")
    print(f"\nPRESENT PARTCIPLE = {dict_in["present_participle"]}{RESET}")
    print(f"   PAST PARTCIPLE = {dict_in["past_participle"]}{RESET}")
    print(f"        AUXILLARY = {dict_in["auxillary"]}")
    note = dict_in["note"]
    if note:
        print(f"{RED}NOTE: {note}")


if __name__ == "__main__":
    choice = input("which verb would you like the conjugation for?\n")
    print_conjugation(verb_conjugator(choice))
