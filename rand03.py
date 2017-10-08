import random

def weighted_choice(weights):
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random.random() * running_total
    for i, total in enumerate(totals):
        if rnd < total:
            return i

for i in range(10):
    weights= [0.2,0.3,0.5]
    list = weighted_choice(weights)
    print (list)

#zipcodef = open("zipcodes.txt","r")
#for lines in zipcodef:
#        values = lines.split()
#        number = random.randrange(int(values[1]),int(values[2]))
#        print (values[0],number)
