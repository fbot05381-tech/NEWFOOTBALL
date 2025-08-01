import json, random
from config import GOAL_GIF, YELLOW_CARD_GIF, RED_CARD_GIF, PASS_GIF, KICK_GIF

DB_FILE = "database.json"

def load_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ✅ Solo Mode Logic
def start_solo(player):
    return f"🎮 Solo Mode Started for {player}!"

# ✅ Team Mode Logic
def start_team(team):
    return f"🏆 Team Mode Started for {team}!"

# ✅ Actions (Kick, Pass, Goal, etc.)
def perform_action(action):
    if action == "kick":
        return KICK_GIF, "⚽ Powerful Kick!"
    elif action == "pass":
        return PASS_GIF, "🤝 Smooth Pass!"
    elif action == "goal":
        return GOAL_GIF, "🥅 GOAL!!!"
    elif action == "yellow":
        return YELLOW_CARD_GIF, "🟨 Yellow Card!"
    elif action == "red":
        return RED_CARD_GIF, "🟥 Red Card!"
    else:
        return "", "Unknown Action"
