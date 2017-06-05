#Handles input/output files !!!

names=["Kevin","Joseph","Mike","Kumar","Laura"]
dobs=["04/05/1970","10/05/1960","08/03/1966","05/30/1996","07/20/1998"]
with open("pyoutput01.txt",'w') as file:
    for i in range(4):
        file.write(names[i]+"|"+dobs[i]+"\n")
print("Wrote out an output file with names and dob")
contents=open("pyoutput01.txt",'r')
print(contents.read())
contents.close();
addmore=open("pyoutput01.txt",'a')
addmore.write(names[4]+"|"+dobs[4])
addmore.close()
contents=open("pyoutput01.txt",'r')
print(contents.read())
contents.close();
