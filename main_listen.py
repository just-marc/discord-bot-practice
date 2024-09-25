from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# STEP 0: LOAD OUR TOKEN FROM .env
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# STEP 2: MESSAGE FUCTIONALITY
async def send_message(message: Message, user_message: str, channel_id: int) -> None:
    if not user_message:
        print('(Message was empty because intents were most likely not enabled.)')
        return

    try:
        recipient_channel = client.get_channel(channel_id)
        await recipient_channel.send(user_message)

    except Exception as e:
        print(e)

# STEP 3: HANDELING THE STARTUP FOR THE BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user or message.channel.id != 1288483003722629170:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message, 1288483052107862037)


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
