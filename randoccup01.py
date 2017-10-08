import random

# generate Education level based on distribution by zipcode
# zipcodeedudist.csv format - <zipcode><count><list of <<choice><dist.probability>>

occup_list = []
with open("Occupation-s.csv",'r') as file:
    for line in file:
        fields = line.split(",")
        if fields[0] == "Subject":
            for i in range(2,7):
                occup_list.append(fields[i])
#            print(occup_list)
        else:
            zipcode=fields[0]
            count=int(fields[1])

            # Education generation
            # first argument - education choices
            #second argument - probability distribution
            # third argument - size of list
            occup_choices = random.choices([occup_list[0],occup_list[1],occup_list[2],occup_list[3],occup_list[4]],\
                                  [float(fields[2]),float(fields[3]),float(fields[4]),float(fields[5]),float(fields[6])],k=count)
            for occup in occup_choices:
                print (zipcode,"Occupation", occup)
