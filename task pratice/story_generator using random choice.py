#story generator using random.choice() and (who,how,where,when,what)

import random

# Take user's name
who = input("Enter your name: ")

when = [
    "Yesterday",
    "Last night",
    "One morning",
    "Last Sunday",
    "A few days ago"
]

what = [
    "found a mysterious box",
    "won a lottery",
    "discovered a treasure",
    "found a magic phone",
    "saw a strange animal"
]

how = [
    "by accident",
    "while walking",
    "while going to college",
    "during a trip",
    "while searching for something"
]

where = [
    "in a forest",
    "near the beach",
    "in a college",
    "at a railway station",
    "in a village"
]

story = (
    random.choice(when) + ", " +
    who + " " +
    random.choice(what) + " " +
    random.choice(how) + " " +
    random.choice(where) + "."
)

print("\nStory:")
print(story)
