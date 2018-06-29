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
import csv

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
args = parser.parse_args()

bot = Bot()
bot.login(username=args.u, password=args.p, proxy=args.proxy)
print("Start up the coffee pot... this may take awhile.")

yoStats = bot.get_user_stats(args.u)
userID = bot.get_userid_from_username('r1b4z01d')
followers = bot.get_user_followers(args.u, yoStats["follower_count"])
#for follower in followers:
#  print bot.get_username_from_userid(follower)
#  time.sleep(0.25)

yoMedia = bot.get_total_user_medias(userID)
likers = []
i = 0

for media in yoMedia:
  i += 1
  print "Media:" + str(i) + " of " + str(len(yoMedia))
  likers = likers + bot.get_media_likers(media)
  time.sleep(0.25)
print "Got All Likers"

likerStats = {}
followerStats = {}
with open('hashtag_liked.tsv','rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')
    #print tsvin
    i = 0
    for row in tsvin:
      i += 1
      print "tsv row " + str(i) + " of " + str(len(tsvin))
      if row[3] in likers:
      	if row[1] in likerStats:
      		likerStats[row[1]] += 1
      	else:
      		likerStats[row[1]] = 1
      if row[3] in followers:
      	if row[1] in followerStats:
      		followerStats[row[1]] += 1
      	else:
      		followerStats[row[1]] = 1
      	print "follower: " + row[1]
print "followerStats:"
print followerStats
print "likerStats:"
print likerStats