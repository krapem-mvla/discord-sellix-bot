import discord
import requests
import re
import json
import random
import time
import os
from os import system
from discord.ext import commands
from requests.structures import CaseInsensitiveDict

bot = commands.Bot(command_prefix='-')
bot.remove_command("help")
api_key = 'VK8FQ-3UUBR-E59U2-245KX'#IGNORE
SELLIX_API_KEY = 'API KEY HERE'

@bot.event
async def on_ready():
    print('-------')
    print('Online')
    print('-------')



@bot.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title="-_-", description="You are using that command wrong, please retry with the correct roles or arguments.")
    embed.set_footer(text="-Cypher")
    await ctx.send(embed=embed)
    print(error)


@bot.command()
async def help(ctx, menu=None):
    admin = ctx.message.author.guild_permissions.administrator
    #Main Menu
    async def main_menu():
        embed = discord.Embed(title="Cypher Help", color=0xffffff)
        embed.set_thumbnail(
            url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2Fa%2Fae%2FQuestion_mark_white-transparent.svg%2F1200px-Question_mark_white-transparent.svg.png&f=1&nofb=1")
        embed.add_field(name="-help user", value="Brings up the user commands section", inline=False)
        embed.add_field(name="-help admin", value="Brings up Admin only commands", inline=False)
        embed.set_footer(text="-Cypher")
        await ctx.send(embed=embed)
    #User Menu
    async def user_menu():
        embed = discord.Embed(title="Cypher User Help", description= "More coming soon...")
        #embed.add_field(name="-verify (order id)", value="Verify your sellix order", inline=False)
        embed.add_field(name="-user (@)", value="Get's a given users info", inline=False)
        embed.add_field(name="-avatar (@)", value="Returns a users Discord Avatar", inline=False)
        embed.set_footer(text="-Cypher")
        await ctx.send(embed=embed)
    #Admin Menu
    async def admin_menu():
        embed = discord.Embed(title="Cypher Admin Help", description="More Soon...")
        embed.add_field(name="-nuke", value="Deletes a channel and duplicates it", inline=False)
        embed.add_field(name="-status 'Status value'", value="Sets Cypher bot status", inline=False)
        embed.add_field(name="-embed 'Title' 'Body Text'", value="Creates a Cypher Embed", inline=False)
        embed.add_field(name="-say 'something'", value="Says whatever you type", inline=False)
        embed.set_footer(text="-Cypher")
        await ctx.send(embed=embed)
    async def permissions_menu():
        embed = discord.Embed(title="No Perms", description="Don't even try it no perms having ass.")
        embed.set_footer(text="-Cypher")
        await ctx.send(embed=embed)
    #Admin Checks
    is_admin = None
    async def admin_check():
        if admin == True:
            await admin_menu()
        if admin != True:
            await permissions_menu()
    if menu == None:
        await main_menu()
    if menu == "user":
        await user_menu()
    if menu == "admin":
        await admin_check()
    print(admin)

@bot.command()
@commands.has_permissions(administrator=True)
async def status(ctx, status):
    await bot.change_presence(activity=discord.Game((status)))
    embed = discord.Embed(title="Status Updated", description=status)
    embed.set_footer(text="-Cypher")
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def embed(ctx, title, description):
    message = ctx.message
    await message.delete()
    embed = discord.Embed(title=str(title), description=str(description), color=0xffffff)
    await ctx.send(embed=embed)
@bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, description):
    message = ctx.message
    await message.delete()
    embed = discord.Embed(description=str(description), color=0xffffff)
    await ctx.send(embed=embed)

@bot.command()
async def allorders(ctx):
    token="APIKEYHERE"
    prod = "https://dev.sellix.io/v1/products"
    order_endpoint = "https://dev.sellix.io/v1/orders/"
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer APIKEYHERE"
    resp = requests.get(order_endpoint, headers=headers)
    output = resp.text
    parsed = json.loads(output)
    print(parsed)

@bot.command()
async def verify(ctx, description):
    author = ctx.message.author
    #post_headers = {'Authorization' : 'Bearer {SELLIX_API_KEY}}
    token="API KEY HERE"
    prod = "https://dev.sellix.io/v1/products"
    order_endpoint = "https://dev.sellix.io/v1/orders/" + description
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer xADoWdXTSvsvQ9BLZUyNtQzikaAFGN5h63w5EmVFozu1KpYeIjEjrqkhL5EHQbty"
    resp = requests.get(order_endpoint, headers=headers)
    output = resp.text
    parsed = json.loads(output)
    #print(resp.json)
   # GET /orders/:uniqid 
    data = (parsed["data"])
    order = (data["order"])
    status_history = (order["status_history"])
    length = len(status_history)
    status = order["status_history"][length - 1]["status"]
    print('\n\n\noutput:\n')
    print ("Request for ID: " + description + " | With status: " + status)
    if status == "COMPLETED":
        error1 = "Order ID Already Verified!"
        with open('data.txt') as f:
            if description in f.read():
                print("true")
        text_file = open("data.txt", "w")
        embed = discord.Embed(title="Cypher.market")
        n = text_file.write(description + "\n")
        text_file.close()
        embed.add_field(name="Order ID: ", value = description, inline = True)
        embed.add_field(name="Status: ", value = status, inline = True)
        embed.add_field(name="Result: ", value = error1, inline = True)
        embed.set_footer(text="-Cypher")
        await ctx.send(embed=embed)
    else:
        
@bot.command()
async def user(ctx, name: discord.Member):
    author = ctx.message.author
    display = name.display_name
    id = name.id
    created_on = name.created_at
    joined_on = name.joined_at
    icon = name.avatar_url
    embed = discord.Embed(title="")
    embed.set_author(name=f"Requested By: {author.name}", icon_url = author.avatar_url)
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Name: ", value = display, inline = True)
    embed.add_field(name="ID: ", value = id, inline = True)
    embed.add_field(name="Created On: ", value = created_on, inline = True)
    embed.add_field(name="Joined On: ", value=joined_on, inline=True)
    embed.set_footer(text="-Cypher")
    await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx, call: discord.Member):
    author = ctx.message.author
    icon = call.avatar_url
    name = call.display_name
    embed = discord.Embed(title=f"{name}'s Avatar")
    embed.set_image(url=icon)
    embed.set_footer(text="Requested by " + author.name)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://thumbs.gfycat.com/EnergeticWastefulCockerspaniel-small.gif")
    async with ctx.typing():
        position = ctx.channel.position
        await ctx.channel.delete()
        c = await ctx.channel.clone()
        await c.edit(position=position)
    await c.send(embed=embed)

bot.run("BOTKEY")
