import json
import csv


with open("mistakes2.json", "r") as f:
    data = json.load(f)

results = []
data = data["from_esperanto_written"]
for key in data.keys():
    records = data[key]
    correct = 0
    for record in records:
        if record["correct"]:
            correct += 1
    results.append((key, correct, len(records)))
    print(f"{key},{correct},{len(records)}")
    

with open("mistake_report.csv", "w") as f:
    w = csv.writer(f)
    w.writerows(results)