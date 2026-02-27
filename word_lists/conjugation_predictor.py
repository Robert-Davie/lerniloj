from copy import deepcopy

while True:
    TARGET = input("which verb would you like the conjugation for?").lower()


    RED = "\033[0;31m"
    RESET = "\033[0m"
    PRONOUNS = ["je", "tu", "il/elle/on", "nous", "vous", "ils/elles"]

    TARGET = TARGET.lower()
    ENDING = TARGET[-2:]
    STEM = TARGET[:-2]

    PRESENT_STEM = STEM
    NOUS_VOUS_PRESENT_STEM = STEM
    ils_present_use_nous_stem = False
    FUTURE_CONDITIONAL_STEM = STEM
    SUBJUNCTIVE_STEM = STEM
    IMPERFECT_SUBJUNCTIVE_STEM = STEM
    PASSE_SIMPLE_STEM = STEM
    defects = []
    AUXILLARY = "avoir"

    if TARGET in [
        "naître"
    ]:
        AUXILLARY = f"{RED}être"


    def justify(x: str, number_char):
        spaces = number_char - len(x.replace(RED, "").replace(RESET, ""))
        if spaces > 0:
            return x + " " * spaces
        return x


    def remove_codes(x):
        return x.replace(RED, "").replace(RESET, "")


    def il_add_t():
        present_endings[2] += RED + "t"


    imperfect_endings = ["ais", "ais", "ait", "ions", "iez", "aient"]
    future_endings = ["ai", "as", "a", "ons", "ez", "ont"]
    conditional_endings = ["ais", "ais", "ait", "ions", "iez", "aient"]
    subjunctive_endings = ["e", "es", "e", "ions", "iez", "ent"]

    er_present_pattern = present_endings = ["e", "es", "e", "ons", "ez", "ent"]
    sst_present_pattern = [f"{RED}s", f"{RED}s", f"{RED}t", "ons", "ez", "ent"]
    u_passe_simple_pattern = [f"u{RESET}s", f"u{RESET}s", f"ut", f"û{RESET}mes", f"û{RESET}tes", f"u{RESET}rent"]

    if ENDING == "er":
        present_endings = er_present_pattern
        FUTURE_CONDITIONAL_STEM = STEM + "er"
        passe_simple_endings = ["ai", "as", "a", "âmes", "âtes", "èrent"]
        past_participle_ending = "é"

        if any([
            TARGET[-4:] == "ager",
            TARGET[-5:] == "anger",
        ]):
            present_endings[3] = RED + "e" + RESET + "ons"
            imperfect_endings = ["eais", "eais", "eait", "ions", "iez", "eaient"]
            IMPERFECT_SUBJUNCTIVE_STEM += "e"
            passe_simple_endings = ["e" + k for k in passe_simple_endings[:-1]] + ["èrent"]
            present_participle_ending = "eant"

    if ENDING == "ir":
        present_endings = ["is", "is", "it", "issons", "issez", "issent"]
        FUTURE_CONDITIONAL_STEM = STEM + "ir"
        passe_simple_endings = ["is", "is", "it", "îmes", "îtes", "irent"]
        past_participle_ending = "i"
        if TARGET == "avoir":
            FUTURE_CONDITIONAL_STEM = f"{RED}aur{RESET}"
            PASSE_SIMPLE_STEM = f"{RED}e{RESET}"
            passe_simple_endings = u_passe_simple_pattern
        elif TARGET == "dormir":
            NOUS_VOUS_PRESENT_STEM = f"{RED}dorm{RESET}"
            PRESENT_STEM = f"{RED}dor"
            present_endings = ["s", "s", "t", "ons", "ez", f"m{RESET}ent"]
        elif TARGET == "mourir":
            PRESENT_STEM = f"{RED}meur{RESET}"
            NOUS_VOUS_PRESENT_STEM = "mour"
            present_endings = sst_present_pattern
            FUTURE_CONDITIONAL_STEM = f"mour{RED}r{RESET}"
            PASSE_SIMPLE_STEM += RED
            passe_simple_endings = u_passe_simple_pattern
        elif TARGET == "offrir":
            present_endings = [RED + i for i in er_present_pattern]
        elif TARGET == "pouvoir":
            FUTURE_CONDITIONAL_STEM = f"{RED}pourr{RESET}"
            PASSE_SIMPLE_STEM = f"p{RED}"
            passe_simple_endings = u_passe_simple_pattern
            defects = "imperative"
        elif TARGET == "valoir":
            FUTURE_CONDITIONAL_STEM = f"{RED}vaudr{RESET}"
            PASSE_SIMPLE_STEM = f"{RED}val"
            passe_simple_endings = u_passe_simple_pattern
        elif TARGET == "venir":
            FUTURE_CONDITIONAL_STEM = f"{RED}viendr{RESET}"
            PASSE_SIMPLE_STEM = f"{RED}v"
            passe_simple_endings = [i[:1] + f"n" + i[1:] for i in passe_simple_endings]
        elif TARGET == "voir":
            FUTURE_CONDITIONAL_STEM = f"{RED}verr{RESET}"
            PASSE_SIMPLE_STEM = f"v{RED}"

    if ENDING == "ïr":
        present_endings = [f"{RED}is", f"{RED}is", f"{RED}it", "ïssons", "ïssez", "ïssent"]
        FUTURE_CONDITIONAL_STEM = STEM + "ïr"
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
        FUTURE_CONDITIONAL_STEM = STEM + "r"
        passe_simple_endings = ["is", "is", "it", "îmes", "îtes", "irent"]
        past_participle_ending = "u"
        if TARGET == "boire":
            NOUS_VOUS_PRESENT_STEM = f"{RED}buv{RESET}"
            PASSE_SIMPLE_STEM = f"{RED}b"
            passe_simple_endings = u_passe_simple_pattern
        elif TARGET == "craindre":
            PRESENT_STEM = f"{RED}craign{RESET}"
        elif TARGET == "croire":
            NOUS_VOUS_PRESENT_STEM = f"cro{RED}y{RESET}"
            il_add_t()
            PASSE_SIMPLE_STEM = RED + "cr"
            passe_simple_endings = u_passe_simple_pattern
        elif TARGET == "être":
            PASSE_SIMPLE_STEM = f"{RED}f"
            passe_simple_endings = u_passe_simple_pattern
            subjunctive_endings = ["ois", "ois", "oit", "oyons", "oyez", "oient"]
            FUTURE_CONDITIONAL_STEM = f"{RED}serr{RESET}"
        elif TARGET == "frire":
            defects = ["nous", "ils", "passe_simple"]
        elif TARGET == "inclure":
            PASSE_SIMPLE_STEM = f"{RED}incl{RESET}"
            passe_simple_endings = u_passe_simple_pattern
        elif TARGET == "lire":
            PRESENT_STEM = f"{RED}li"
            NOUS_VOUS_PRESENT_STEM = f"{RED}lis{RESET}"
            ils_present_use_nous_stem = True
            present_endings = sst_present_pattern
            PASSE_SIMPLE_STEM = f"{RED}l"
        elif TARGET == "moudre":
            NOUS_VOUS_PRESENT_STEM = f"mou{RED}l{RESET}"
            ils_present_use_nous_stem = True
            PASSE_SIMPLE_STEM = f"mou{RED}l{RESET}"
            passe_simple_endings = u_passe_simple_pattern
            passe_simple_endings = [f"{RED}{i[0]}{i[1:]}" for i in passe_simple_endings]
        elif TARGET == "plaire":
            passe_simple_endings = u_passe_simple_pattern
            past_participle_ending = "u"

    if TARGET[-5:] == "faire":
        il_add_t()
        present_endings[3] = f"{RED}s{RESET}ons"
        present_endings[4] = f"{RED}tes"
        FUTURE_CONDITIONAL_STEM = TARGET[:-4] + f"{RED}er{RESET}"
        past_participle_ending = RED + "t"
        PASSE_SIMPLE_STEM = RED + TARGET[:-4] + RESET

    if TARGET[-4:] == "fire":
        il_add_t()
        NOUS_VOUS_PRESENT_STEM += RED + "s" + RESET
        ils_present_use_nous_stem = True
        PASSE_SIMPLE_STEM = RED + TARGET[:-3] + RESET
        past_participle_ending = RED + "t"

    if TARGET[-7:] == "prendre":
        NOUS_VOUS_PRESENT_STEM = RED + STEM[:-1] + RESET
        PASSE_SIMPLE_STEM = RED + TARGET[:-5] + RESET

    if TARGET[-4:] == "rire":
        il_add_t()
        PASSE_SIMPLE_STEM = RED + TARGET[:-3] + RESET

    if TARGET[-5:] == "crire":
        NOUS_VOUS_PRESENT_STEM += RED + "v" + RESET
        ils_present_use_nous_stem = True
        PASSE_SIMPLE_STEM += f"{RED}iv{RESET}"

    if TARGET[-6:] == "rompre":
        il_add_t()

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
    present[3] = f"{NOUS_VOUS_PRESENT_STEM}{present_endings[3]}"
    present[4] = f"{NOUS_VOUS_PRESENT_STEM}{present_endings[4]}"
    if ils_present_use_nous_stem:
        present[5] = f"{NOUS_VOUS_PRESENT_STEM}{present_endings[5]}"
    if TARGET == "avoir":
        present = [f"{RED}ai{RESET}", f"{RED}as{RESET}", f"{RED}a{RESET}", f"{RED}av{RESET}ons", f"{RED}av{RESET}ez", f"{RED}ont{RESET}"]
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
        present = [f"{RED}suis", f"{RED}es", f"{RED}est", f"{RED}sommes", f"{RED}êtes", f"{RED}sont"]
    elif TARGET == "inclure":
        present[2] = f"{RED}inclut"
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
    elif TARGET == "nuire":
        p1 = f"nui{RED}s{RESET}"
        present = [p1, p1, f"nui{RED}t", p1 + "ons", p1 + "ez", p1 + "ent"]
    elif TARGET == "plaire":
        p1 = f"plai{RED}s"
        present = present[:2] + [f"pla{RED}ît", p1 + "ons", p1 + "ez", p1 + "ent"]
    elif TARGET == "pouvoir":
        p1 = f"{RED}peux"
        p2 = f"{RED}peut"
        p3 = f"{RED}pouv{RESET}"
        p4 = f"{RED}peuvent"
        present = [p1, p1, p2, p3 + "ons", p3 + "ez", p4]
    elif TARGET == "valoir":
        p1 = f"{RED}val{RESET}"
        p2 = f"{RED}vaux{RESET}"
        p3 = f"{RED}vaut{RESET}"
        present = [p2, p2, p3, p1 + "ons", p1 + "ez", p1 + "ent"]
    elif TARGET == "venir":
        p1 = f"{RED}viens{RESET}"
        p2 = f"{RED}vient{RESET}"
        p3 = f"{RED}ven{RESET}"
        p4 = f"{RED}vienn{RESET}"
        present = [p1, p1, p2, p3 + "ons", p3 + "ez", p4 + "ent"]
    elif TARGET == "voir":
        p1 = f"vo{RED}y{RESET}"
        present = present[:3] + [p1 + "ons", p1 + "ez", f"vo{RED}i{RESET}ent"]
    if TARGET[-5:] == "faire":
        present[5] = RED + TARGET[:-4] + "ont"
    if TARGET[-7:] == "prendre":
        present[5] = f"{TARGET[:-3]}{RED}n{RESET}ent"
    SUBJUNCTIVE_STEM = present[5][:-3]
    if TARGET == "avoir":
        SUBJUNCTIVE_STEM = f"{RED}ai{RESET}"
    elif TARGET == "pouvoir":
        SUBJUNCTIVE_STEM = f"{RED}puiss{RESET}"
    elif TARGET == "valoir":
        SUBJUNCTIVE_STEM = f"{RED}vaill{RESET}"
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
    imperfect = [f"{IMPERFECT_STEM}{j}" for j in imperfect_endings]
    future = [f"{FUTURE_CONDITIONAL_STEM}{j}" for j in future_endings]
    conditional = [f"{FUTURE_CONDITIONAL_STEM}{j}" for j in conditional_endings]
    subjunctive = [f"{SUBJUNCTIVE_STEM}{j}" for j in subjunctive_endings]
    if TARGET == "avoir":
        subjunctive[2] = f"{RED}ait"
        subjunctive[3] = f"{RED}ay{RESET}ons"
        subjunctive[4] = f"{RED}ay{RESET}ez"
    if TARGET == "croire":
        subjunctive[3] = f"cro{RED}y{RESET}ions"
        subjunctive[4] = f"cro{RED}y{RESET}iez"
    imperative = deepcopy(present)
    if ENDING == "er":
        imperative[1] = imperative[1][:-1]
    if TARGET == "avoir":
        imperative[1] = f"{RED}aie"
        imperative[3] = f"{RED}ay{RESET}ons"
        imperative[4] = f"{RED}ay{RESET}ez"        
        pass
    elif TARGET == "être":
        imperative[1] = f"{RED}sois"
        imperative[3] = f"{RED}soy{RESET}ons"
        imperative[4] = f"{RED}soy{RESET}ez"
    present_participle = present[3][:-3] + "ant"
    past_participle = STEM + past_participle_ending
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
    # partciples
    irregular_past_participles = {
        "avoir": "eu",
        "battre": "battu",
        "boire": "bu",
        "craindre": "craint",
        "croire": "cru",
        "être": "été",
        "inclure": "inclus",
        "lire": "lu",
        "luire": "lui",
        "moudre": "moulu",
        "mourir": "mort",
        "naître": "né",
        "nuire": "nui",
        "offrir": "offert",
        "plaire": "plu",
        "pouvoir": "pu",
        "valoir": "valu",
        "venir": "venu",
        "voir": "vu",
    }
    for k, v in irregular_past_participles.items():
        if TARGET == k:
            past_participle = f"{RED}{v}"

    if TARGET == "être":
        present_participle = f"{RED}étant"
            
    # passe simple and imperfect subjunctive
    if past_participle[-1] == "u":
        passe_simple_endings = u_passe_simple_pattern
    passe_simple = [f"{PASSE_SIMPLE_STEM}{j}" for j in passe_simple_endings]
    IMPERFECT_SUBJUNCTIVE_STEM = f"{passe_simple[2][:-2]}"
    vowel = remove_codes(passe_simple[2])[-2]
    imperfect_subjunctive_endings = ["sse", "sses", "t", "ssions", "ssiez", "ssent"]
    imperfect_subjunctive_endings = [vowel + RESET + i for i in imperfect_subjunctive_endings]
    if vowel == "a":
        imperfect_subjunctive_endings[2] = f"â{RESET}t"
    elif vowel == "i":
        imperfect_subjunctive_endings[2] = f"î{RESET}t"
    elif vowel == "u":
        imperfect_subjunctive_endings[2] = f"û{RESET}t"
    imperfect_subjunctive = [f"{IMPERFECT_SUBJUNCTIVE_STEM}{j}" for j in imperfect_subjunctive_endings]
    if TARGET == "venir":
        imperfect_subjunctive[2] = f"{RED}vînt"


    s1 = f"\n           {'PRESENT':15} {'IMPERFECT':15} {'FUTURE':15} {'CONDITIONAL':15}"
    s2 = f"\n           {'SUBJUNCTIVE':15} {'IMP. SUBJ.':15} {'PASSE SIMPLE':15} {'IMPERATIVE':15}"

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


    for k in [[s1, tenses[:4]], [s2, tenses[4:]]]:
        print(k[0])
        for pronoun in range(6):
            print(f"{PRONOUNS[pronoun].rjust(10)}", end=" ")
            for tense in k[1]:
                if any([
                    tense is imperative and pronoun in [0, 2, 5],
                    pronoun == 3 and "nous" in defects and (tense is present or tense is imperative),
                    pronoun == 4 and "nous" in defects and (tense is present or tense is imperative),
                    pronoun == 5 and "ils" in defects and tense is present,
                    "nous" in defects and tense is imperfect,
                    "ils" in defects and tense is subjunctive,
                    "passe_simple" in defects and tense is passe_simple,
                    "passe_simple" in defects and tense is imperfect_subjunctive,
                    "imperative" in defects and tense is imperative
                ]):
                    print("-".ljust(15), end=" ")
                    continue
                print(justify(f"{tense[pronoun]}", 15), end=" ")
                print(f"{RESET}", end="")
            print("")

    if "nous" in defects:
        present_participle = "-"
    print(f"\nPRESENT PARTCIPLE = {present_participle}{RESET}")
    print(f"   PAST PARTCIPLE = {past_participle}{RESET}")
    print(f"   AUXILLARY = {AUXILLARY}")