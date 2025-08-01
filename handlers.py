from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext
import game_utils

# ✅ Start Command
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("⚽ Solo Mode", callback_data="solo")],
        [InlineKeyboardButton("🏆 Team Mode", callback_data="team")],
        [InlineKeyboardButton("🎯 Tournament", callback_data="tournament")],
        [InlineKeyboardButton("💰 Auction Mode", callback_data="auction")]
    ]
    await update.message.reply_text(
        "🏟️ Welcome to Football Bot!\nChoose your mode:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ✅ Button Handler
async def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    user = query.from_user

    if query.data == "solo":
        game_utils.save_player(user.id, user.username, "solo")
        await query.edit_message_text("✅ You joined Solo Mode!")

    elif query.data == "team":
        game_utils.register_team(user.id, user.username)
        await query.edit_message_text("✅ You joined Team Mode!")

    elif query.data == "tournament":
        game_utils.start_tournament()
        await query.edit_message_text("🏆 Tournament Started!")

    elif query.data == "auction":
        game_utils.start_auction_mode()
        await query.edit_message_text("💰 Auction Mode Started!")

# ✅ /solo Command
async def solo_cmd(update: Update, context: CallbackContext):
    game_utils.save_player(update.effective_user.id, update.effective_user.username, "solo")
    await update.message.reply_text("✅ Registered in Solo Mode!")

# ✅ /team Command
async def team_cmd(update: Update, context: CallbackContext):
    game_utils.register_team(update.effective_user.id, update.effective_user.username)
    await update.message.reply_text("✅ Registered in Team Mode!")

# ✅ /start_game Command
async def start_game_cmd(update: Update, context: CallbackContext):
    await game_utils.start_game(update.message)

# ✅ /start_tournament Command
async def tournament_cmd(update: Update, context: CallbackContext):
    game_utils.start_tournament()
    await update.message.reply_text("🏆 Tournament Started!")

# ✅ /start_auction Command
async def auction_cmd(update: Update, context: CallbackContext):
    game_utils.start_auction_mode()
    await update.message.reply_text("💰 Auction Mode Started!")

# ✅ Handle In-game Actions
async def action_handler(update: Update, context: CallbackContext):
    await game_utils.handle_action(update.effective_user, update.message.text, update.message)
