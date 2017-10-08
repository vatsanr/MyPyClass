import random

# Generate salary based on income distribution by zipcode
# zipcodeedudist.csv format - <zipcode><count><list of <<choice><dist.probability>>

with open("Household_income-s.csv",'r') as file:
    for line in file:
        fields = line.split()
    # Control fields in heading
        if fields[0] == "Heading":
            range1 = "0" + ' ' + fields[2]
            print(fields[2])
            range2_min = int(fields[2]) + 1
            range2 = str(range2_min)  + ' ' + fields[3]
            range3_min = int(fields[3]) + 1
            range3 = str(range3_min) + ' ' + fields[4]
            range4_min = int(fields[4]) + 1
            range4 = str(range4_min) + ' ' + fields[5]
            range5_min = int(fields[5]) + 1
            range5 = str(range5_min) + ' ' + fields[6]
            range6_min = int(fields[6]) + 1
            range6 = str(range6_min) + ' ' + fields[7]
            range7_min = int(fields[7]) + 1
            range7 = str(range7_min) + ' ' + fields[8]
            range8_min = int(fields[8]) + 1
            range8 = str(range8_min) + ' ' + fields[9]
            range9_min = int(fields[9]) + 1
            range9 = str(range9_min) + ' ' + fields[10]
            range10_min = int(fields[10]) + 1
            range10 = str(range10_min) + ' ' + fields[11]
        else:
            zipcode=fields[0]
            count=int(fields[1])
            #print (range1,range2,range3,range4,range5,range6,range7,range8,range9,range10)
            # Salary generation
            # first argument - polulation list
            # second argument - probablity distribution
            # third argument - size of list
            s_choice = random.choices([range1,range2,range3,range4,range5,range6,range7,range8,range9,range10],\
                                  [float(fields[2]),float(fields[3]),float(fields[4]),float(fields[5]),float(fields[6]),float(fields[7]),float(fields[8]),float(fields[9]),float(fields[10]),float(fields[11])],k=count)
            for i in s_choice:
                min_max = i.split()
                salary = random.randint(int(min_max[0]),int(min_max[1]))
                print (zipcode,"Salary", salary)
