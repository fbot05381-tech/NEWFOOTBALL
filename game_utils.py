import json

DB_FILE = "database.json"

# ✅ Load DB
def load_db():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return {"players": [], "teams": [], "tournament": {}, "auction": {}}

# ✅ Save DB
def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ✅ Solo Player
def save_player(user_id, username, mode="solo"):
    db = load_db()
    db["players"].append({"id": user_id, "username": username, "mode": mode})
    save_db(db)

# ✅ Team Player
def register_team(user_id, username):
    db = load_db()
    db["teams"].append({"id": user_id, "username": username})
    save_db(db)

# ✅ Start Game
async def start_game(message):
    actions = ["⚽ Kick", "🎯 Pass", "🚀 Long Pass", "📈 Lob Pass", "🔥 Shoot", "🛡️ Defend"]
    await message.reply_text("🏟️ Match Started!\nAvailable actions:\n" + ", ".join(actions))

# ✅ Start Tournament
def start_tournament():
    db = load_db()
    db["tournament"] = {"status": "running"}
    save_db(db)

# ✅ Start Auction
def start_auction_mode():
    db = load_db()
    db["auction"] = {"status": "open", "bids": []}
    save_db(db)

# ✅ Action Handler with Commentary
async def handle_action(user, text, message):
    actions = {
        "kick": "⚽ {p} performs a powerful kick!",
        "pass": "🎯 {p} passes the ball perfectly!",
        "long pass": "🚀 {p} sends a long pass!",
        "lob pass": "📈 {p} makes a lob pass!",
        "shoot": "🔥 {p} takes a shot at the goal!",
        "defend": "🛡️ {p} defends strongly!",
        "yellow card": "🟨 Referee gives a Yellow Card to {p}!",
        "red card": "🟥 Red Card! {p} is sent off!"
    }
    action = actions.get(text.lower())
    if action:
        await message.reply_text(action.format(p=user.first_name))
    else:
        await message.reply_text("❌ Invalid action! Try Kick, Pass, Shoot, Defend etc.")
