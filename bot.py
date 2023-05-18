import requests
import asyncio
from datetime import date
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

# Replace 'your-bot-token' with your bot's token on the last line

bot = commands.Bot(command_prefix='!')

SERVER_IP_TEMPLATE = 'Servers Up! Join by typing in the console "open {}"'

# Replace 'your-webhook' with a discord webhook for your status channel
WEBHOOK_URL = your-webhook

# Set the channel ID where the webhook messages are being sent
CHANNEL_ID = channel-id

async def delmsg():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        async for message in channel.history(limit=5):  # Adjust the limit if necessary
            if message.webhook_id:
                await message.delete()
                await message.delete()
                return message.id
    else:
        print("No message to delete currently.")

async def send_embed(title, description, color, image_url):
    data = {
        'embeds': [{
            'title': title,
            'description': description,
            'color': color,
            'image': {'url': image_url}
        }]
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print('Message sent successfully.')
    else:
        print('Failed to send message:', response.status_code, response.text)



async def send_message(content):
    data = {
        'content': content
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print('Message sent successfully.')
    else:
        print('Failed to send message:', response.status_code, response.text)



async def main():
    server_ip = input("Enter the server IP address that you are hosting with: ")
    SERVER_IP = SERVER_IP_TEMPLATE.format(server_ip)


    while True:
        print('Choose an option:')
        print('-------------')
        print('1. Servers up')
        print('-------------')
        print('2. Servers in progress')
        print('Note: unnecessary as this is automatically sent after 270 seconds')
        print('-------------')
        print('3. Servers restarting')
        print('-------------')
        print('4. Servers offline')
        print('-------------')
        print('q. Quit')

        choice = input('Enter your choice: ').lower()

        if choice == '1':
            message_id = await delmsg()
            await send_embed('SERVERS UP!', SERVER_IP, 0x32CD32, r'https://media.discordapp.net/attachments/1067617185108865071/1086840538201858099/a3db519ffdb441307b1f8c92d910ef9b.jpeg?width=1201&height=675')
            # Replace @&PING ROLE ID with your role ID
            await send_message('Servers up! Join by typing the command above. <@&PING ROLE ID>')
            message_id = await delmsg()
            await asyncio.sleep(120)
            message_id = await delmsg()
            await send_embed('SERVERS IN PROGRESS', 'Servers in progress, please wait...', 0xFFD700, r'https://media.discordapp.net/attachments/1067617185108865071/1086840443263791114/TNHyeyqTofRfpqVFMzb8QS-1200-80.jpg?width=900&height=506')
        elif choice == '2':
            message_id = await delmsg()
            await send_embed('SERVERS IN PROGRESS', 'Servers in progress, please wait...', 0xFFD700, r'https://media.discordapp.net/attachments/1067617185108865071/1086840443263791114/TNHyeyqTofRfpqVFMzb8QS-1200-80.jpg?width=900&height=506')
        elif choice == '3':
            message_id = await delmsg()
            await send_embed('SERVERS RESTARTING!', 'Please wait for the servers to start in a minute.', 0xFF0000, r'https://media.discordapp.net/attachments/894403210788372511/1086856727716171948/c5717-16465652482721-1920.png?width=1351&height=675')
        elif choice == '4':
            message_id = await delmsg()
            await send_embed(f'Servers offline as of {date.today().strftime("%B %d, %Y")}.', 'Thank you for playing! 😃', 0x3D3D3D, r'https://media.discordapp.net/attachments/1067617185108865071/1086840853777092658/cb0b260f3a7f5bf346aaa9472b768dcf.jpg?width=1201&height=675')
        elif choice == 'q':
            break

if __name__ == '__main__':
    bot.loop.create_task(main())
    bot.run('your-bot-token')  # Replace 'your-bot-token' with your bot's token

