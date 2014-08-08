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
elif total <=8;
    print "Not bad!"
elif total <=12;
    print "Nice!"

#alternate approach with functions:

# def respond_to_total(total):
#     if total <= 4:
#         message = "Yikes!"
#     elif total <= 8:
#         message = "Not Bad!"
#     else:
#         message = "Nice!"
#     return message

# def main():
#     d1 = random.randint(1, 6)
#     d2 = random.randint(1, 6)
#     total = d1 + d2
#     summary = "Your dice were %s and %s" % (d1, d2)
#     evaluation = respond_to_total(total)
#     print summary
#     print evaluation

# main()