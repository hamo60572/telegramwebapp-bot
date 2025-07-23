
from telethon.sync import TelegramClient, events

api_id = 27434599
api_hash = 'ee6fa01ef5cc3b87b60d553c36c91fa6'
bot_username = '@portals_market_bot'

with TelegramClient('session_name', api_id, api_hash) as client:
    async def main():
        await client.send_message(bot_username, '/start')
        print("تم فتح البوت. افتح التليجرام وشوف")

    client.loop.run_until_complete(main())
    