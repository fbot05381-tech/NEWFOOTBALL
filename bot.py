import logging
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import TOKEN
import handlers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", handlers.start))
    app.add_handler(CommandHandler("solo", handlers.solo_cmd))
    app.add_handler(CommandHandler("team", handlers.team_cmd))
    app.add_handler(CommandHandler("start_game", handlers.start_game_cmd))
    app.add_handler(CommandHandler("start_tournament", handlers.tournament_cmd))
    app.add_handler(CommandHandler("start_auction", handlers.auction_cmd))

    # Button callbacks
    app.add_handler(CallbackQueryHandler(handlers.button_handler))

    # Game actions
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.action_handler))

    logger.info("⚽ Football Bot Started Successfully!")
    app.run_polling()

if __name__ == "__main__":
    main()
