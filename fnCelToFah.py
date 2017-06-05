print ('Converts Celsius to Fahrenheit')
def celtofahr(celsius):
    if float(celcius) < -273.15:
        return "celcius data invalid range"
    else:
        fahr=float(celsius)*9/5+32
        return fahr

celcius=input("Enter temp in celcius: ")
print(celtofahr(celcius))
# file writing example
temperatures=[10,-20,-289,100]
file=open("temps-in-farh.txt",'w')
for i in temperatures:
    if float(i) > -273.15:
        file.write(str(celtofahr(i))+"\n")
file.close()
