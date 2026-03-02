import pytest
from lerniloj.conjugation_predictor import get_tense_conjugation_from_verb, verb_conjugator, get_tense_conjugation_by_pronoun, remove_text_colour


def quick_assert(verb, tense, pronoun, expected):
    assert get_tense_conjugation_from_verb(verb, tense, pronoun) == expected


def quick_assert_auxillary(verb, expected):
    verb_conjugator(verb)["auxillary"] == expected


@pytest.mark.parametrize("verb, expected", [
    ("absoudre", "absous"),
    ("acquérir", "acquis"),
    ("apprendre", "appris"),
    ("asseoir", "assis"),
    ("atteindre", "atteint"),
    ("avoir", "eu"),
    ("boire", "bu"),
    ("choir", "chu"),
    ("comprendre", "compris"),
    ("conduire", "conduit"),
    ("connaître", "connu"),
    ("construire", "construit"),
    ("courir", "couru"),
    ("couvrir", "couvert"),
    ("craindre", "craint"),
    ("croire", "cru"),
    ("croître", "crû"),
    ("décevoir", "déçu"),
    ("découvrir", "découvert"),
    ("devoir", "dû"),
    ("dire", "dit"),
    ("écrire", "écrit"),
    ("éteindre", "éteint"),
    ("être", "été"),
    ("faire", "fait"),
    ("falloir", "fallu"),
    ("frire", "frit"),
    ("instruire", "instruit"),
    ("joindre", "joint"),
    ("lire", "lu"),
    ("luire", "lui"),
    ("mettre", "mis"),
    ("mourir", "mort"),
    ("mouvoir", "mû"),
    ("naître", "né"),
    ("offrir", "offert"),
    ("ouvrir", "ouvert"),
    ("paraître", "paru"),
    ("peindre", "peint"),
    ("plaire", "plu"),
    ("pleuvoir", "plu"),
    ("pouvoir", "pu"),
    ("prendre", "pris"),
    ("produire", "produit"),
    ("promettre", "promis"),
    ("recevoir", "reçu"),
    ("rendre", "rendu"),
    ("résoudre", "résolu"),
    ("rire", "ri"),
    ("savoir", "su"),
    ("souffrir", "souffert"),
    ("suivre", "suivi"),
    ("tenir", "tenu"),
    ("traduire", "traduit"),
    ("venir", "venu"),
    ("vêtir", "vêtu"),
    ("vivre", "vécu"),
    ("voir", "vu"),
    ("vouloir", "voulu"),
])
def test_check_past_participle(verb, expected):
    assert remove_text_colour(verb_conjugator(verb)["past_participle"]) == expected


@pytest.mark.parametrize("verb, expected", [
    ("acheter", "achète"),
    ("appeler", "appelle"),
    ("attendre", "attends"),
    ("battre", "bats"),
    ("boire", "bois"),
    ("bouillir", "bous"),
    ("commencer", "commence"),
    ("conclure", "conclus"),
    ("connaître", "connais"),
    ("coudre", "couds"),
    ("courir", "cours"),
    ("craindre", "crains"),
    ("créer", "crée"),
    ("croître", "croîs"),
    ("cueillir", "cueille"),
    ("cuire", "cuis"),
    ("descendre", "descends"),
    ("devenir", "deviens"),
    ("dormir", "dors"),
    ("écrire", "écris"),
    ("émouvoir", "émeus"),
    ("envoyer", "envoie"),
    ("espérer", "espère"),
    ("fuir", "fuis"),
    ("haïr", "hais"),
    ("jeter", "jette"),
    ("joindre", "joins"),
    ("lever", "lève"),
    ("lire", "lis"),
    ("maudire", "maudis"),
    ("mordre", "mords"),
    ("moudre", "mouds"),
    ("mourir", "meurs"),
    ("naître", "nais"),
    ("nettoyer", "nettoie"),
    ("offrir", "offre"),
    ("paraître", "parais"),
    ("peindre", "peins"),
    ("perdre", "perds"),
    ("plaire", "plais"),
    ("prendre", "prends"),
    ("protéger", "protège"),
    ("recevoir", "reçois"),
    ("répondre", "réponds"),
    ("résoudre", "résous"),
    ("rire", "ris"),
    ("rompre", "romps"),
    ("servir", "sers"),
    ("sortir", "sors"),
    ("suffire", "suffis"),
    ("suivre", "suis"),
    ("tenir", "tiens"),
    ("traire", "trais"),
    ("vaincre", "vaincs"),
    ("valoir", "vaux"),
    ("vêtir", "vêts"),
    ("vivre", "vis"),
])
def test_check_present_je(verb, expected):
    quick_assert(verb, "present", "je", expected)


def test_etre_present():
    assert get_tense_conjugation_from_verb("etre", "present") == ["suis", "es", "est", "sommes", "êtes", "sont"]


def test_avoir_present():
    assert get_tense_conjugation_from_verb("avoir", "present") == ["ai", "as", "a", "avons", "avez", "ont"]


def test_aller_present():
    assert get_tense_conjugation_from_verb("aller", "present") == ["vais", "vas", "va", "allons", "allez", "vont"]


def test_faire_present():
    assert get_tense_conjugation_from_verb("faire", "present") == ["fais", "fais", "fait", "faisons", "faites", "font"]


def test_lancer_present_nous():
    assert get_tense_conjugation_from_verb("lancer", "present", "nous") == "lançons"


def test_aller_imperfect_subjunctive():
    assert get_tense_conjugation_from_verb("aller", "imperfect_subjunctive") == ["allasse", "allasses", "allât", "allassions", "allassiez", "allassent"]


def test_dire_present():
    assert get_tense_conjugation_from_verb("dire", "present") == ["dis", "dis", "dit", "disons", "dites", "disent"]


def test_acheter_present():
    assert get_tense_conjugation_from_verb("acheter", "present") == ["achète", "achètes", "achète", "achetons", "achetez", "achètent"]


def test_vêtir_present():
    assert get_tense_conjugation_from_verb("vêtir", "present") == ["vêts", "vêts", "vêt", "vêtons", "vêtez", "vêtent"]


def test_recevoir_present():
    assert get_tense_conjugation_from_verb("recevoir", "present") == ["reçois", "reçois", "reçoit", "recevons", "recevez", "reçoivent"]


def test_vouloir_present():
    assert get_tense_conjugation_from_verb("vouloir", "present") == ["veux", "veux", "veut", "voulons", "voulez", "veulent"]


def test_vouloir_future():
    assert get_tense_conjugation_from_verb("vouloir", "future", "je") == "voudrai"


def test_vouloir_subjunctive():
    assert get_tense_conjugation_from_verb("vouloir", "subjunctive", "je") == "veuille"


def test_vouloir_subjunctive():
    assert get_tense_conjugation_from_verb("vouloir", "subjunctive", "nous") == "voulions"


def test_vouloir_passe_simple():
    assert get_tense_conjugation_from_verb("vouloir", "passe_simple", "je") == "voulus"


def test_voir_subjunctive_nous():
    quick_assert("voir", "subjunctive", "nous", "voyions")


def test_se_taire_auxillary():
    quick_assert_auxillary("se taire", "être")


def test_se_taire_present():
    assert get_tense_conjugation_from_verb("se taire", "present") == ["tais", "tais", "tait", "taisons", "taisez", "taisent"]


def test_se_taire_je():
    assert get_tense_conjugation_by_pronoun("se taire", "je") == ["tais", "taisais", "tairai", "tairais", "taise", "tusse", "tus", "-"]


def test_mettre_il():
    assert get_tense_conjugation_by_pronoun("mettre", "il") == ["met", "mettait", "mettra", "mettrait", "mette", "mît", "mit", "-"]


def test_appeler_je():
    assert get_tense_conjugation_by_pronoun("appeler", "je") == ["appelle", "appelais", "appellerai", "appellerais", "appelle", "appelasse", "appelai", "-"]


def test_jeter_present_je():
    quick_assert("jeter", "present", "je", "jette")


def test_inclure_present_il():
    quick_assert("inclure", "present", "il", "inclut")


def test_reléguer_je():
    assert get_tense_conjugation_by_pronoun("reléguer", "je") == ["relègue", "reléguais", "reléguerai", "reléguerais", "relègue", "reléguasse", "reléguai", "-"]


def test_pouvoir_present():
    assert get_tense_conjugation_from_verb("pouvoir", "present") == ["peux", "peux", "peut", "pouvons", "pouvez", "peuvent"]


def test_valoir_present():
    assert get_tense_conjugation_from_verb("valoir", "present") == ["vaux", "vaux", "vaut", "valons", "valez", "valent"]


def test_rejoindre_present():
    assert get_tense_conjugation_from_verb("rejoindre", "present") == ["rejoins", "rejoins", "rejoint", "rejoignons", "rejoignez", "rejoignent"]


def test_vaincre_present_vous():
    quick_assert("vaincre", "present", "vous", "vainquez")


def test_vaincre_passe_simple_je():
    quick_assert("vaincre", "passe_simple", "je", "vainquis")


def test_suivre_tu():
    assert get_tense_conjugation_by_pronoun("suivre", "tu") == [
        "suis", 
        "suivais", 
        "suivras", 
        "suivrais", 
        "suives", 
        "suivisses", 
        "suivis", 
        "suis",
    ]


def test_suffire_tu():
    assert get_tense_conjugation_by_pronoun("suffire", "tu") == [
        "suffis", 
        "suffisais", 
        "suffiras", 
        "suffirais", 
        "suffises", 
        "suffisses", 
        "suffis", 
        "suffis",
    ]

@pytest.mark.parametrize("verb, expected", [
        ("courir", ["cours", "courais", "courras", "courrais", "coures", "courusses", "courus", "cours",]),
        ("acquérir", ["acquiers", "acquérais", "acquerras", "acquerrais", "acquières", "acquisses", "acquis", "acquiers"]),
        ("asseoir", ["assieds", "asseyais", "assiéras", "assiérais", "asseyes", "assisses", "assis", "assieds"])
    ], ids=["courir", "acquérir", "asseoir"]
)
def test_tu(verb, expected):
    assert get_tense_conjugation_by_pronoun(verb, "tu") == expected


def test_pleuvoir_il():
    assert get_tense_conjugation_by_pronoun("pleuvoir", "il") == ["pleut", "pleuvait", "pleuvra", "pleuvrait", "pleuve", "plût", "plut", "-"]


def test_falloir_il():
    assert get_tense_conjugation_by_pronoun("falloir", "il") == ["faut", "fallait", "faudra", "faudrait", "faille", "fallût", "fallut", "-"]


def test_nuire_present():
    assert get_tense_conjugation_from_verb("nuire", "present") == ["nuis", "nuis", "nuit", "nuisons", "nuisez", "nuisent"]


def test_bouillir_je():
    assert get_tense_conjugation_by_pronoun("bouillir", "je") == ["bous", "bouillais", "bouillirai", "bouillirais", "bouille", "bouillisse", "bouillis", "-"]