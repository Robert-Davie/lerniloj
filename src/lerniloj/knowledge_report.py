import json
import datetime


# lookups = ["from_esperanto_written", "to_esperanto_written"]
# TARGET_FILE = "word_lists/esperanto15000v2.txt"
# HISTORY_FILE = "history/mistakes2.json"

def knowledge_report(lookup, TARGET_FILE, HISTORY_FILE):
    with open(TARGET_FILE, "r") as f:
        terms = [line.strip().split(";")[0] for line in f.readlines()]


    with open(HISTORY_FILE, "r") as f:
        data = json.load(f)

    correct_count = 0
    incorrect_count = 0
    untaken_count = 0
    for term in terms:
        if " " in term:
            term = term.split()[0]
        if term in data[lookup].keys():
            if data[lookup][term][-1]["correct"]:
                correct_count += 1
            else:
                incorrect_count += 1
        else:
            if lookup == "from_esperanto_written":
                pass
            untaken_count += 1
    total = correct_count + incorrect_count + untaken_count
    subtotal = correct_count + incorrect_count
    result_string = f"""
date:          {datetime.datetime.now()}
lookup:        {lookup}
target_file:   {TARGET_FILE}
    
correct:       {correct_count}    
               {round(correct_count * 100 / total, 1)}% 
    relative   {round((correct_count * 100 / (subtotal if subtotal != 0 else 1)), 1)}%
incorrect:     {incorrect_count}    
               {round(incorrect_count * 100 / total, 1)}%
untaken_count: {untaken_count}    
               {round(untaken_count * 100 / total, 1)}%
total: {total} {len(terms)}
    """

    with open("reports/knowledge_report.txt", "w") as f:
        f.writelines(result_string)

    return result_string
