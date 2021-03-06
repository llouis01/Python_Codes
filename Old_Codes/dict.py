# dictionaries in python ; dict = {x : 'none',... }; key-value pair

# suppose you have two list of countries and their population
x = ['Haiti', 'Zoolandia', 'Wakanda', 'Diagon Alley']
y = [11.2, 32.4, 333.1, 0.002] # in million

# if you need the population of Zoolandia, you can...
indx_zld = x.index('Zoolandia')
zld_pop = y[indx_zld]
print("The hard way still works -->",zld_pop)

# but that is very confusing and non-intuitive
print()

#instead, we can create a dictionary
ctr_pop = {'Haiti' : 11.2, 'Zoolandia' : 32.4, 'Wakanda' : 333.1, 'Diagon Alley' : 0.002}
print("With keys:", ctr_pop.keys())
print()
print("And values:", ctr_pop.values())
print()
print("Population of Zoolandia is", ctr_pop['Zoolandia'], "million.") # var[key]=key_val
print()

"""
dictionaries cannot contain duplicates and contents are immutable objects.
if I try to include another key that already exists, the value will be up-
dated but the additional key will not be included.
"""

ctr_pop = {'Haiti' : 11.2, 'Zoolandia' : 32.4, 'Wakanda' : 333.1,
           'Diagon Alley' : 0.002, 'Zoolandia' : 39.3}

print(ctr_pop) # the last value entered for the preexisting key will be kept
print()

ctr_pop["Hogwarts"] = 0.000035 # adding to a dict with dict[key_to_add] = key_value
print(ctr_pop)
print()

print("Seaburst" in ctr_pop) # bool check if a key is present
print()

ctr_pop["Haiti"] = 12.0 # updating a key
print(ctr_pop)
print()

del(ctr_pop["Hogwarts"]) # removing elements from a dictionary
print(ctr_pop)
print()

ctr_pop["Haiti"] = {'capital': 'port-au-prince', 'population': 3} # dictionary can be a dictionary of dictionary
ctr_pop["Zoolandia"] = {'capital': 'zoopitoo', 'population': 1.3}
ctr_pop["Wakanda"] = {'capital': 'Harlem', 'population': 0.7}
ctr_pop["Diagon Alley"] = {'capital': 'London', 'population': 1.8}
print(ctr_pop)
print()

print(ctr_pop['Wakanda']['capital'])
print()

murder_stats = {'homicide': 'not enough data', 'accidents': 'not enough data'}
ctr_pop['Murder Total']= murder_stats
print(ctr_pop)