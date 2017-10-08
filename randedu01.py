import random

# generate Education level based on distribution by zipcode
# zipcodeedudist.csv format - <zipcode><count><list of <<choice><dist.probability>>

edu_list = []
with open("Educational_attainment-s.csv",'r') as file:
    for line in file:
        fields = line.split(",")
        if fields[0] == "Subject":
            for i in range(2,9):
                edu_list.append(fields[i])
            print(edu_list)
        else:
            zipcode=fields[0]
            count=int(fields[1])

            # Education generation
            # first argument - education choices
            #second argument - probability distribution
            # third argument - size of list
            edu_choices = random.choices([edu_list[0],edu_list[1],edu_list[2],edu_list[3],edu_list[4],edu_list[5],edu_list[6]],\
                                  [float(fields[2]),float(fields[3]),float(fields[4]),float(fields[5]),float(fields[6]),float(fields[7]),float(fields[8])],k=count)
            for edu in edu_choices:
                print (zipcode,"Education", edu)
