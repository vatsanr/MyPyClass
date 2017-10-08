import random

# generate Education level based on distribution by zipcode
# zipcodeedudist.csv format - <zipcode><count><list of <<choice><dist.probability>>

trans_list = []
with open("Transportation-s.csv",'r') as file:
    for line in file:
        fields = line.split(",")
        if fields[0] == "Subject":
            for i in range(2,8):
                trans_list.append(fields[i])
#            print(trans_list)
        else:
            zipcode=fields[0]
            count=int(fields[1])

            # Education generation
            # first argument - education choices
            #second argument - probability distribution
            # third argument - size of list
            trans_choices = random.choices([trans_list[0],trans_list[1],trans_list[2],trans_list[3],trans_list[4],trans_list[5]],\
                                  [float(fields[2]),float(fields[3]),float(fields[4]),float(fields[5]),float(fields[6]),float(fields[7])],k=count)
            for trans in trans_choices:
                print (zipcode,"Transportation", trans)
