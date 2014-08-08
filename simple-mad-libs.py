# a simple mad libs game, with no error messaging

from datetime import datetime

year_born = raw_input("What year were you born?")
adj = raw_input("Enter an adjective:")
noun = raw_input("Enter a noun:")
place = raw_input("Enter a place:")

now = datetime.now()
years_ago = now.year - int(year_born)

story = "In %s, exactly %s years ago, a %s %s was born in %s. It was you!" % (year_born, years_ago, adj, noun, place)

print story

