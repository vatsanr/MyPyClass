from census import Census
from us import states

c = Census("79d91c12a49eb82eca73eedf242f9cd13414e474")
geoarea_homes = c.acs5.state(('NAME','B25034_010E'), states.MD.fips)
print (geoarea_homes)
print (c.acs5.state('B01001_004E', Census.ALL))
