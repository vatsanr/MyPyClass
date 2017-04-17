print ('Converts Celsius to Fahrenheit')
def celtofahr(celsius):
    if float(celcius) < -273.15:
        return "celcius data invalid range"
    else:
        fahr=float(celsius)*9/5+32
        return fahr

celcius=input("Enter temp in celcius: ")
print(celtofahr(celcius))

temperatures=[10,-20,-289,100]
for i in temperatures:
    print(celtofahr(i))
