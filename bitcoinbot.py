import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix='$')

@bot.command()
async def bitcoin_wallet_info(ctx, wallet_address: str):
    # API request
    response = requests.get(f'https://api.blockcypher.com/v1/btc/main/addrs/{wallet_address}')
    data = response.json()

    # Check if the request was successful
    if response.status_code == 200:
        # Retrieve data
        balance = data['balance']
        total_received = data['total_received']
        total_sent = data['total_sent']
        unconfirmed_balance = data['unconfirmed_balance']

        # Create response message
        response_message = f'Wallet Info:\n' \
                           f'Balance: {balance}\n' \
                           f'Total Received: {total_received}\n' \
                           f'Total Sent: {total_sent}\n' \
                           f'Unconfirmed Balance: {unconfirmed_balance}'

        await ctx.send(response_message)
    else:
        await ctx.send("Invalid Wallet Address or Other Error Encountered")

bot.run('your_bot_token')
