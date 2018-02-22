import asyncio
import discord
import random
import math
from   datetime import datetime
from   discord.ext import commands
from   operator import itemgetter
from   Cogs import DisplayName
from   Cogs import Nullify
from   Cogs import CheckRoles
from   Cogs import Message

def setup(bot):
	# Add the bot and deps
	settings = bot.get_cog("Settings")
	bot.add_cog(XpStack(bot, settings))

# This is the xp module.  It's likely to be retarded.
