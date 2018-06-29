"""
    instabot example

    Workflow:
        get all hashtags used by a user.
"""

import sys
import os
import time
import random
import json
from tqdm import tqdm
import argparse

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

def get_hashtags(text, order=False):
    tags = set([item.strip("#.,-\"\'&*^!") for item in text.split() if (item.startswith("#") and len(item) < 256)])
    return sorted(tags) if order else tags

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
args = parser.parse_args()

bot = Bot()
bot.login(username=args.u, password=args.p,
          proxy=args.proxy)
print("Start up the coffee pot... this may take awhile.")
medias = bot.get_total_user_medias(bot.user_id)
#medias = bot.get_your_medias()

#for media in medias:
hastags = []
for media in medias:
	mediaInfo = bot.get_media_info(media)
	if mediaInfo[0]["caption"] is no None:
		tags = get_hashtags(mediaInfo[0]["caption"]["text"].lower())
		for tag in tags:
			if tag not in hastags:
			    hastags.append(tag)

print hastags