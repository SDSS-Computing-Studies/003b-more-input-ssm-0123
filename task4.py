#!python3
 
"""
Assignment 5:
Make a Mad Lib

Ask the user to enter a number of words, one for each of the underscored words in the following paragraph.  Once they have finished, display the following story to them with the replacements made in the Mad Lib

Today we picked apple from _PERSON_'s Orchard. I had no idea there were so many different varieties of apples. I ate _ADJECTIVE_ apples straight off the tree that tasted like _FOOD_. Then there was a _ADJECTIVE_ apple that looked like a _NOUN_.  When our bag was full, we went on a free hay ride to _PLACE_ and back. It ended at a hay pile where we got to _VERB_ _ADVERB_. I can hardly wait to get home and cook with the apples. We are going to make apple _FOOD_ and _THINGS_ pies!
"""


PERSON = input("person").strip()
adj1 = input("adjective").strip()
food = input("food").strip()
adj2 =input ("adjective").strip()
noun = input("noun").strip()
place = input("place").strip()
verb = input("verb").strip()
adverb = input("adverb").strip()
food2 = input("food").strip()
things = input("things").strip()

print ("Today we picked apple from",PERSON+"'s Orchard. I had no idea there were so many different varieties of apples. I ate "+ adj1 +" apples straight off the tree that tasted like "+ food +". Then there was a "+ adj2 +" apple that looked like a "+noun+".  When our bag was full, we went on a free hay ride to "+place+" and back. It ended at a hay pile where we got to "+verb, adverb+". I can hardly wait to get home and cook with the apples. We are going to make apple "+ food2 +" and "+things+" pies!")