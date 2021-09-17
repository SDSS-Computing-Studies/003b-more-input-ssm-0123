#!python3
 
"""
Assignment 5:
Make a Mad Lib

Ask the user to enter a number of words, one for each of the underscored words in the following paragraph.  Once they have finished, display the following story to them with the replacements made in the Mad Lib

Today we picked apple from _PERSON_'s Orchard. I had no idea there were so many different varieties of apples. I ate _ADJECTIVE_ apples straight off the tree that tasted like _FOOD_. Then there was a _ADJECTIVE_ apple that looked like a _NOUN_.  When our bag was full, we went on a free hay ride to _PLACE_ and back. It ended at a hay pile where we got to _VERB_ _ADVERB_. I can hardly wait to get home and cook with the apples. We are going to make apple _FOOD_ and _THINGS_ pies!
"""

PERSON = input("Today we picked apple from ________'s Orchard.")
print("I had no idea there were so many different varieties of apples.")
adj = input("I ate _______ apples straight off the tree")
food = input("that tasted like ______.")
ADJ = input("Then there was a ________ apple")
noun = input("that looked like a ____.")
place = input(" When our bag was full, we went on a free hay ride to _____ and back.")
verb = input("It ended at a hay pile where we got to VERB")
adverb = input("(any adverb)")

Food = input("")