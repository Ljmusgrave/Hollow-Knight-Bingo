"""
Run this program, then copy the result to "Board" under
"Custom(Advanced)" Game on bingosync.com

Add to bingo_list in the following code for more customized bingo options
using "{\"name\": \"TYPE_GOAL_HERE\"}"
"""

import random

amount = 25
bingo_list = ["{\"name\": \"Save 5 Grubs\"}",
              "{\"name\": \"Obtain 1 Pale Ore\"}",
              "{\"name\": \"Obtain Love Key\"}",
              "{\"name\": \"Obtain 2 Charm Notches\"}",
              "{\"name\": \"Buy 2 Maps\"}",
              "{\"name\": \"Buy 5 Maps\"}",
              "{\"name\": \"Howling Wraiths\"}",
              "{\"name\": \"Mantis Claw\"}",
              "{\"name\": \"Crystal Heart\"}",
              "{\"name\": \"Uumuu\"}",
              "{\"name\": \"Soul Master\"}",
              "{\"name\": \"4 Mask Shards\"}",
              "{\"name\": \"3 Vessel Fragments\"}",
              "{\"name\": \"Vengeful Spirit\"}",
              "{\"name\": \"Cyclone Slash\"}",
              "{\"name\": \"Shopkeeper’s Key\"}",
              "{\"name\": \"Dream Gate\"}",
              "{\"name\": \"Shaman Stone + Spell Twister\"}",
              "{\"name\": \"Use 1 Simple Key\"}",
              "{\"name\": \"Tram Pass\"}",
              "{\"name\": \"Monarch Wings\"}",
              "{\"name\": \"Obtain Dream Nail\"}",
              "{\"name\": \"Lumafly Lantern\"}",
              "{\"name\": \"Sprintmaster + Dashmaster\"}",
              "{\"name\": \"Sell 3 Relics to Lemm\"}",
              "{\"name\": \"Dung Defender\"}",
              "{\"name\": \"Xero\"}",
              "{\"name\": \"Gruz Mother\"}",
              "{\"name\": \"Brooding Mawlek\"}",
              "{\"name\": \"Enraged Guardian 1\"}",
              "{\"name\": \"Acquire 10 charms\"}"
              ]

random.shuffle(bingo_list)
final = bingo_list[:amount]

print("[")
for element in final[:-1]:
    print(" "+element+",")
print(" "+final[-1])
print("]\n")
