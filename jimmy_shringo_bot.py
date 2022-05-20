# bot.py
import os
import random


import discord
from discord.ext import commands,tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# This is shtuff that is printed to powershell when the bot goes online
@client.event
async def on_ready():
    print(f'{client.user} has hacked into the mainframe \U0001F608 \U0001F608 \U0001F608 \n') # those are devil emojis #swag
    print("Jimmy Shringo Bot has infiltrated the following servers: ")
    for guild in client.guilds:
        print(guild)

# This is stuff that the bot will say when prompted by something in chat
@client.event
async def on_message(message):
    if message.author == client.user:
        return
          
    # Instance for "WHAT BRO WHAT DUDE WHAT" etc.
    DUDE_BRO_WHAT_response = ["DUDE!", "BROOOOOOOOOOOO", "WHAT DUDE?!?!?!??!?!??!", "DUUUUUUUUUUDE!!!!!!!!!!!!!!!", "BROOOOOOOOOOOOOOOOOO!!!!!!!!!!! YOU CAN'T SAY THAT DUDE!!!!",
    "WHAT BRO YOU'RE LITERALLY GAY", "WHAT BRO YOU'RE A LIBERAL \U0001F923 \U0001F923 \U0001F923"]
    DUDE_BRO_WHAT_input = ["dude", "bro", "bro!", "dude!", "what", "what dude", "what bro",
     "what bro?!", "what bro!?", "what dude!?", "what dude!?"]

    if message.content.lower() in DUDE_BRO_WHAT_input:
        response = random.choice(DUDE_BRO_WHAT_response)
        await message.channel.send(response)

    # Instance for "you're a liberal" stuff
    liberal_response = ["WHAT BRO I'M NOT A LIBERAL", "says the lib \U0001F923", "DUUUUUUUUUUDE BROOOOOOOOON I'M NOT A LIBERAL!!!!!!!!! \uE059 \uE059 \uE059"]
    liberal_input = ["you're a liberal", "you're a lib", "lib", "liberal", "ur a lib", "ur a liberal", "your a lib"]

    if message.content.lower() in liberal_input:
        response = random.choice(liberal_response)
        await message.channel.send(response)

    # Instance for "you're gay" stuff
    gay_input = ["you're gay", "gay", "faggot", "fag", "you're a faggot", "you're a fag", "ur gay", "ur a faggot"]
    gay_response = ["DUDE I'M NOT GAY!!!!!!!!!! \uE059 \uE059 \uE059", "kys fag"]

    if message.content.lower() in gay_input:
        response = random.choice(gay_response)
        await message.channel.send(response)

    # Instance for nword
    nword_input = "nigger"
    nword_response = ["nword", "DUDE WHAT THE FUCK YOU CAN NOT SAY THAT I'M FUCKING SERIOUS I AM REPORTING YOU TO THE FBI WTF WTF WTF", "DUDE WHAT THE FUCK YOU ABSOLUTELY CAN NOT SAY THAT!!!!!!!!!!!!!!!!!", 
    "DUUUUUUDE I SCREEENSHOTTING YOUR COMMENT AND I AM SENDING IT TO YOUR EMPLOYER BROOOOOOOOOOOOOOOOOOOOO #CANCELLED #PRIDE"]

    if message.content.lower() in nword_input:
        response = random.choice(nword_response)
        await message.channel.send(response)

    
# Part where I attempt to make a music bot




client.run(TOKEN)

