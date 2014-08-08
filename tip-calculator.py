# a basic tip calculator

meal = float(raw_input("What's the bill?")) #convert to a number with decimals
tip = float(raw_input("What tip percent?"))/100.0 #keep the decimal in 100 to handle floats in fraction

total = meal + (meal * tip)

print total