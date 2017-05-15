#!/usr/bin/python
"""
This program lists a series of meals for the week according to the season
provided by the user.
"""
##### LIBRARIES #####
import csv
import random

##### CONSTANTS #####
SEASON_INPUT = [
        "printemps", "spring",
        "ete", "été", "summer",
        "automne", "autumn",
        "hiver", "winter",
]

FNAME = "menus.csv"

##### USER DEFINED FUNCTIONS #####


##### MAIN PROGRAM #####
def main():
    # parse .csv file
    # demand informations to user: current season
    # choice a random meal in the current season
    # print the result


## Releases
# program takes arguments or not: file .csv + season
# program detects the default language of operating system and change his interface
# the result could give more informations: recipe's details ; ingredients

"""
file = open(FNAME, 'r')
data_list = []
autumn_list = []
winter_list = []
spring_list = []
summer_list = []
for line in file:
    if "\"menu\"" not in line:
        data_list.append(line.strip().split(','))
        """
        if "\"automne\"" not in line:
            autumn_list.append(line.strip().split(','))
        elif "\"hiver\"" not in line:
            winter_list.append(line.strip().split(','))
        elif "\"printemps\"" not in line:
            spring_list.append(line.strip().split(','))
        elif "\"ete\"" not in line:
            summer_list.append(line.strip().split(','))
        """
file.close()
print(autumn_list,winter_list,spring_list,summer_list)
print(data_list)

def buildMenus(season):
    selectedMeals = []
    selectedMeals.append(random.choice(data_list))
    return selectedMeals

print("Tapez le nom de l'actuelle saison : ")
season = input().lower()
if season in SEASON_INPUT:
    print(season)
    selectedMeals = buildMenus(season)
    print(selectedMeals)
else:
    print("Attention, la saison est mal orthographiee")

if season == "ete":
    print("ete")
elif season == "automne":
    print("automne")
elif season == "hiver":
    print("hiver")
elif season == "printemps":
    print("printemps")
"""
