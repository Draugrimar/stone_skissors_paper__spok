import json

all_players = [
    {"name": "Ed", "win": 10, "draw": 5, "lose": 5, "ratio": 50.0},
    {"name": "Player 2", "win": 100, "draw": 50, "lose": 50, "ratio": 50.0},
    {"name": "Player 3", "win": 2, "draw": 1, "lose": 1, "ratio": 50.0}]


player_name = input("Enter your name: ")
current_player = None

for player in all_players:
    if player.get("name") == player_name:
        current_player = player

if current_player == None:
    current_player = dict(name=player_name, win=0, draw=0, lose=0, ratio=0)


player_name, win, draw, lose, ratio = current_player.values()


# print(f"{player_name} win {win} times, get {draw} draws, lose {lose} games. Overall win ratio is {ratio}")

print(all_players)
open("win_list.txt", "w").write(json.dumps(all_players))
