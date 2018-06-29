"""
    instabot example

    Workflow:
        1) unfollows users that don't follow you.
"""

import sys
import os
import argparse

sys.path.append(os.path.join(sys.path[0], '../'))

from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
args = parser.parse_args()

bot = Bot()
bot.login(username=args.u, password=args.p,
          proxy=args.proxy)
print(bot.get_user_info(bot.get_userid_from_username("rozekid")))