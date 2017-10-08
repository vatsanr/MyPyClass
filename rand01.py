import random

zipcodef = open("zipcodes.txt","r")
for lines in zipcodef:
        values = lines.split()
        number = random.randrange(int(values[1]),int(values[2]))
        print (values[0],number)
