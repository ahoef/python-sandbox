# a simple script that imports and uses a standard python library, uses string concatenation, and uses conditional logic

import random

dice_1 = random.randint(1, 6) # will give you a random integer between 1 and 6
dice_2 = random.randint(1, 6) # will give you a different random integer between 1 and 6
total = dice_1 + dice_2

print "Your numbers are %s and %s" % (dice_1, dice_2)
# same as:
# print "Your numbers are " + str(dice_1) + " and " + str(dice_2)

if total <= 4:
    print "Yikes!"
elif total >= 5 and total <= 8:
    print "Not bad!"
elif total >=9 and total <=12:
    print "Nice!"