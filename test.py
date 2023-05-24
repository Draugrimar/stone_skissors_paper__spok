import json

all_players = {}
with open("win_list.txt") as file:
    for line in file:
        key, *value = line.split(":")
        all_players[key] = value
print(all_players)

# open("win_list.txt", "w").write(json.dumps(all_players))
