import random

vowels='aeiouy'
consonants='bcdfghjklmnpqrstvwxz'
alphabets=vowels+consonants

letter1=input("Choose between 'v' for vowel, 'c' for consonants and 'a' for alphabets: ")
letter2=input("Choose between 'v' for vowel, 'c' for consonants and 'a' for alphabets: ")
letter3=input("Choose between 'v' for vowel, 'c' for consonants and 'a' for alphabets: ")

def namegenerator(letter):
    if letter == 'v':
        namel=random.choice(vowels)
    elif letter == 'c':
        namel=random.choice(consonants)
    elif letter == 'a':
        namel=random.choice(alphabets)
    else:
        namel=letter
    return(namel)

with open("babynames.txt",'w') as file:
    for i in range(20):
        file.write(namegenerator(letter1)+namegenerator(letter2)+namegenerator(letter3)+"\n")
        
