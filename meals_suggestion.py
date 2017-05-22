#!/usr/bin/python
"""
This program lists a series of meals for the week according to the season
provided by the user.
"""
##############################################################################
#                               LIBRARIES                                    #
##############################################################################
import csv
import random

##############################################################################
#                               CONSTANTS                                    #
##############################################################################
SEASON_INPUT = {
        "spring": ["printemps", "spring", ],
        "summer": ["ete", "été", "summer", ],
        "autumn": ["automne", "autumn", ],
        "winter": ["hiver", "winter", ],
}

MEALS_BY_SEASON = {
        "spring": [],
        "summer": [],
        "autumn": [],
        "winter": [],
}

FNAME = "dishes.csv"

##############################################################################
#                               FUNCTIONS                                    #
##############################################################################


def convert_csv_to_dict(csv_file):
    with open(csv_file) as f:
        f.readline()
        d = dict(csv.reader(f, delimiter=','))
        for key, value in d.items():
            MEALS_BY_SEASON[value].append(key)


def check_validity_season(wanted_season):
    for key, value in SEASON_INPUT.items():
        if wanted_season in value:
            return key
    else:
        print("Attention, la saison est mal orthographiee")


def select_dishes(current_season):
    menu = []
    count = 0
    while len(menu) < 5 and count < 10:
        meal = random.choice(MEALS_BY_SEASON[current_season])
        print(meal)
        if meal not in menu:
            menu.append(meal)
        count += 1
    return menu

##############################################################################
#                               MAIN                                         #
##############################################################################


def main():
    # parse .csv file
    convert_csv_to_dict(FNAME)
    # demand informations to user: current season
    print("Tapez le nom de l'actuelle saison : ")
    wanted_season = input().lower()
    current_season = check_validity_season(wanted_season)
    print(MEALS_BY_SEASON)
    menu = select_dishes(current_season)
    print(menu)


if __name__ == '__main__':
    main()

# Releases
# program takes arguments or not: file .csv + season
# program detects the default language of operating system
# the result could give more informations: recipe's details ; ingredients
