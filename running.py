import json 

with open("running.json", "r") as file:
    data = json.load(file)
 
runners = data["competition"]["participants"]

runners_sorted = sorted(runners, key= lambda x: x["time_seconds"])

top3 = runners_sorted[:3]

print('Top Runners:')
for i,p in enumerate(top3, start=1):
    print(f"{i}. {p['name']}: {p['time_seconds']} seconds")

