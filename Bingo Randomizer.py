"""
Run this program, then copy the result to "Board" under
"Custom(Advanced)" Game on bingosync.com

Add to bingo_list in the following code for more customized bingo options
using "{\"name\": \"TYPE_GOAL_HERE\"}"
"""

import random

amount = 25
bingo_list = [
              # GRUBS
              "{\"name\": \"Save 5 Grubs\"}",
              "{\"name\": \"Save 15 Grubs\"}",

              # SPELLS + ABILITIES
              "{\"name\": \"Howling Wraiths\"}",
              "{\"name\": \"Mantis Claw\"}",
              "{\"name\": \"Vengeful Spirit\"}",
              "{\"name\": \"Crystal Heart\"}",
              "{\"name\": \"Monarch Wings\"}",
              "{\"name\": \"Isma's Tear\"}",

              # BOSSES
              "{\"name\": \"Uumuu\"}",
              "{\"name\": \"Soul Master\"}",
              "{\"name\": \"Dung Defender\"}",
              "{\"name\": \"Xero\"}",
              "{\"name\": \"Gruz Mother\"}",
              "{\"name\": \"Brooding Mawlek\"}",
              "{\"name\": \"Enraged Guardian 1\"}",
              "{\"name\": \"Shroomal Ogres\"}",

              # MASKS + VESSELS
              "{\"name\": \"4 Mask Shards\"}",
              "{\"name\": \"3 Vessel Fragments\"}",

              # NAIL ARTS
              "{\"name\": \"Cyclone Slash\"}",
              "{\"name\": \"Great Slash\"}",
              "{\"name\": \"Dash Slash\"}",

              # SHOPS + VENDORS
              "{\"name\": \"Shopkeeper’s Key\"}",
              "{\"name\": \"Buy 2 Maps\"}",
              "{\"name\": \"Buy 5 Maps\"}",
              "{\"name\": \"Lumafly Lantern\"}",
              "{\"name\": \"Sell 3 Relics to Lemm\"}",
              "{\"name\": \"Obtain 1 Pale Ore\"}",
              "{\"name\": \"Channelled Nail (2 upgrades)\"}",
              "{\"name\": \"Coiled Nail (3 upgrades)\"}",

              # CHARMS
              "{\"name\": \"Acquire 10 charms\"}",
              "{\"name\": \"Acquire 15 charms\"}",
              "{\"name\": \"Shaman Stone + Spell Twister\"}",
              "{\"name\": \"Sprintmaster + Dashmaster\"}",
              "{\"name\": \"Flukenest + Defender's Crest\"}",
              "{\"name\": \"Soul Catcher + Soul Eater\"}",
              "{\"name\": \"Shape of Unn\"}",
              "{\"name\": \"Glowing Womb\"}",

              # DREAMERS + ESSENCE
              "{\"name\": \"Monomon\"}",
              "{\"name\": \"Lurien\"}",
              "{\"name\": \"Herrah\"}",
              "{\"name\": \"Dream Nail\"}",
              "{\"name\": \"Dream Gate\"}",
              "{\"name\": \"500 Essence\"}",

              # STAG STATIONS
              "{\"name\": \"Open 5 Stag Stations\"}",
              "{\"name\": \"Distant Village Stag\"}",
              "{\"name\": \"King's Station Stag\"}",
              "{\"name\": \"Queen's Station Stag\"}",

              # ENTER AREAS
              "{\"name\": \"Enter Royal Waterways\"}",
              "{\"name\": \"Enter The Hive\"}",
              "{\"name\": \"Enter The Abyss\"}",

              # MISC.
              "{\"name\": \"1500 Geo in the Bank\"}",
              "{\"name\": \"Bounce Zote's Head 3 Times\"}",
              "{\"name\": \"Use 2 Simple Keys\"}",
              "{\"name\": \"Tram Pass\"}",
              "{\"name\": \"Obtain Love Key\"}",
              "{\"name\": \"Obtain 2 Charm Notches\"}"
              ]

random.shuffle(bingo_list)
final = bingo_list[:amount]

print("[")
for element in final[:-1]:
    print(" "+element+",")
print(" "+final[-1])
print("]\n")
